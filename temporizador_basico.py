# libreria que nos permite trabajar con la pc
import os

import time
import datetime


# solo funciona para linux, para windows es otra forma
def limpiar_terminal() -> None:
    # limpiamos la consola con el comando clear
    os.system("clear")


def main() -> None:
    # guardamos el tiempo de ejecucion de la funcion
    inicio = datetime.datetime.now()

    while True:
        tiempo_transcurrido = datetime.datetime.now() - inicio
        tiempo_formateado = str(tiempo_transcurrido).split(".")[0]
        print(tiempo_formateado, end="\r")
        time.sleep(0.1)


if __name__ == "__main__":
    input("presione ENTER para iniciar el cronometro")
    limpiar_terminal()
    main()
