from controllers.biblioteca import BibliotecaDeMidias
from models.filme import Filme
from models.serie import Serie

def main():
    biblioteca = BibliotecaDeMidias()  # Carrega as mídias do arquivo JSON
    
    while True:
        print("\nOpções:")
        print("1. Adicionar Filme")
        print("2. Adicionar Série")
        print("3. Listar Mídias")
        print("4. Excluir Mídia")
        print("5. Atualizar Mídia")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            titulo = input("Título: ")
            diretor = input("Diretor: ")
            genero = input("Gênero: ")
            ano = input("Ano: ")
            filme = Filme(titulo, diretor, genero, ano)
            biblioteca.adicionar_midia(filme)
        elif escolha == "2":
            titulo = input("Título: ")
            diretor = input("Diretor: ")
            genero = input("Gênero: ")
            ano = input("Ano: ")
            temporadas = input("Temporadas: ")
            serie = Serie(titulo, diretor, genero, ano, temporadas)
            biblioteca.adicionar_midia(serie)
        elif escolha == "3":
            biblioteca.listar_midias()
        elif escolha == "4":
            indice = int(input("Número da mídia a excluir: "))
            biblioteca.excluir_midia(indice)
        elif escolha == "5":
            indice = int(input("Número da mídia a atualizar: "))
            tipo = input("É um filme ou uma série?").lower()
            if tipo == "filme":
                titulo = input("Novo título (ou Enter para manter): ")
                diretor = input("Novo diretor (ou Enter para manter): ")
                genero = input("Novo gênero (ou Enter para manter): ")
                ano = input("Novo ano (ou Enter para manter): ")
                detalhes = {k: v for k, v in [("titulo", titulo), ("diretor", diretor), ("genero", genero), ("ano", ano)] if v}
                biblioteca.atualizar_midia(indice, **detalhes)
            elif tipo == "serie":
                titulo = input("Novo título (ou Enter para manter): ")
                diretor = input("Novo diretor (ou Enter para manter): ")
                genero = input("Novo gênero (ou Enter para manter): ")
                ano = input("Novo ano (ou Enter para manter): ")
                temporadas = input("Novas temporadas (ou Enter para manter): ")
                detalhes = {k: v for k, v in [("titulo", titulo), ("diretor", diretor), ("genero", genero), ("ano", ano), ("temporadas", temporadas)] if v}
                biblioteca.atualizar_midia(indice, **detalhes)
        elif escolha == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
