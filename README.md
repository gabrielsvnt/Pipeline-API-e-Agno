# Pipeline-API-e-Agno
## Visão Geral

Este projeto consiste em uma API de pipeline para extração, processamento e visualização de dados do Bitcoin, utilizando agentes inteligentes para automação de tarefas.

## Estrutura do Projeto

- `pipeline/bitcoin_etl.py`: Responsável pela extração, transformação e carregamento (ETL) dos dados do Bitcoin. Realiza a coleta de dados de fontes externas, processa e armazena para uso posterior.
- `dashboard/bitcoin_dashboard.py`: Implementa um dashboard interativo para visualização dos dados processados do Bitcoin, permitindo análise gráfica e acompanhamento em tempo real.
- `agents/main.py`: Contém a lógica dos agentes inteligentes que automatizam tarefas dentro do pipeline, como monitoramento de dados, alertas e execução de rotinas programadas.

## Como Executar

1. Clone o repositório:
    ```bash
    git clone git@github.com:gabrielsvnt/Pipeline-API-e-Agno.git
    cd Pipeline-API-e-Agno
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o pipeline ETL:
    ```bash
    python pipeline/bitcoin_etl.py
    ```

4. Inicie o dashboard:
    ```bash
    python dashboard/bitcoin_dashboard.py
    ```

5. Execute os agentes:
    ```bash
    python agents/main.py
    ```
