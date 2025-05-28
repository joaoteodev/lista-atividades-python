from utils import *
from time import sleep


def prime_numbers():
    while True:
        try:
            title("Numeros primos")
            start = get_number("Digite o inicio do intervalo: ")
            end = get_number("Digite o final do intervalo: ")
            print()

            if start > end:
                raise ValueError

            primes = []

            for x in range(start, end + 1):
                count = 0

                for num in range(1, x + 1):
                    if x % num == 0:
                        count += 1

                if count == 2:
                    primes.append(x)

            title(f"Numeros primos entre {start} e {end}")

            print(f"Os numeros primos sao: {get_text_list(primes)}")
            print()
            print(f"{'Foi encontrado' if len(primes) == 1 else 'Foram encontrados'} {len(primes)} {'número' if len(primes) == 1 else 'números'}")
            print()

            input("Pressione enter para continuar.")

            title("Deseja validar outro intervalo?")
            print("1 - Sim")
            print("2 - Nao")
            print()
            repeat = get_number("Digite uma opcao: ")

            if repeat == 2:
                break

        except ValueError:
            title("O final nao pode ser menor do que o inicio")
            sleep(1)
            clear()
