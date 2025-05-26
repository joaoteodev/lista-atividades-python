from time import sleep
from utils import *


def register():
    users = []

    count = 0

    while True:
        title("Registro de usuário")

        while True:
            if count == 0:
                name = input("Digite o nome do usuário (ou 'X' para sair): ").strip()
            else:
                name = input(f"Digite o nome do usuário: ").strip()

            if name and "".join(name.split(" ")).isalpha():
                break
            else:
                title("Nome inválido. Tente novamente.")
                sleep(1)

        if name.upper() == "X":
            return

        age = get_number(f"Digite a idade de {name}: ")

        users.append({"name": name, "age": int(age)})
        title(f"Usuário {name} registrado com sucesso!")
        sleep(1)

        count += 1

        while True:
            continue_registering = (
                input("Deseja registrar outro usuário? (S/N): ").strip().upper()
            )

            if continue_registering in ["S", "N"]:
                break
            else:
                title("Opção inválida. Tente novamente.")
                sleep(1)

        if continue_registering == "N":
            break

    size = len(users)

    title(
        f"Lista de usuários [{size} {"usuário" if size == 1 else "usuários"} registrados]: "
    )
    for user in users:
        print(f"Nome: {user['name']}, Idade: {user['age']}")

    average = sum(user["age"] for user in users) / len(users)
    msg = f"A média de idade dos usuários é {round(average)} anos."
    message(msg)

    younger = min(users, key=lambda x: x["age"])
    msg = f"O usuário mais novo é {younger['name']} com {younger['age']} anos."
    message(msg)

    older = max(users, key=lambda x: x["age"])
    msg = f"O usuário mais velho é {older['name']} com {older['age']} anos."
    message(msg)

    sleep(2)
    print()
    input("Registro concluído. Pressione Enter para voltar ao menu.")
