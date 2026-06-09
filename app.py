import time
import dice

def lanzar_dados(amount, sides):
    formula = f"{amount}d{sides}"
    resultados = dice.roll(formula)
    return resultados

sides = 20
amount = 6

resultados_obtenidos = lanzar_dados(amount, sides)

for indice, resultado in enumerate(resultados_obtenidos, start=1):
    print(f"Lanzamiento {indice} número obtenido {resultado}")
    if indice < amount: 
        time.sleep(5) 