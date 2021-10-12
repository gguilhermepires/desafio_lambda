# desafio_lambda

# Descrição
Antes de começar....
Keep it simple, entendemos que você possui suas prioridades e nossa proposta é com esse desafio é ter uma idéia geral de como você faz seus códigos, toma suas decisões arquiteturais e o seu conhecimento geral sobre os assuntos abordados.
O desafio que propomos é provisionar uma infraestrutura na AWS, em que se tenha uma lambda que sejá capaz de registrar em um banco de dados relacional ou não relacional, dados sobre funcionários de uma empresa.

Observação
Não tem problema se você não conseguir finalizar tudo! Não deixe de enviar seu desafio por isso!
Requisitos
Utilizar Clean Architectute
Seu desafio precisa estar versionado no Github, em um repositório público.
Documentação é primordial e vamos nos guiar por ela ;)
Um funcionário deve possuir como atributos : Id , Idade , Nome e Cargo
Salvar as informações necessárias em um banco de dados relacional ou não relacional de sua escolha dentro de uma infraestrutura AWS
Será necessário que a Lambda consiga consultar, deletar e atualizar um funcionário e que ele esteja acessível via internet.
Os recuros podem ser provisionados por serveless framework ou terraform.
Realizar testes unitário com JEST.

# solução
Como o desafio é voltado para a infraestrutura na AWS, criei uma única função lambda para realizar o crud e não utilizei o padrão REST.

O ideal no meu ponto de vista seria uma lambda para cada operação e uma API gateway contendo um endpoint para cada operação utilizando o padrão REST.Cada lambda deveria ter a sua role.

Utilizei o serverless para fazer o deploy da lambda

Segue no projeto uma coleção do postman.

Abaixo está uns exemplos de consumo da API.

# Exemplos
### busca por id
curl --location --request POST 'https://bq7nzw4d26.execute-api.us-east-1.amazonaws.com/v1/usuarios' \
--header 'Content-Type: application/json' \
--data-raw '{
    "acao": "selecionaId",
    "id": 10
}'

### busca todos
curl --location --request POST 'https://bq7nzw4d26.execute-api.us-east-1.amazonaws.com/v1/usuarios' \
--header 'Content-Type: application/json' \
--data-raw '{
    "acao": "buscaTodos"
}'

### inserir
curl --location --request POST 'https://bq7nzw4d26.execute-api.us-east-1.amazonaws.com/v1/usuarios' \
--header 'Content-Type: application/json' \
--data-raw '{
  "acao": "inserir",
  "nome": "teste",
  "idade": 10,
  "cargo": "teste"
}'

### remover
curl --location --request POST 'https://bq7nzw4d26.execute-api.us-east-1.amazonaws.com/v1/usuarios' \
--header 'Content-Type: application/json' \
--data-raw '{
  "acao": "excluirId",
  "id": 11
}'
