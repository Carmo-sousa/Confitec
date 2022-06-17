# Confitec

Consome a API do [Genius](https://genius.com) para buscar as dez melhores musicas de um artista.

## Tecnologias utilizadas

- [Python](http://www.python.org) linguagem utilizadas no desenvolvimento do projeto.
- [Redis](https://redis.io/) para servir como cache.
- [DynamoDB](https://dynamodb.amazonaws.com/) para armazenar os dados do artista.

## Bibliotecas/Frameworks utilizados no projeto

- [Flask](https://flask.palletsprojects.com/) para a construção da API
- [Dynaconf](https://dynaconf.com/) para gerenciar as configurações do projeto
- [Boto3](https://aws.amazon.com/pt/sdk-for-python/) sdk para integrar com o DynamoDB
- [redis-py](https://redis-py.readthedocs.io/en/stable/) sdk para integrar com o Redis

## Requisitos do projeto

Ter instalado o [Docker](https://www.docker.com/) e o [Docker Compose](https://docs.docker.com/compose/install/)

## Como executar o projeto (linux)

Antes de executar o projeto, é necessário trocar as credenciais de usuário do AWS e Genius.

    git clone https://github.com/Carmo-sousa/Confitec.git
    cd Confitec
    cp .sample.env .env

No arquivo .env, é necessário definir as seguintes variáveis: trocando pelas credenciais do seu AWS e Genius.
As credenciais do aws são obtidas no site do [AWS](https://docs.aws.amazon.com/general/latest/gr/root-vs-iam.html). E as credenciais do Genius são obtidas no site do [Genius](https://genius.com/api-clients).

```env
FLASK_ENV=development
FLASK_APP=confitec/app.py
GENIUS_API_KEY=<your_genius_api_key>
ACCESS_KEY=<your_access_key>
SECRET_KEY=<your_secret_key>
```

    docker compose up --build -d

Agora é possível acessar a API do projeto no endereço: <http://localhost:5000/artists/>
Buscando por um artista: <http://localhost:5000/artists/?q=Lukas%20Grahan>
É possível acessar os dados em cache com o parâmetro `cache=true`
