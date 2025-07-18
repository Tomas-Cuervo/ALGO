meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado",
}

# Convertir la entrada a número entero
pregunta1 = int(input("Hola, este es un diccionario de palabras modernas, ¿cuántas palabras quieres definir? "))

for i in range(pregunta1):
    pregunta = input("¿Quieres conocer el significado de una palabra?, por favor responde SI o NO en mayúsculas: ")

    if pregunta == "SI":
        word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
        if word in meme_dict:
            print(meme_dict[word])
        else:
            print("Esa palabra no está en el diccionario, por favor ingresa otra")
    
    elif pregunta == "NO":
        print("Gracias por usar el diccionario, ¡Adiós!")
        break
    
    else:
        print("Por favor responde SI o NO en mayúsculas")
