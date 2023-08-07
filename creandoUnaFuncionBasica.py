# importamos una libreria nativa de python especializada para calculos matematicos
import math


# la funcion la inicializamos
def funcion_que_recibe_un_numero_y_retorna_su_raiz_cuadrada(numero: float) -> float:
    # en el atributo decimos que tipo de dato puede ser, el interprete no lo considera obligado
    # en la flecha de la funcion indicamos que tipo de dato va a retornar
    # es opcional pero es recomendado para una mejor documentacion

    # hacemos una variable donde guardamos el valor de la raiz
    resultado: float = math.sqrt(numero)

    # retornamos el valor de la funcion
    return resultado


# preguntamos si se ejecuta el programa en main, si es asi  procede a usar la funcion
# e imprimir el resultado en la consola
if __name__ == "__main__":
    num: float = float(input("dame un numero y te digo su raiz cuadrada: "))
    raiz: float = funcion_que_recibe_un_numero_y_retorna_su_raiz_cuadrada(num)
    print(raiz)
