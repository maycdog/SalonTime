# SalonTime

O **SalonTime** é um sistema de agendamento de salões de beleza desenvolvido com Django. Ele permite que os clientes escolham serviços como manicure e pedicure, e agendem horários através de uma interface web simples. O sistema também permite que os administradores visualizem e gerenciem os agendamentos realizados.

## Índice

1. [Visão Geral](#visão-geral)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalação)
4. [Tutorial de Uso](#tutorial-de-uso)
5. [Histórico de Versões](#histórico-de-versões)
6. [Licença](#licença)
7. [Contribuição](#contribuição)
8. [Agradecimentos](#agradecimentos)

## Visão Geral

O **SalonTime** é um sistema online que permite que clientes agendem serviços como **Manicure** e **Pedicure**, escolha de horário e forma de pagamento. Ele inclui funcionalidades para:

- **Adicionar Cliente**: Cadastrar novos clientes com nome, serviços, telefone, e-mail e horário do agendamento.
- **Listar Clientes**: Exibir a lista de clientes agendados e os serviços escolhidos.
- **Atualizar Cliente**: Permite a edição de dados de clientes já cadastrados.
- **Deletar Cliente**: Excluir clientes do sistema.

O sistema é desenvolvido em Django, com front-end simples usando HTML e CSS, e backend com banco de dados MySQL.

## Tecnologias Utilizadas

- **Django**: Framework Python utilizado para o backend.
- **Python 3.12**: Linguagem de programação usada para o desenvolvimento.
- **MySQL**: Banco de dados para armazenar as informações de clientes e agendamentos.
- **HTML/CSS**: Para a construção do front-end.
- **Django Forms**: Para a criação e validação de formulários.
- **Django Models**: Utilizado para o relacionamento de clientes com os serviços agendados (Many-to-Many).

## Instalação

Siga os passos abaixo para configurar o projeto localmente.

### 1. Clonando o Repositório

git clone https://github.com/seu-usuario/salontime.git
cd salontime

### 2. Instalando Dependências

Use o pip para instalar as dependências do projeto:

pip install -r requirements.txt

### 3. Configuração do Banco de Dados

Crie um banco de dados MySQL e configure as credenciais no arquivo .env:

DB_NAME=salontime_db
DB_USER=root
DB_PASSWORD=sua_senha
DB_HOST=127.0.0.1
DB_PORT=3306

### 4. Rodando as Migrações

Execute as migrações para criar as tabelas no banco de dados:

python manage.py migrate

### 5. Criando Superusuário

Crie um superusuário para acessar o painel de administração:

python manage.py createsuperuser

### 6. Iniciando o Servidor

Para rodar o servidor de desenvolvimento, use:

python manage.py runserver

Agora, você pode acessar o sistema em http://127.0.0.1:8000/.
### Tutorial de Uso

    Adicionando um Novo Cliente:

        Acesse a página de agendamento.

        Preencha os campos do formulário com o nome, telefone, e-mail, e horário desejado.

        Selecione os serviços que o cliente deseja agendar.

        Clique em "Salvar" para adicionar o cliente ao banco de dados.

    Visualizando a Lista de Clientes:

        Vá até a página de listagem de clientes.

        Todos os clientes agendados serão exibidos, com detalhes como nome, serviços escolhidos, preço e horário.

    Atualizando um Cliente:

        Na página de listagem, clique no link de "Editar" ao lado do cliente que deseja atualizar.

        Edite os dados e clique em "Salvar" para confirmar as mudanças.

    Deletando um Cliente:

        Na página de listagem, clique no link "Deletar" ao lado do cliente para excluí-lo do sistema.

### Histórico de Versões

    Versão 1.0:

        Funcionalidades iniciais de agendamento implementadas.

        Interface para adicionar e listar clientes.

        Relacionamento entre clientes e serviços.

### Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
Contribuição

    Faça um fork do projeto.

    Crie uma branch para sua funcionalidade (git checkout -b feature/MinhaFeature).

    Faça o commit das suas alterações (git commit -am 'Adicionar nova feature').

    Faça o push para o repositório remoto (git push origin feature/MinhaFeature).

    Abra um Pull Request para revisão.

### Agradecimentos

Agradeço aos tutoriais online e o conhecimento de aprendizagem.
