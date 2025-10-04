# Projeto PIM - Cadastro de Pessoas em JSON

Este projeto foi desenvolvido como parte da disciplina de **Pensamento Lógico Computacional**. É um sistema de console em Python que permite ao usuário cadastrar informações de pessoas (nome, idade e e-mail) e salvá-las em um arquivo local no formato JSON.

## Tecnologias Utilizadas
* **Python 3**
* Módulo `json` (para manipulação de arquivos JSON)
* Módulo `os` (para verificar a existência de arquivos)

## Funcionalidades

O programa oferece um menu interativo com as seguintes opções:

* **Cadastrar Pessoa:**
    * Solicita ao usuário que insira nome, idade e e-mail.
    * Salva as informações em um dicionário e o adiciona a uma lista no arquivo `dados.json`.

* **Listar Cadastros:**
    * Recurso protegido por senha. A senha padrão é `ADS2025`.
    * Se a senha estiver correta, exibe todos os cadastros salvos no arquivo `dados.json` de forma organizada.
    * Caso a senha esteja incorreta, o acesso é negado.

* **Persistência de Dados:**
    * Os dados são carregados do arquivo `dados.json` ao iniciar e salvos no mesmo arquivo após cada novo cadastro, garantindo que as informações não se percam.

## Como Executar o Projeto

Para executar este projeto, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MatheusRenat0/ProjetoPIM.git](https://github.com/MatheusRenat0/ProjetoPIM.git)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd ProjetoPIM
    ```
3.  **Execute o arquivo principal:**
    ```bash
    python seu_arquivo.py
    ```

4.  Siga as instruções no menu do console para cadastrar ou listar pessoas.
