from utils import *
from time import sleep


def atm():
    saldo = 0
    notas = [100, 50, 20, 10, 5, 2]

    while True:
        notas_sacar = []
        try:
            title("Caixa eletrônico")

            print(f"Seu saldo é: R$ {saldo}")
            print()

            while True:
                print("1 - Depositar dinheiro")
                print("2 - sacar dinheiro")
                print("X - Sair")
                print()
                option = input("Selecione uma opção: ").strip().upper()

                if option not in "12X":
                    raise TypeError("Opcao invalida. Tente novamente.")

                if option == "1":
                    title("Depositar")
                    amount = get_number("Digite o valor que deseja depositar: ")
                    if amount < 0:
                        raise ValueError(
                            "Não é possível depositar valor menor que zero. Tente novamente."
                        )
                    if amount == 0:
                        title("Operação cancelada")
                        print("Nenhum valor foi depositado.")
                        sleep(1)
                        break
                    if "," in str(amount) or "." in str(amount):
                        raise ValueError(
                            "Não é possível depositar moedas. Tente novamente."
                        )

                    title("Depositar")
                    print(f"Você depositou: R$ {amount}")
                    print()
                    print("Operação realizada com sucesso!")
                    sleep(1)
                    print()
                    input("Pressione enter para continuar.")
                    print()
                    saldo += amount
                    break

                if option == "2":
                    title("Sacar")
                    print(f"Saldo disponivel: R$ {saldo}")
                    print()

                    sacar = get_number(
                        "Digite o valor que deseja sacar [Digite 0 para voltar]: "
                    )

                    if sacar > saldo:
                        raise ValueError(
                            "Valor maior que o saldo disponivel. Tente novamente."
                        )

                    if sacar < 0:
                        raise ValueError("Valor negativo. Tente novamente.")

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

                    if restante > 0:
                        raise ValueError(
                            "Não é possível sacar esse valor com as notas disponíveis. Tente novamente."
                        )

                    saldo -= sacar

                    title("Sacando")
                    print(f"Voce sacou: R$ {sacar}")
                    print()
                    for sacado in notas_sacar:
                        quantidade_notas = sacado[0]
                        nota_atual = sacado[1]
                        print(
                            f"{quantidade_notas} {'nota' if quantidade_notas < 2 else 'notas'} de R$ {nota_atual}"
                        )
                    print()
                    input("Pressione enter para continuar.")
                    break

                if option == "X":
                    title("Saindo")
                    print("Obrigado por usar nosso caixa eletrônico!")
                    sleep(1)
                    return
        except ValueError as e:
            msg = str(e)
            title(msg)
            sleep(1)

        except TypeError as e:
            msg = str(e)
            title(msg)
            sleep(1)

        except:
            title("Erro")
            sleep(1)
