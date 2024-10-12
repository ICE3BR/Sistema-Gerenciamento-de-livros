# Adicione a classe Livro
class Livro():
    def __init__(self, nome, genero, autor_nome, ano, valor):
        self.nome = nome
        self.genero = genero
        self.autor_nome = autor_nome
        self.ano = ano
        self.valor = valor

# Lista de livros
_biblioteca_livros = []

# Adicionando livros à lista
_biblioteca_livros.append(Livro("O Senhor dos Anéis", "Fantasia", "J.R.R. Tolkien", 1954, 120.00))
_biblioteca_livros.append(Livro("1984", "Distopia", "George Orwell", 1949, 45.00))
_biblioteca_livros.append(Livro("O Pequeno Príncipe", "Infantil", "Antoine de Saint-Exupéry", 1943, 30.00))
_biblioteca_livros.append(Livro("Dom Casmurro", "Romance", "Machado de Assis", 1899, 25.00))

# Decorador para logar operações realizadas
def log_operacao(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executando: {func.__name__}")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper

# Modificação da função adicionar_livros com decorador
@log_operacao
def adicionar_livros(nome, genero, autor_nome, ano, valor):
    if not nome or not genero or not autor_nome or not ano or not valor:
        print(f"Dados inválidos, tente novamente")
        return False
    else:
        _biblioteca_livros.append(Livro(nome, genero, autor_nome, ano, valor))
        print(f"Livro {nome} foi adicionado com sucesso")
        return True

# Criando um gerador para listar os livros
@log_operacao
def listar_livros(biblioteca_livros):
    for livro in biblioteca_livros:
        yield f"""\
        
        Livro:	{livro.nome}
        Gênero:	{livro.genero}
        Autor:	{livro.autor_nome}
        Ano:	{livro.ano}
        Valor:	R$ {livro.valor}
        {"-" * 20}"""

def show_menu():
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
        show_menu()
        input_menu = input("Selecione uma opção: ")
        if input_menu == "1": # Adicionar livros
            print("Informe os dados necessários para adicionar o livro")
            nome = input("Nome: ")
            genero = input("Gênero: ")
            autor_nome = input("Autor: ")
            ano = input("Ano: ")
            valor = input("Valor: R$")
            adicionar_livros(nome, genero, autor_nome, ano, valor)

        elif input_menu == "2": # Listar livros
            for livro in listar_livros(_biblioteca_livros):
                print(livro)
        elif input_menu == "3": # Buscar livro por nome
            pass
        elif input_menu == "4": # Excluir livro
            pass
        elif input_menu == "0": # sair
            break
        else:
            print("\n@@@ Opção inválida, por favor selecione novamente. @@@")

menu_livraria()