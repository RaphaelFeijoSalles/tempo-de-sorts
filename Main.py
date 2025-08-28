from random import randint
from time import perf_counter
import Insertion
import Selection
import Bubble


def gera_lista(tamanho_da_lista: int):
    return [randint(1, tamanho_da_lista) for _ in range(tamanho_da_lista)]


def imprimir_ordenacoes(lista, ordenada, limite=2000, elementos_por_linha=10, blocos=20):
    def formatar(l):
        if len(l) <= limite:
            linhas = []
            for i in range(0, len(l), elementos_por_linha):
                bloco = l[i:i + elementos_por_linha]
                linhas.append(", ".join(map(str, bloco)))
            return "[\n" + "\n".join(linhas) + "\n]"
        else:
            print()
            print(f"(Aviso: lista limitada a {blocos*2} elementos exibidos + reticências para não imprimir {len(l)} elementos)")

            primeiros = l[:blocos]
            ultimos = l[-blocos:]

            linhas = []
            for i in range(0, len(primeiros), elementos_por_linha):
                linhas.append(", ".join(map(str, primeiros[i:i + elementos_por_linha])))

            linhas.append("...")

            for i in range(0, len(ultimos), elementos_por_linha):
                linhas.append(", ".join(map(str, ultimos[i:i + elementos_por_linha])))

            return "[\n" + "\n".join(linhas) + "\n]"

    print("\nLista antes da ordenação:\n" + formatar(lista))
    print("\nLista depois da ordenação:\n" + formatar(ordenada))





def tempo(lista, metodo, nome_metodo):
    antes = perf_counter()
    ordenada = metodo(lista[:])
    depois = perf_counter()
    print(f"Seu programa {nome_metodo} demorou {depois - antes:.6f} segundos.")
    return ordenada


def pedir_tamanho():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da lista (mínimo 100): "))
            if tamanho < 100:
                print("ERRO: Digite um número maior ou igual a 100!\n")
            else:
                return tamanho
        except ValueError:
            print("\nERRO: Insira um número inteiro!\n")


def perguntar(mensagem, opcoes=("s", "n")):
    while True:
        resposta = input(mensagem).lower()
        if resposta in opcoes:
            return resposta
        print("Opção inválida, tente novamente.")


def escolher_metodo():
    metodos = []
    menu = "\nInsira os métodos a serem comparados:\n\n[i] Insertion\n[b] Bubble\n[s] Selection\n[(enter)] Confirmar\n"
    while True and len(metodos) < 3:
        print(menu)
        print(f"{len(metodos) + 1}º opção - ", end="")
        metodo = input().lower()
        if metodo == "":
            if len(metodos) < 2:
                print("\nERRO: Insira pelo menos DOIS métodos!\n")
            else:
                print("Sucesso!\n")
                break
        elif metodo not in ("i", "b", "s"):
            print("\nERRO: Insira uma das opções fornecidas!\n")
        else:
            if metodo not in metodos:
                metodos.append(metodo)
                if metodo == "i":
                    menu = menu.replace("\n[i] Insertion", "")
                if metodo == "b":
                    menu = menu.replace("\n[b] Bubble", "")
                if metodo == "s":
                    menu = menu.replace("\n[s] Selection", "")
            else:
                print("Esse método já foi escolhido!")
    return metodos


def insercao(lista):
    return Insertion.insertion_sort(lista)


def selecao_direta(lista):
    return Selection.selecao_direta(lista)


def bolha(lista):
    return Bubble.bubble_sort(lista)


def main():

    while True:
        metodos = escolher_metodo()
        tamanho_da_lista = pedir_tamanho()
        lista = gera_lista(tamanho_da_lista)
        print("\nComparando em TEMPO REAL os ordenadores (pode demorar dependendo do tamanho da lista)...")
        print("-----------------------------------------------------------------------------------------------------")
        metodos_disponiveis = {
            "i": ("Insertion", insercao),
            "b": ("Bubble", bolha),
            "s": ("Selection", selecao_direta),
        }
        ordenada = None
        for m in metodos:
            nome, funcao = metodos_disponiveis[m]
            ordenada = tempo(lista, funcao, nome)
        print("-----------------------------------------------------------------------------------------------------")
        if perguntar("Deseja ver o antes e depois da lista gerada? (s/n): ") == "s":
            imprimir_ordenacoes(lista, ordenada)
        else:
            print("Você escolheu ocultar a lista gerada!")

        if perguntar("\nDeseja comparar outro método de ordenação/outro tamanho de lista? (s/n): ") == "n":
            print("\nPrograma finalizado com sucesso!")
            return


if __name__ == "__main__":
    main()
