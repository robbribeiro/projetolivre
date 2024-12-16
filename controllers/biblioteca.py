class BibliotecaDeFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)
        print("Filme adicionado com sucesso!")

    def listar_filmes(self):
        if not self.filmes:
            print("A biblioteca está vazia.")
        else:
            for i, filme in enumerate(self.filmes, start=1):
                print(f"{i}. {filme}")

    def excluir_filme(self, indice):
        try:
            filme_removido = self.filmes.pop(indice - 1)
            print(f"Filme '{filme_removido.titulo}' removido com sucesso!")
        except IndexError:
            print("Índice inválido.")

    def atualizar_filme(self, indice, **detalhes):
        try:
            filme = self.filmes[indice - 1]
            filme.atualizar_detalhes(**detalhes)
            print("Detalhes do filme atualizados com sucesso!")
        except IndexError:
            print("Índice inválido.")
