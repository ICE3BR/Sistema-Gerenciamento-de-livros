
# Adicione a classe Livro
class livro():
    def __init__(self, nome, genero, autor_nome, ano, valor):
        self.nome = nome
        self.genero = genero
        self.autor_nome = autor_nome
        self.ano = ano
        self.valor = valor

# Lista de livros
_biblioteca_livros = []

# Adicionando livros à lista
_biblioteca_livros.append(livro("O Senhor dos Anéis", "Fantasia", "J.R.R. Tolkien", 1954, 120.00))
_biblioteca_livros.append(livro("1984", "Distopia", "George Orwell", 1949, 45.00))
_biblioteca_livros.append(livro("O Pequeno Príncipe", "Infantil", "Antoine de Saint-Exupéry", 1943, 30.00))
_biblioteca_livros.append(livro("Dom Casmurro", "Romance", "Machado de Assis", 1899, 25.00))

def adicionar_livros(nome, genero, autor_nome, ano, valor):
    if adicionar_livros is None:
        print(f"Dados inválidos, tente novamente")
        return False
    else:
        _biblioteca_livros.append(livro(nome, genero, autor_nome, ano, valor))
        print(f"Livro {nome} foi Adicionado com sucesso")
        

class listar_livros():
    def __init__(self, biblioteca_livros):
        self.livros = biblioteca_livros
        self._index = 0
    
    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            livro = self.livros[self._index]
            return f"""\
            
            Livro:\t{livro.nome}
            genero:\t{livro.genero}
            Autor:\t{livro.autor_nome}
            Ano:\t{livro.ano}
            Valor:\tR$ {livro.valor}
            {"-" * 20}"""
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

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
            print("Informe os dados nescessários para adicionar o livro")
            nome = input("nome: ")
            genero = input("genero: ")
            autor_nome = input("autor_nome: ")
            ano = input("ano: ")
            valor = input("valor: R$")
            adicionar_livros(nome, genero, autor_nome, ano, valor)

        elif input_menu == "2": # Listar livro
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