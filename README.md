🚀 Proxy Checker - Verificador de Proxies 💻🌐
Este script em Python permite verificar se suas proxies HTTP, HTTPS, SOCKS4 ou SOCKS5 estão ativas ou inativas. Você pode carregar um arquivo de proxies e o script vai testar a conectividade com um site de teste, como o Google. As proxies ativas serão salvas em um arquivo de saída para uso futuro.

📦 Requisitos
Python 3.x
Bibliotecas:
requests
colorama
concurrent.futures
Você pode instalar as dependências executando:

bash
Copiar código
pip install requests colorama
🔧 Funcionalidade
Verifica Proxies: O script testa proxies HTTP, HTTPS, SOCKS4 ou SOCKS5.
Exibe Status: Exibe proxies ativas (verdes) e mortas (vermelhas) no terminal.
Arquivos de Entrada e Saída:
O script lê proxies de arquivos como https_proxies.txt, socks4_proxies.txt, ou socks5_proxies.txt.
Proxies ativas são salvas no arquivo active_proxies.txt.
⚙️ Como Usar
Escolha o tipo de proxy:

Digite 1 para HTTP/HTTPS.
Digite 2 para SOCKS4.
Digite 3 para SOCKS5.
Forneça o arquivo de proxies:

O script irá perguntar o tipo de proxy que você quer testar.
Tenha arquivos de proxies como https_proxies.txt, socks4_proxies.txt ou socks5_proxies.txt prontos.
Verifique as proxies:

O script irá testar as proxies, mostrando no terminal se estão vivas ou mortas.
As proxies vivas são salvas no arquivo active_proxies.txt.
Exemplo de Execução no Terminal:
bash
Copiar código
$ python proxy_checker.py
Você verá o seguinte no terminal:

markdown
Copiar código
Escolha o tipo de proxy para verificar:
1. HTTPS (HTTP/HTTPS)
2. SOCKS4
3. SOCKS5

Digite o número correspondente: 1

(192.168.0.1:8080) HTTP/HTTPS ESTÁ VIVA
(192.168.0.2:8080) SOCKS5 ESTÁ MORTA
...
🌈 Personalização
Cores Personalizadas: O script utiliza a biblioteca colorama para colorir a saída no terminal:
🟩 Verde: Proxy ativa.
🟥 Vermelho: Proxy inativa.
💖 Rosa: Estilo do texto.
⚪ Branco: Informações gerais.
📄 Arquivos de Entrada
O script espera que os arquivos de proxies estejam no formato:

https_proxies.txt para proxies HTTP/HTTPS.
socks4_proxies.txt para proxies SOCKS4.
socks5_proxies.txt para proxies SOCKS5.
Cada linha desses arquivos deve conter um proxy no formato:

makefile
Copiar código
ip:porta
Exemplo:

makefile
Copiar código
192.168.1.1:8080
203.0.113.0:1080
💾 Arquivo de Saída
Após a verificação, o script salva as proxies ativas no arquivo:

Copiar código
active_proxies.txt
Cada proxy ativa será salva no formato ip:porta.

🧑‍💻 Autor
Feito por Caique 😎

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
