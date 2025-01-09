from models.midia import Midia

class Serie(Midia):
    def __init__(self, titulo, diretor, genero, ano, temporadas):
        super().__init__(titulo, diretor, genero, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{super().__str__()}, Temporadas: {self.temporadas}"

    def atualizar_detalhes(self, titulo=None, diretor=None, genero=None, ano=None, temporadas=None):
        super().atualizar_detalhes(titulo, diretor, genero, ano)
        if temporadas:
            self.temporadas = temporadas
