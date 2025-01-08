class Filme:
    def __init__(self, titulo, diretor, genero, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero
        self.ano = ano

    def atualizar_detalhes(self, titulo=None, diretor=None, genero=None, ano=None):
        if titulo:
            self.titulo = titulo
        if diretor:
            self.diretor = diretor
        if genero:
            self.genero = genero
        if ano:
            self.ano = ano

    def __str__(self):
        return f"Título: {self.titulo}, Diretor: {self.diretor}, Gênero: {self.genero}, Ano: {self.ano}"

    def __repr__(self):
        return f"Filme({repr(self.titulo)}, {repr(self.diretor)}, {repr(self.genero)}, {repr(self.ano)})"