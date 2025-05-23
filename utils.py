from time import sleep
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def dash(n = 30, simbol = "="):
    print(simbol * n)

def title(msg = "Mensagem padrao"):
    clear()
    size = len(msg) + 10
    dash(size)
    print(msg.center(size))
    dash(size)
    print()

def get_number(text, default = ""):
    while True:
        input_number = input(text).replace(",", ".")
        try:
            if "." in input_number:
                return float(input_number)
            else:
                return int(input_number)
            
            # if f"{default}".isdigit():
            #     return default

        except ValueError:
            title("O valor digitado não é um número válido. Tente novamente.")
            sleep(1)
            clear()

def get_text_list(list_items):
    size = len(list_items)
    text = ""

    for x in range(size):
        if x == size - 2:
            text += f"{list_items[x]} e "
            continue

        if x == size - 1:
            text += f"{list_items[x]}"
            continue

        text += f"{list_items[x]}, "

    return text