from time import sleep
from utils import *

def buy_list():
    while True:
        try:
            title("Lista de compras")

            amount = get_number("Digite quantos itens deseja adicionar a lista: ")

            if amount <= 0:
                raise ValueError
            
            items = []

            for x in range(1, amount + 1):
                clear()

                try:
                    product = input(f"Digite o {x}º item que deseja comprar: ").strip()
                    # product_amount = get_number("Digite a quantidade que deseja comprar" \
                    # "[Deixe em branco para adicionar 1]: ", 1)

                    if (product == ""):
                        raise TypeError
                    
                    items.append(product)
                    
                except TypeError:
                    title("O item nao pode estar vazio.")
                    sleep(1)
     
            sorted_items = sorted(items)

            title("Itens na lista")
            print(f"Todos os itens adicionados na lista: {get_text_list(items)}")
            print()
            print(f"Sua lista tem: {amount} {'item' if amount == 1 else 'itens'}")
            print()
            print(f"Itens em ordem afabética: {get_text_list(sorted_items)}")

            print()
            input("Pressione enter para continuar.")

            title("Deseja validar outro intervalo?")
            print("1 - Sim")
            print("2 - Nao")
            print()
            repeat = get_number("Digite uma opcao: ")

            if repeat == 2:
                break;

            
        except ValueError:
            title("O valor não pode ser inferior ou igual a zero")
            sleep(1)