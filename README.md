🚀 Proxy Checker - Verificador de Proxies Ativos
Este script Python é projetado para verificar a disponibilidade de proxies listados em um arquivo de texto. Ele verifica proxies de diferentes tipos, como SOCKS4, SOCKS5, HTTP e HTTPS, e retorna se estão ativas ou não. As proxies ativas são salvas em um arquivo para referência futura. ✅🌐

🛠️ Funcionalidades
Verificação em múltiplos tipos de proxies: O script tenta identificar proxies SOCKS5, SOCKS4, HTTP e HTTPS. 🔍
Verificação rápida: Utiliza a biblioteca ThreadPoolExecutor para verificar proxies em paralelo, aumentando a performance. ⚡
Suporte a SOCKS5 e SOCKS4: Usa a biblioteca requests com suporte para proxies SOCKS, além de HTTP/HTTPS. 🌐
Feedback visual colorido: Utiliza cores com colorama para destacar proxies ativas (verde) e inativas (vermelho). 🎨
Salvamento de proxies ativas: Armazena as proxies válidas em um arquivo de saída, removendo duplicatas. 📂
📦 Requisitos
Certifique-se de ter as bibliotecas necessárias instaladas antes de rodar o script:

bash
Copiar código
pip install requests colorama pysocks
📝 Como Usar
Prepare seu arquivo de proxies: Crie um arquivo de texto (proxies.txt) com uma lista de proxies no formato IP:PORTA. Coloque o arquivo na mesma pasta do script.
Execute o script: Rode o script Python para verificar as proxies. 👨‍💻
Exemplo de proxies.txt:
txt
Copiar código
192.168.1.1:8080
192.168.1.2:1080
123.45.67.89:3128
Verifique o resultado: O script criará um arquivo de saída chamado active_proxies.txt, onde serão salvas as proxies ativas. ✅
⚙️ Como Funciona
Etapas de execução:
O script carrega as proxies do arquivo proxies.txt.
Em seguida, verifica cada proxy individualmente.
Para cada proxy, o script tenta se conectar usando diferentes tipos de protocolos (SOCKS5, SOCKS4, HTTP/HTTPS).
Caso o proxy responda corretamente (status code 200), ele é considerado ativo e é adicionado ao arquivo active_proxies.txt. 📈
Ao final, o script imprime um resumo da execução e lista as proxies ativas no arquivo. 📄
Exemplo de saída:
csharp
Copiar código
Pressione 'ENTER' para começar a verificar as proxies... 👇
██╗  ██╗ █████╗   ██╗  ██╗ █████╗   
██║  ██║██╔══██╗ ██║  ██║██╔══██╗  
███████║███████║ ███████║███████║  
██╔══██║██╔══██║ ██╔══██║██╔══██║  
██║  ██║██║  ██║ ██║  ██║██║  ██║  
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝  

(192.168.1.1:8080) SOCKS5 ESTÁ VIVA ✅
(123.45.67.89:3128) HTTP/HTTPS ESTÁ VIVA ✅
(192.168.1.2:1080) ESTÁ MORTA ❌

Verificação concluída. Proxies ativas salvas em 'active_proxies.txt'. 📂
📂 Arquivos Gerados
proxies.txt: Arquivo com a lista de proxies a serem verificadas. 📋
active_proxies.txt: Arquivo com as proxies ativas após a verificação. ✅
⚙️ Configurações
Você pode personalizar algumas configurações do script:

TEST_URL: URL usada para testar as proxies. Atualmente está configurado para "https://www.google.com", mas pode ser alterado para qualquer URL de sua escolha. 🌍
TIMEOUT: O tempo máximo (em segundos) que o script espera por uma resposta de cada proxy. ⏱️
MAX_THREADS: Número máximo de threads simultâneas para a verificação de proxies. 💨
PROXY_FILE: Nome do arquivo que contém a lista de proxies para verificação (padrão: proxies.txt). 📂
OUTPUT_FILE: Nome do arquivo onde as proxies ativas serão salvas (padrão: active_proxies.txt). 💾
🖥️ Como Rodar
Clone ou baixe o script Python.
Crie ou edite o arquivo proxies.txt na mesma pasta do script.
Execute o script com:
bash
Copiar código
python proxy_checker.py
📜 Licença
Este projeto está licenciado sob a MIT License.

