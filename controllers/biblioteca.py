import json
from models.midia import Midia
from models.filme import Filme
from models.serie import Serie

class BibliotecaDeMidias:
    def __init__(self, arquivo_json='midias.json'):
        self.arquivo_json = arquivo_json
        self.midias = self.carregar_midias()

    def carregar_midias(self):
        try:
            with open(self.arquivo_json, 'r', encoding='utf-8') as f:
                midias_data = json.load(f)
                midias = []
                for midia in midias_data:
                    tipo = midia.pop("tipo", None)  # Remove o campo "tipo"
                    if tipo == "filme":
                        midias.append(Filme(**midia))
                    elif tipo == "serie":
                        midias.append(Serie(**midia))
            return midias
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []

    def salvar_midias(self):
        midias_data = [
            {**midia.__dict__, "tipo": "filme" if isinstance(midia, Filme) else "serie"} 
            for midia in self.midias
        ]
        with open(self.arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(midias_data, f, indent=4)

    def adicionar_midia(self, midia):
        self.midias.append(midia)
        self.salvar_midias()
        print("Mídia adicionada com sucesso!")

    def listar_midias(self):
        if not self.midias:
            print("A biblioteca está vazia.")
        else:
            for i, midia in enumerate(self.midias, start=1):
                print(f"{i}. {midia}")

    def excluir_midia(self, indice):
        try:
            midia_removida = self.midias.pop(indice - 1)
            self.salvar_midias()
            print(f"Mídia '{midia_removida.titulo}' removida com sucesso!")
        except IndexError:
            print("Índice inválido.")

    def atualizar_midia(self, indice, **detalhes):
        try:
            midia = self.midias[indice - 1]
            midia.atualizar_detalhes(**detalhes)
            self.salvar_midias()
            print("Detalhes da mídia atualizados com sucesso!")
        except IndexError:
            print("Índice inválido.")
