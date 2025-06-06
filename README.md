# Sistema de Ouvidoria

Este projeto é um sistema simples em Python para o gerenciamento de manifestações como elogios, reclamações e sugestões. Ele realiza operações de cadastro, listagem, exclusão, contagem e pesquisa de manifestações armazenadas em um banco de dados MySQL.

## 📂 Estrutura dos Arquivos

- **menu.py**: Interface principal em linha de comando para o usuário interagir com o sistema.
- **Metodos.py**: Contém as funções principais de manipulação de manifestações (adicionar, listar, remover, pesquisar, contar).
- **operacoesbd.py**: Define funções para interagir com o banco de dados MySQL (inserção, listagem, exclusão, etc.).
- **Adicionar.py**: Script separado para adicionar manifestações diretamente.
- **Listar.py**: Lista todas as manifestações no banco de dados.
- **Listar-por-tipo.py**: Lista manifestações com base no tipo selecionado.
- **Pesquisar.py**: Permite pesquisar uma manifestação por código.
- **Remover.py**: Remove uma manifestação informando seu código.
- **Quantidade.py**: Mostra a quantidade total de manifestações cadastradas.

## 🧰 Requisitos

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python`
