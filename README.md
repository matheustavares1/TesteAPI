# TesteAPI

Este projeto consiste em uma interface web construída com Vue.js que interage com um servidor em Python. A aplicação permite realizar buscas textuais em uma lista de cadastros de operadoras e retorna os registros mais relevantes.
## Tecnologias Utilizadas

- **Vue.js** para o Front-End
- **Python** para o Back-End
- **Docker** para a criação de containers e execução do projeto
- **Docker Compose** para orquestrar os containers

## Estrutura do Projeto

- **BackEndAPI**: Contém a implementação da API Backend.
- **FrontEndVue**: Contém o código do Front-End em Vue.js.
- **node_modules**: Dependências do Front-End.
- **docker-compose.yml**: Arquivo de configuração para a execução do projeto via Docker.

## EndPoint
Busca dos registros
```
GET /buscar-operadoras - Realizar a busca com base na entrada do usuário.
```

## Como Executar :
1. Clone o reepositório
```
git clone https://github.com/matheustavares1/TesteAPI.git
```
2. Buildar o docker-compose
```
docker-compose up --build
```

