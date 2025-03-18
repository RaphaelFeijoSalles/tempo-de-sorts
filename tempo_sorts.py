from random import randint
from time import time
import insertion
import SelecaoDireta
import bubble
tamanho_da_lista = eval(input("Digíte o tamanho da lista a ser comparada: "))
class Ordenador: 
    
    
    def __init__(self):
        self.lista = self.geraLista()
            

    
    def geraLista (self):
        lista = [randint(1, tamanho_da_lista) for _ in range(tamanho_da_lista)]
        return lista
    
    
    def exibeLista(self):
        print(self.lista)
    
    
    def insert(self):
        insercao = insertion.insertion_sort(self.lista)
        return insercao
    
    def selecao(self):
        selec = SelecaoDireta.selecao_direta(self.lista)
        return selec
    
    def bolha(self):
        bol = bubble.bubble_sort(self.lista)
        return bol


def ImprimirOdenacoes(metodo):
    ordenador = Ordenador()  
    
    metodo_escolhido = getattr(ordenador, metodo)
    
    print("Lista antes da ordenação:")
    ordenador.exibeLista()  
    
    metodo_escolhido()
    
    print("\nLista depois da ordenação:")
    ordenador.exibeLista()
    




def tempo(metodo):
    ordenador = Ordenador()  
    
    metodo_escolhido = getattr(ordenador, metodo)
    
    antes_selecao = time()
       
    metodo_escolhido()
        
    depois_selecao = time()
    
    print("Seu programa", metodo, "demorou", depois_selecao - antes_selecao, "para ser executado.")    


def escolher_metodo():
    print ("Insira os métodos a serem comparados(insertion, bubble, selection):")
    metodos = []
    aux = 0
    while aux != (""):
        aux = input("(Aperte enter para sair):")
        metodos.append(aux)
    
    imprimir = []
    imprimir.append(input("Deseja o antes e depois de organizado?\n(s p/ sim)\n(n p/ não)\n"))
    
    
    
    for metodo in metodos:
        if str(metodo) == "insertion":
            tempo(("insert"))
            if imprimir[0] == "s":
                ImprimirOdenacoes("insert")
            else:
                print("Listas ocultas")
        if str(metodo) == "selection":
            tempo("selecao")
            if imprimir[0] == "s":
                ImprimirOdenacoes("selecao")
            else:
                print("Listas ocultas")
        if str(metodo) == "bubble":
            tempo("bolha")
            if imprimir[0] == "s":    
                ImprimirOdenacoes("bolha")
            else:
                print("Listas ocultas")


escolher_metodo()



