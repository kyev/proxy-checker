# Proxy Checker 🕵️‍♂️🔍

Este script permite verificar a disponibilidade de proxies (HTTP/HTTPS) em massa, testando sua conectividade em múltiplos sites. Ele é ideal para quem precisa validar grandes listas de proxies e salvar aquelas que estão ativas em um arquivo.

## Funcionalidades

- **Verificação em massa**: O script permite testar várias proxies simultaneamente.
- **Testes em múltiplos sites**: A proxy é testada com um site principal (Google) para verificar sua funcionalidade.
- **Alta performance**: A verificação das proxies é feita em paralelo utilizando múltiplas threads.
- **Salvamento de proxies ativas**: Proxies que estiverem funcionando são salvas automaticamente em um arquivo.
- **Feedback visual**: O script utiliza cores para destacar proxies ativas e inativas, e também informa o tempo de resposta (ping) das proxies.

## Como Usar 🚀

1. **Pré-requisitos**:
    - Python 3.x instalado.
    - Bibliotecas necessárias: `requests`, `colorama`.
    - Um arquivo de texto (`proxies.txt`) contendo a lista de proxies a ser verificada.

2. **Instalação**:
    - Clone o repositório ou baixe o arquivo do script.
    - Instale as dependências executando:
    ```bash
    pip install requests colorama
    ```

3. **Estrutura de Arquivos**:
    - **proxies.txt**: Arquivo contendo a lista de proxies que você deseja testar.
    - **active_proxies.txt**: Arquivo de saída onde as proxies ativas serão salvas.
    - **proxy_checker.py**: O script principal que realiza a verificação.

4. **Execução**:
    - No terminal, navegue até a pasta do script e execute:
    ```bash
    python proxy_checker.py
    ```

5. **Escolha o tipo de proxy**:
    - O script solicitará que você escolha o tipo de proxy a ser verificado.
    - Ele testará cada proxy da lista fornecida, exibindo se está "ativa" ou "morta".


### Cores no Terminal 🎨
- **Verde**: Proxy ativa, funcionando com sucesso.
- **Vermelho**: Proxy inativa, não foi possível se conectar.
- **Ciano**: Mensagem de conclusão, com o caminho onde as proxies ativas foram salvas.

## Como Funciona 🧠

O script realiza as seguintes etapas:
1. **Carrega as proxies**: O arquivo `proxies.txt` é lido e as proxies são extraídas.
2. **Verificação**: Cada proxy é testada com a URL de teste (Google).
3. **Resultados**: Proxies ativas são salvas no arquivo `active_proxies.txt`, enquanto as inativas são descartadas.
4. **Execução paralela**: O script usa múltiplas threads para garantir uma verificação rápida.

## Personalizações ⚙️

- **Ajuste de tempo limite**: Você pode alterar o tempo limite de resposta de cada proxy modificando a variável `TIMEOUT` no script.
- **Alteração da URL de teste**: Se desejar testar com outros sites, edite a variável `TEST_URL` no código.

## Contribuições 💡

Se você quiser contribuir para o desenvolvimento do script, fique à vontade para fazer um **fork** e enviar um **pull request** com melhorias.

## Licença 📜

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido por kyev** 👨‍💻

