from utils import *
from time import sleep

def atm():
    saldo = 0
    notas = [100, 50, 20, 10, 7, 5, 2, 1]

    while True:
        notas_sacar = []
        try:
            title("Caixa eletronico")


            print(f"Seu saldo e: R$ {saldo}")
            print()

            while True:
                print("1 - Depositar dinheiro")
                print("2 - sacar dinheiro")
                print()
                option = input("Selecione uma opcao: ")

                if option not in "12":
                    raise TypeError
                
                if option == "1":
                    title("Depositar")
                    amount = get_number("Digite o valor que deseja depositar: ")
                    if amount < 0:
                        raise TypeError
                    saldo += amount
                    break

                if option == "2":
                    title("Sacar")
                    print(f"Saldo disponivel: R$ {saldo}")

                    sacar = get_number("Digite o valor que deseja sacar [Digite 0 para voltar]: ")

                    if sacar > saldo:
                        raise ValueError
                    
                    if sacar == 0:
                        break

                    restante = sacar
                    
                    for nota in notas:
                        if restante == 0:
                            break

                        if restante < nota:
                            continue

                        quantidade = int(restante / nota)
                        restante -= nota * quantidade
                        if quantidade > 0:
                            notas_sacar.append([quantidade, nota])

                    saldo -= sacar

                    title("Sacar")
                    print(f"Voce sacou: R$ {sacar}")
                    print()
                    for sacado in notas_sacar:
                        quantidade_notas = sacado[0]
                        nota_atual = sacado[1]
                        print(f"{quantidade_notas} {'nota' if quantidade_notas < 2 else 'notas'} de R$ {nota_atual}")
                    print()
                    input("Pressione enter para continuar.")
                    break




        except ValueError:
            title("Nao e possivel sacar um valor maior que o saldo.")
            sleep(1)

        except TypeError:
            title("Opcao invalida. Tente novamente.")
            sleep(1)

        except:
            title("Erro")
            sleep(1)