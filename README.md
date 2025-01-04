# Proxy Checker - Verificador de Proxies SOCKS4, SOCKS5 e HTTP/HTTPS 🕵️‍♂️

## O que é este script?

Este script em Python foi desenvolvido para verificar a **atividade e o status** de proxies HTTP, HTTPS, SOCKS4 e SOCKS5. Ele realiza a verificação de forma eficiente e paralela, utilizando múltiplas threads para garantir um desempenho rápido. Proxies válidas são identificadas e salvas em um arquivo de saída, enquanto as inativas são descartadas.

## Como funciona?

1. **Carrega proxies**: O script lê um arquivo de texto chamado `proxies.txt`, que contém uma lista de proxies no formato `IP:PORTA`. Esses proxies podem ser de qualquer um dos seguintes tipos:
   - **HTTP**: Exemplo `192.168.0.1:8080`
   - **HTTPS**: Exemplo `192.168.0.2:443`
   - **SOCKS4**: Exemplo `socks4://192.168.0.3:1080`
   - **SOCKS5**: Exemplo `socks5://192.168.0.4:1080`

2. **Verificação**: O script tenta se conectar ao URL de teste (`https://www.google.com`) usando cada proxy e mede o **tempo de resposta** (ping). Se a conexão for bem-sucedida, o script considera a proxy **ativa**.

3. **Resultado**:
   - Se a proxy estiver **ativa**, o script exibe uma mensagem indicando que ela está "viva", junto com o tempo de resposta (ping).
   - Se a proxy estiver **inativa**, o script a marca como "morta".

4. **Armazenamento das proxies ativas**: Após a execução, todas as proxies que funcionaram corretamente são salvas em um arquivo chamado `active_proxies.txt`, para que você possa usá-las novamente no futuro.

## Detalhes Técnicos

- **Verificação Paralela**: O script utiliza **multithreading** (Threads) para realizar a verificação de várias proxies ao mesmo tempo, garantindo um processo rápido e eficiente.
- **Suporte a SOCKS4/5**: A verificação funciona para proxies **SOCKS4** e **SOCKS5**, além de proxies **HTTP** e **HTTPS**.
- **Exibição de Status**: Durante a execução, o script fornece feedback ao vivo no terminal, exibindo o status de cada proxy.

## Exemplo de Saída

Durante a execução, você verá algo como:

```text
(192.168.0.1:8080) ESTÁ VIVA - PING: 85.23 MS
(socks5://192.168.0.2:1080) ESTÁ MORTA
(http://192.168.0.3:3128) ESTÁ VIVA - PING: 120.45 MS
Ao final, o script salvará as proxies ativas no arquivo active_proxies.txt.

Como Usar
Prepare um arquivo de proxies: Crie um arquivo de texto chamado proxies.txt com uma lista de proxies. Coloque uma proxy por linha no formato IP:PORTA, socks4://IP:PORTA ou socks5://IP:PORTA.

Execute o script:

No terminal, execute o seguinte comando:

bash
Copiar código
python proxy_checker.py
Aguarde o resultado: O script fará a verificação e, ao final, você verá o relatório com proxies ativas salvas em active_proxies.txt.

Personalização
Você pode personalizar o comportamento do script alterando algumas variáveis dentro do código:

TEST_URL: O URL utilizado para testar as proxies (padrão: https://www.google.com).
TIMEOUT: O tempo máximo de espera para cada proxy, em segundos (padrão: 5 segundos).
MAX_THREADS: O número máximo de threads para realizar a verificação em paralelo (padrão: 50).
PROXY_FILE: O nome do arquivo que contém as proxies para serem verificadas (padrão: proxies.txt).
OUTPUT_FILE: O nome do arquivo para salvar as proxies ativas (padrão: active_proxies.txt).
Requisitos
Este script exige a instalação das seguintes dependências Python:

requests
colorama
pysocks
Instale as dependências com o seguinte comando:

bash
Copiar código
pip install requests colorama pysocks
Contribuindo
Se você deseja melhorar ou adicionar novas funcionalidades ao script, fique à vontade para abrir um Pull Request ou relatar problemas através de Issues.

Licença
Este projeto está sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Desenvolvido com ♥ e Python!
