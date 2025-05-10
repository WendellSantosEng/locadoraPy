import os
import time
import sys

cars_list = [
    ("Chevrolet Opala", 100),
    ("Dodge Dart", 120),
    ("Volkswagen Fusca", 45),
    ("Ford Escort", 70),
]

rental_cars = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_cars(list_cars):
    print("")
    for i, car in enumerate(list_cars):
        print(f"{i} | {car[0]} - R${car[1]}")

def get_out():
    clear_screen()
    print("Obrigado por utilizar a locadora!")
    time.sleep(2)
    sys.exit()

def pause():
    input("\nPressione ENTER para continuar...")

def get_valid_option(prompt, min_val, max_val):
    while True:
        try:
            op = int(input(prompt))
            if op < min_val or op > max_val:
                print("Opção inválida! Tente novamente.")
                continue
            return op
        except ValueError:
            print("Por favor, digite um número válido.")

welcome = 0

while True:
    clear_screen()

    if welcome == 0:
        print("🚗 Bem-vindo à Locadora de Carros 🚗")
        print("")
        pause()
        welcome = 1
    
    print("1 - Mostrar portifólio")
    print("2 - Alugar um carro")
    print("3 - Devolver um carro")
    print("4 - Sair")
    print("")
    
    op = get_valid_option("Escolha: ", 1, 4)

    if op == 1:
        clear_screen()
        print("📋 Carros de nosso portifólio:")
        print_cars(cars_list + rental_cars)
        pause()
    
    elif op == 2:
        clear_screen()

        if cars_list:
            print("🚘 Carros disponíveis:")
            print_cars(cars_list)

            print("")
            code = get_valid_option("Digite o código do carro escolhido: ", 0, len(cars_list)-1)
            days = get_valid_option("Digite a quantidade de dias que ficará com o carro: ", 1, 365)

            clear_screen()
            total = cars_list[code][1] * days
            print(f"Você escolheu o {cars_list[code][0]} por {days} dias, totalizando R${total}. Deseja alugar?")
            print("\n1 - Sim | 2 - Não\n")
            confirm = get_valid_option("Escolha: ", 1, 2)

            if confirm == 1:
                rental_cars.append(cars_list.pop(code))
                clear_screen()
                print("✅ Carro alugado com sucesso!")
            else:
                print("Aluguel cancelado.")
        else:
            print("❌ Nenhum carro disponível para alugar!")
        pause()

    elif op == 3:
        clear_screen()

        if rental_cars:
            print("🔁 Carros para devolução:")
            print_cars(rental_cars)

            print("")
            code = get_valid_option("Digite o código do carro que deseja devolver: ", 0, len(rental_cars)-1)

            clear_screen()
            print(f"Devolver {rental_cars[code][0]}?")
            print("\n1 - Sim | 2 - Não\n")
            confirm = get_valid_option("Escolha: ", 1, 2)

            if confirm == 1:
                cars_list.append(rental_cars.pop(code))
                clear_screen()
                print("✅ Carro devolvido com sucesso!")
            else:
                print("Devolução cancelada.")
        else:
            print("❌ Nenhum carro foi alugado!")
        pause()

    elif op == 4:
        get_out()

    clear_screen()
    print("Deseja continuar no menu principal?")
    print("\n1 - Sim | 2 - Sair\n")
    op = get_valid_option("Escolha: ", 1, 2)

    if op == 2:
        get_out()
