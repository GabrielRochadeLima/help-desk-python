# Help Desk em Python

Sistema de linha de comando para gerenciamento de chamados de suporte técnico.

## Sobre o projeto

O projeto foi desenvolvido para praticar lógica de programação, funções, autenticação simples e persistência de dados em arquivos de texto com Python.

## Funcionalidades

- Cadastro de usuários, com validação de campos obrigatórios e prevenção de e-mails duplicados.
- Login de usuários cadastrados.
- Abertura de chamados com número sequencial, título, descrição, prioridade, setor responsável, impacto e data-limite.
- Consulta dos chamados abertos pelo usuário autenticado.
- Área administrativa para consultar todos os chamados registrados.
- Consulta dos usuários cadastrados pela área administrativa, sem exibir senhas.
- Armazenamento dos dados em arquivos locais (`usuarios.txt` e `chamados.txt`).

## Como executar

Com o Python instalado, execute no diretório do projeto:

```bash
python help-desk.py
```

No menu inicial, escolha uma das opções disponíveis:

1. Fazer login;
2. Cadastrar usuário;
3. Acessar a área administrativa;
4. Sair.

Após o login, é possível abrir um chamado ou consultar os chamados associados ao usuário.

## Arquivos de dados

- `usuarios.txt`: armazena nome, e-mail e senha dos usuários cadastrados.
- `chamados.txt`: armazena os chamados abertos pelo sistema.

Os arquivos são criados ou atualizados automaticamente conforme o uso da aplicação.

## Tecnologias

- Python
- Git
- GitHub
