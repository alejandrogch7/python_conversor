divisa = input(" Introduce tu divisa, 1 para pesos Colombianos, 2 para dólares: ")
divisa = float(divisa)
divisa = round(divisa, 2)

amount = input("introduce la cantidad a convertir: ")
amount = float(amount)

if divisa == 1: 
    valor_dolar = 3700
    tu_cambio = amount/valor_dolar
    tu_cambio = round(tu_cambio, 2) 
    tu_cambio = str(tu_cambio)
    print("Tienes $"+ tu_cambio +" USD")
else: 
    valor_dolar = 3700 
    tu_cambio = amount*valor_dolar
    tu_cambio = round(tu_cambio, 2) 
    tu_cambio = str(tu_cambio)
    print("Tienes $"+ tu_cambio +" COP")


    