```mermaid
graph TD
    A[Início] --> B[Exibir Menu]
    
    B --> C1[Opção 1: Adicionar Livro]
    B --> C2[Opção 2: Listar Livros]
    B --> C3[Opção 3: Buscar Livro por Filtro]
    B --> C4[Opção 4: Excluir Livro]
    B --> C5[Opção 0: Sair]

    %% Adicionar Livro
    C1 --> D1[Solicitar dados do livro]
    D1 --> E1[Validar dados]
    E1 --> F1{Dados válidos?}
    F1 -- Sim --> G1[Adicionar livro à lista]
    F1 -- Não --> H1[Exibir erro e voltar ao menu]
    G1 --> B

    %% Listar Livros
    C2 --> D2[Iterar pelos livros na biblioteca]
    D2 --> E2[Exibir detalhes de cada livro]
    E2 --> B

    %% Buscar Livro por Filtro
    C3 --> D3[Solicitar tipo de filtro e valor]
    D3 --> E3[Buscar livro por filtro]
    E3 --> F3{Livro encontrado?}
    F3 -- Sim --> G3[Exibir detalhes do livro]
    F3 -- Não --> H3[Exibir mensagem de erro]
    G3 --> B
    H3 --> B

    %% Excluir Livro
    C4 --> D4[Solicitar ID do livro]
    D4 --> E4[Buscar livro pelo ID]
    E4 --> F4{Livro encontrado?}
    F4 -- Sim --> G4[Excluir livro da lista]
    F4 -- Não --> H4[Exibir mensagem de erro]
    G4 --> B
    H4 --> B

    %% Sair
    C5 --> I[Encerrar programa]
    ```
