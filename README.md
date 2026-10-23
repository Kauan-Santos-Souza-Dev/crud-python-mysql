# CRUD em Python com MySQL

Meu primeiro CRUD de back-end: um script em Python puro (sem framework) que conecta a um banco MySQL e executa as quatro operações básicas sobre uma tabela de vendas.

Observação: O Código foi escrito 100% por mim, ele está comentado pois eu estou anotando conceitos em cima do código para estudos pessoais.

## O que o projeto faz

O script `crudpython.py` realiza, em sequência, as quatro operações do CRUD na tabela `vendas`:

| Operação   | Comando SQL | O que o script faz                           |
| ---------- | ----------- | -------------------------------------------- |
| **C**reate | `INSERT`    | Cadastra uma venda (nome do produto e valor) |
| **R**ead   | `SELECT`    | Lista todas as vendas e imprime o resultado  |
| **U**pdate | `UPDATE`    | Altera o valor de uma venda pelo `idVendas`  |
| **D**elete | `DELETE`    | Remove uma venda pelo `idVendas`             |

Os valores usados (produto, valor e ids) estão como variáveis no próprio código. Edite-os para testar com os seus dados.

## Tecnologias

- Python 3
- MySQL
- [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/): conexão entre o Python e o MySQL
- [`python-dotenv`](https://pypi.org/project/python-dotenv/): leitura das credenciais a partir de um arquivo `.env`

## Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/Kauan-Santos-Souza-Dev/crud-python-mysql.git
cd crud-python-mysql
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

Windows (PowerShell):

```powershell
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

> No PowerShell, se aparecer o erro de que a execução de scripts está desabilitada, rode uma vez: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o banco e a tabela

No MySQL Workbench (ou outro cliente), execute:

```sql
CREATE DATABASE crud;
USE crud;

CREATE TABLE `vendas` (
    `idVendas` int NOT NULL AUTO_INCREMENT,
    `nome_produto` varchar(45) DEFAULT NULL,
    `valor` int DEFAULT NULL,
    PRIMARY KEY (`idVendas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 5. Configure as credenciais

Copie o arquivo de exemplo e preencha com os seus dados:

```bash
cp .env.example .env
```

No Windows (PowerShell): `Copy-Item .env.example .env`

Edite o `.env`:

```dotenv
DB_HOST=localhost
DB_USER=root
DB_PASSWORD='sua_senha_aqui'
DB_NAME=crud
```

> Se a senha tiver `#`, mantenha-a entre aspas simples. O `.env` está no `.gitignore` e **nunca** deve ser enviado ao GitHub.

### 6. Execute

```bash
python crudpython.py
```

## Estrutura do projeto

```
├── crudpython.py       # código do CRUD
├── requirements.txt    # dependências
├── .env.example        # modelo das variáveis de ambiente
└── .gitignore          # ignora o .env e o venv
```

## Boas práticas aplicadas

- **Consultas parametrizadas** (`%s`): evitam SQL injection.
- **Credenciais fora do código**: senha e dados do banco ficam no `.env`.
- **Ambiente virtual** (`venv`): dependências isoladas por projeto.
- **`.gitignore`**: impede que segredos e a pasta `venv` sejam versionados.

## Próximos passos

- [x] Separar cada operação em uma função
- [ ] Criar um menu interativo no terminal
- [ ] Tratar erros com `try/except` e validar os dados de entrada
- [ ] Evoluir para um framework como django
