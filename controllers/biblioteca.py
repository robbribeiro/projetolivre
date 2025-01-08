import json
from models.filme import Filme

class BibliotecaDeFilmes:
    def __init__(self, arquivo_json='filmes.json'):
        self.arquivo_json = arquivo_json
        self.filmes = self.carregar_filmes()

    def carregar_filmes(self):
        try:
            with open(self.arquivo_json, 'r', encoding='utf-8') as f:
                filmes_data = json.load(f)
                return [Filme(**filme) for filme in filmes_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []

    def salvar_filmes(self):
        filmes_data = [filme.__dict__ for filme in self.filmes]
        with open(self.arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(filmes_data, f, indent=4)

    def adicionar_filme(self, filme):
        self.filmes.append(filme)
        self.salvar_filmes()
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
            self.salvar_filmes()
            print(f"Filme '{filme_removido.titulo}' removido com sucesso!")
        except IndexError:
            print("Índice inválido.")

    def atualizar_filme(self, indice, **detalhes):
        try:
            filme = self.filmes[indice - 1]
            filme.atualizar_detalhes(**detalhes)
            self.salvar_filmes()
            print("Detalhes do filme atualizados com sucesso!")
        except IndexError:
            print("Índice inválido.")