def transform_usd(currency, usd_value):
    currency = float(input("Cúanto dinero tienes?"))
    usd_value = currency/usd_value
    usd_value = round(usd_value,2)
    usd_value = str(usd_value)
    print("Tienes $ "+ usd_value +" dólares")

def usd_transform(currency, usd_value):
    currency = float(input("Cúanto dinero tienes? "))
    usd_value = currency*usd_value
    usd_value = round(usd_value,2)
    usd_value = str(usd_value)
    print("Tienes $ "+ usd_value +" pesos")

menu = """
Si vas a convertir de una divisa a dolares estas son tus opciones:  

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Si vas a convertir tus dólares a una divisa, escoge cual, estas son tus opciones:

4 - Pesos Colombianos
5 - Pesos Argentinos 
6 - Pesos Mexicanos

Elige una opción: """

option = int(input(menu))    

if option == 1:
    transform_usd("colombianos", 3422)
elif option == 2:
    transform_usd("argentinos", 85)
elif option == 3:
    transform_usd("mexicanos", 19)
elif option == 4:
    usd_transform("colombianos", 3422)
elif option == 5:
    usd_transform("argentinos", 85)
elif option == 6:
    usd_transform("mexicanos", 19)
else:
    print('Ingresa una opción correcta por favor')


    
