# libreria nativa de python para request (peticion) a la api que nos da el clima
import requests


def temperatura() -> None:  # ponemos que no retornamos nada
    # pon el api key que te da la pagina, hazte una cuenta en: ttps://weatherstack.com/
    api_key = "pon el api aqui con las comillas"

    # pais donde pedimos la temperatura
    pais = "Cuba"

    # la url donde haremos la peticion de la temperatura
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={pais}"

    # hacemos la request (peticion)
    response = requests.get(url)

    # lo convertimos a json
    data = response.json()

    # del json pedimos la temperatura y la retornamos
    return data["current"]["temperature"]


if __name__ == "__main__":
    # llamamos la funcion
    temperature = temperatura()

    # imprimimos la temperatura en la terminal
    print(f"la temperatura actual de cuba es de {temperature} grados celcius")
