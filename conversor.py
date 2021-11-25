menu = """
Bienvenido al conversor de monedas 💰💰💰

1 - Pesos argentinos 
2 - Pesos colombianos 
3 - Pesos mexicanos 
Elige una opción: """

opcion = int(input(menu))

if opcion == 1: 
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 100.57
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2: 
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3959
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 21.23
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else: 
    print("😅 Por favor, ingresa una opción válida")
