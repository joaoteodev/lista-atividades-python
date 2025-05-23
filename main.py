from time import sleep
from utils import *
from prime_numbers import *
from buy_list import *
from atm import *

def menu():
    while(True):
        title("Menu de selecao")
        print("1 - Numeros primos entre um intervalo")
        print("2 - Lista de compras")
        print("3 - Caixa eletronico")
        print("4 - Cadastro de pessoas")
        print("X - Sair")
        print()
        option = input("Digite a opcao selecionada: ").strip().upper()

        validOptions = "1234X"

        if option in validOptions:
            execute(option)

        if option not in validOptions:
            title("Opcao invalida. Tente novamente.")
            sleep(1)

def execute(option):
    if option == "1": prime_numbers()
    if option == "2": buy_list()
    if option == "3": atm()
    if option == "4": prime_numbers()
    if option == "x":
        title("Encerrando programa.")
        sleep(2)
        exit(0)

menu()