def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)

    enPesos = int((money-expense) // 1)
    enCentavos = int(((money-expense) - int(money-expense)) * 100)

    print("\nVuelto")
    print("\nPesos:")
    print(enPesos)
    print("Centavos:")
    print(enCentavos)

change()