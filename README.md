# Projeto Ouvidoria 

Este é um sistema simples de ouvidoria desenvolvido em Python, com o objetivo de gerenciar manifestações de usuários, como reclamações, sugestões e feedbacks. O sistema utiliza um banco de dados MySQL para armazenar os dados e oferece funcionalidades básicas de CRUD (Create, Read, Update, Delete).

## Funcionalidades

1. **Listar Manifestações**: Exibe todas as manifestações cadastradas no sistema.
2. **Buscar por Tipo**: Permite filtrar manifestações por tipo (reclamação, sugestão ou feedback).
3. **Criar Nova Manifestação**: Adiciona uma nova manifestação ao banco de dados.
4. **Exibir Quantidade de Manifestações**: Mostra o número total de manifestações registradas.
5. **Buscar por Código**: Permite localizar uma manifestação específica usando seu código único.
6. **Excluir Manifestação**: Remove uma manifestação específica do sistema.
7. **Sair**: Encerra o sistema.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- `main.py`: Contém o menu principal e a lógica de interação com o usuário.
- `service.py`: Inclui as funções responsáveis pelas operações no banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **MySQL**: Banco de dados utilizado para armazenar as manifestações.
- **Biblioteca `operacoesbd`**: Para manipulação do banco de dados.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-ouvidoria.git
   cd projeto-ouvidoria
   ```

2. Configure o banco de dados MySQL:
   - Crie um banco de dados chamado `ouvidoriaBD`.
   - Configure o arquivo `operacoesbd` para se conectar ao banco de dados com suas credenciais.

3. Instale as dependências necessárias (se houver).

4. Execute o script principal:
   ```bash
   python main.py
   ```

5. Siga as instruções no menu para utilizar o sistema.

## Melhorias Futuras

- Interface gráfica para uma experiência de usuário aprimorada.
- Implementação de autenticação para proteger o acesso.
- Adicionar relatórios estatísticos sobre as manifestações.
- Integração com APIs para envio de notificações sobre alterações nas manifestações.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.

---------------------------------------------------------------------------------------------------------------------------------------

Projeto feito por: Erik Silva,Luis Felipe,Luis Claudio.
