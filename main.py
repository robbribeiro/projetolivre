from controllers.biblioteca import BibliotecaDeFilmes
from models.filme import Filme

def main():
    biblioteca = BibliotecaDeFilmes()
    
    while True:
        print("\nOpções:")
        print("1. Adicionar Filme")
        print("2. Listar Filmes")
        print("3. Excluir Filme")
        print("4. Atualizar Filme")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            titulo = input("Título: ")
            diretor = input("Diretor: ")
            genero = input("Gênero: ")
            ano = input("Ano: ")
            filme = Filme(titulo, diretor, genero, ano)
            biblioteca.adicionar_filme(filme)
        elif escolha == "2":
            biblioteca.listar_filmes()
        elif escolha == "3":
            indice = int(input("Número do filme a excluir: "))
            biblioteca.excluir_filme(indice)
        elif escolha == "4":
            indice = int(input("Número do filme a atualizar: "))
            titulo = input("Novo título (ou Enter para manter): ")
            diretor = input("Novo diretor (ou Enter para manter): ")
            genero = input("Novo gênero (ou Enter para manter): ")
            ano = input("Novo ano (ou Enter para manter): ")
            detalhes = {k: v for k, v in [("titulo", titulo), ("diretor", diretor), ("genero", genero), ("ano", ano)] if v}
            biblioteca.atualizar_filme(indice, **detalhes)
        elif escolha == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()