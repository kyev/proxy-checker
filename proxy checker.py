import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

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
    # Adiciona cada linha com a parte branca e a parte rosa sem espaços
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

def check_proxy(proxy, active_proxies):
    """Verifica se o proxy no formato IP:PORTA está ativo."""
    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        start_time = time.time()
        response = requests.get(TEST_URL, proxies=proxy_dict, timeout=TIMEOUT)
        ping = round((time.time() - start_time) * 1000, 2)  # Ping em milissegundos
        if response.status_code == 200:
            print(f"{Fore.GREEN}({proxy}) ESTÁ VIVA - PING: {ping} MS{RESET}")
            active_proxies.add(proxy)  # Adiciona a proxy ao set de proxies ativas
            return True
    except Exception:
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
