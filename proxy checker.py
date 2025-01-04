import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import socks
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

# Inicializa o colorama
init(autoreset=True)

# Configurações
TEST_URL = "https://www.google.com"  # URL para testar proxies
TIMEOUT = 5  # Tempo limite em segundos para cada proxy
MAX_THREADS = 50  # Máximo de threads simultâneas
PROXY_FILE = "proxies.txt"  # Arquivo com a lista de proxies
OUTPUT_FILE = "active_proxies.txt"  # Arquivo para salvar proxies ativas

# Define as cores ANSI
WHITE = "\x1b[37m"
PINK = "\x1b[38;5;213m"  # Rosa choque
RESET = "\x1b[0m"

# Texto em ASCII com alinhamento ajustado
ASCII_WHITE = [
    f"{WHITE}██╗  ██╗ █████╗ {RESET}",
    f"{WHITE}██║  ██║██╔══██╗{RESET}",
    f"{WHITE}███████║███████║{RESET}",
    f"{WHITE}██╔══██║██╔══██║{RESET}",
    f"{WHITE}██║  ██║██║  ██║{RESET}",
    f"{WHITE}╚═╝  ╚═╝╚═╝  ╚═╝{RESET}"
]

ASCII_PINK = [
    f"{PINK}██╗  ██╗ █████╗ {RESET}",
    f"{PINK}██║  ██║██╔══██╗{RESET}",
    f"{PINK}███████║███████║{RESET}",
    f"{PINK}██╔══██║██╔══██║{RESET}",
    f"{PINK}██║  ██║██║  ██║{RESET}",
    f"{PINK}╚═╝  ╚═╝╚═╝  ╚═╝{RESET}"
]

# Combine as versões em branco e rosa na mesma linha sem espaço
ASCII = ""
for i in range(len(ASCII_WHITE)):
    ASCII += f"{ASCII_WHITE[i]}{ASCII_PINK[i]}\n"

# Funções principais
def load_proxies(file_path):
    """Carrega as proxies de um arquivo."""
    try:
        with open(file_path, "r") as file:
            return [line.strip().upper() for line in file if line.strip()]  # Convertendo para maiúsculas
    except FileNotFoundError:
        print(f"ERRO: ARQUIVO '{file_path}' NÃO ENCONTRADO.")
        return []

def load_active_proxies(output_file):
    """Carrega as proxies ativas já salvas no arquivo, removendo duplicatas."""
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            return set(line.strip() for line in file)  # Usando set para garantir unicidade
    return set()

def save_active_proxies(active_proxies):
    """Salva as proxies ativas no arquivo, sem duplicatas."""
    with open(OUTPUT_FILE, "w") as file:
        for proxy in active_proxies:
            file.write(proxy + "\n")

class SOCKSAdapter(HTTPAdapter):
    """Adaptador para suportar proxies SOCKS4 e SOCKS5."""
    def __init__(self, proxy_url, **kwargs):
        self.proxy_url = proxy_url
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs['proxy_url'] = self.proxy_url
        return super().init_poolmanager(*args, **kwargs)

def check_proxy(proxy, active_proxies):
    """Verifica se o proxy no formato IP:PORTA está ativo, incluindo SOCKS4 e SOCKS5."""
    try:
        # Primeiramente tentamos SOCKS5
        proxy_dict = {
            "http": f"socks5://{proxy}",
            "https": f"socks5://{proxy}",
        }
        session = requests.Session()
        session.mount("http://", SOCKSAdapter(proxy_dict["http"]))
        session.mount("https://", SOCKSAdapter(proxy_dict["https"]))
        response = session.get(TEST_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            print(f"{Fore.GREEN}({proxy}) SOCKS5 ESTÁ VIVA{RESET}")
            active_proxies.add(proxy)
            return True
    except Exception:
        pass

    try:
        # Se falhou no SOCKS5, tentamos SOCKS4
        proxy_dict = {
            "http": f"socks4://{proxy}",
            "https": f"socks4://{proxy}",
        }
        session = requests.Session()
        session.mount("http://", SOCKSAdapter(proxy_dict["http"]))
        session.mount("https://", SOCKSAdapter(proxy_dict["https"]))
        response = session.get(TEST_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            print(f"{Fore.GREEN}({proxy}) SOCKS4 ESTÁ VIVA{RESET}")
            active_proxies.add(proxy)
            return True
    except Exception:
        pass

    try:
        # Tentamos HTTP/HTTPS
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }
        session = requests.Session()
        session.proxies.update(proxy_dict)
        response = session.get(TEST_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            print(f"{Fore.GREEN}({proxy}) HTTP/HTTPS ESTÁ VIVA{RESET}")
            active_proxies.add(proxy)
            return True
    except Exception:
        pass

    # Se nenhuma das tentativas funcionou, o proxy é considerado inativo
    print(f"{Fore.RED}({proxy}) ESTÁ MORTA{RESET}")
    return False

def main():
    # Carrega as proxies do arquivo
    proxies = load_proxies(PROXY_FILE)
    if not proxies:
        print("NENHUMA PROXY ENCONTRADA NO ARQUIVO.")
        return

    # Carrega as proxies ativas já salvas, removendo duplicatas
    active_proxies = load_active_proxies(OUTPUT_FILE)

    # Exibe o ASCII com o logo
    print(ASCII)

    # Avisa o usuário para pressionar 'Enter' para começar
    input("PRESSIONE 'ENTER' PARA COMEÇAR A VERIFICAR AS PROXIES...")

    # Verificação em paralelo usando ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        list(executor.map(lambda proxy: check_proxy(proxy, active_proxies), proxies))

    # Salva as proxies ativas
    save_active_proxies(active_proxies)

    # Exibe o resultado final
    print(f"\n{Fore.CYAN}VERIFICAÇÃO CONCLUÍDA. PROXIES ATIVAS SALVAS EM '{OUTPUT_FILE}'.{RESET}")

if __name__ == "__main__":
    main()
