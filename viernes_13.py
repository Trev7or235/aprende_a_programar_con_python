# importamos libreria nativa de python para el tiempo
import datetime


# funcion que devuelve un booleano de True o False si hay un viernes 13


def viernes_13(año: int, mes: int, dia: int = 13) -> bool:
    # enviamos los datos a datetime y nos devuelve un int
    datos = datetime.datetime(año, mes, 13)
    # si el int es igual a 4 (viernes) no devuelve True sino False
    return datos.weekday() == 4


# verificamos que sea main el modulo
if __name__ == "__main__":
    # ponemos el año a verificar
    año: int = 2023

    # ponemos el mes a verificar
    mes: int = 2

    # guardamos el resultado en una variable
    result = viernes_13(año, mes)

    # lo imprimimos en la consola
    print(result)
