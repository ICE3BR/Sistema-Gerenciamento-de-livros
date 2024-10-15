import uuid

# Adicione a classe Livro
class Livro():
    # Construtor da classe Livro, que inicializa os atributos do livro
    def __init__(self, nome, genero, autor_nome, ano, valor):
        self.nome = nome
        self.genero = genero
        self.autor_nome = autor_nome
        self.ano = ano
        self.valor = valor
        self.ID = uuid.uuid4()  # Gera um ID único

# Lista de livros
_biblioteca_livros = []

# Adicionando livros à lista
# Inicializando a lista da biblioteca com alguns livros
_biblioteca_livros.append(Livro(f"O Senhor dos Anéis", "Fantasia", "J.R.R. Tolkien", 1954, 120.00))
_biblioteca_livros.append(Livro(f"1984", "Distopia", "George Orwell", 1949, 45.00))
_biblioteca_livros.append(Livro(f"O Pequeno Príncipe", "Infantil", "Antoine de Saint-Exupéry", 1943, 30.00))
_biblioteca_livros.append(Livro(f"Dom Casmurro", "Romance", "Machado de Assis", 1899, 25.00))
_biblioteca_livros.append(Livro(f"Vermelho, Branco e Sangue Azul", "Romance", "Casey McQuiston", 2019, 80.00))
_biblioteca_livros.append(Livro(f"Marketing do amor", "Romance", "Renato Ritto", 2022, 50.00))

# Decorador para logar operações realizadas
def log_operacao(func):
    # Função decoradora para registrar operações realizadas
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Executando: {func.__name__}")
        resultado = func(*args, **kwargs)  # Chama a função original
        return resultado
    return wrapper

# Modificação da função adicionar_livros com decorador
@log_operacao
def adicionar_livros(nome, genero, autor_nome, ano, valor):
    # Verifica se todos os dados são válidos antes de adicionar o livro
    if not nome or not genero or not autor_nome or not ano or not valor:
        print(f"Dados inválidos, tente novamente")
        return False
    else:
        # Adiciona o livro à lista de biblioteca
        _biblioteca_livros.append(Livro(nome, genero, autor_nome, ano, valor))
        print(f"Livro '{nome}' foi adicionado com sucesso")
        return True

# Criando um gerador para listar os livros
@log_operacao
def listar_livros(biblioteca_livros):
    # Função geradora que retorna cada livro da biblioteca
    for livro in biblioteca_livros:
        yield f"""\
        
        Livro:  {livro.nome}
        Gênero: {livro.genero}
        Autor:  {livro.autor_nome}
        Ano:    {livro.ano}
        Valor:  R$ {livro.valor}
        ID: {livro.ID}
        {"-" * 20}"""

# Função para excluir um livro da biblioteca
@log_operacao
def excluir_livro(livro_id):
    # Encontra o livro pelo ID e o remove da lista
    for i, livro in enumerate(_biblioteca_livros):
        if str(livro.ID) == str(livro_id):
            del _biblioteca_livros[i]
            print(f"Livro com ID '{livro_id}' foi excluído com sucesso.")
            return True
    print(f"Livro com ID '{livro_id}' não encontrado.")
    return False


# Função para exibir o menu
def show_menu():
    # Exibe as opções do menu para o usuário
    print(f"""
        Menu Livraria:
        1. Adicionar livros
        2. Listar livros
        3. Buscar livro por nome
        4. Excluir livro
        0. Sair
        """)

# Função menu para listar os livros
def menu_livraria():
    while True:
        show_menu()  # Exibe o menu
        input_menu = input("Selecione uma opção: ")
        if input_menu == "1":  # Adicionar livros
            print("Informe os dados necessários para adicionar o livro")
            nome = input("Nome: ")
            genero = input("Gênero: ")
            autor_nome = input("Autor: ")
            ano = input("Ano: ")
            valor = input("Valor: R$")
            adicionar_livros(nome, genero, autor_nome, ano, valor)

        elif input_menu == "2":  # Listar livros
            # Usa o gerador para listar todos os livros na biblioteca
            for livro in listar_livros(_biblioteca_livros):
                print(livro)
        elif input_menu == "3":  # Buscar livro por filtros
            # Função a ser implementada para buscar um livro específico por algum filtro: nome/genero/autor/ano/ID
            pass
        elif input_menu == "4":  # Excluir livro
            # Solicita o nome do livro a ser excluído
            nome = input("Digite o nome do livro que deseja excluir: ")
            excluir_livro(nome)
        elif input_menu == "0":  # Sair
            # Encerra o loop e sai do menu
            break
        else:
            # Mensagem de erro para entrada inválida
            print("\n@@@ Opção inválida, por favor selecione novamente. @@@")

# Inicia o menu da livraria
menu_livraria()

# OBS: Adicionar função que ao ADD um livro gera um ID unico para ele.
# Adicionar função para buscar um livro específico por algum filtro: nome/genero/autor/ano/ID
# Mudar menu de exclusão para pedir ID ao invés de nome