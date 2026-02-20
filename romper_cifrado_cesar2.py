import string 
from langdetect import detect # Importa la función detect para identificar el idioma del texto

ALFABETO = string.ascii_lowercase + string.digits # Define el alfabeto ampliado: letras minúsculas + números del 0 al 9

def algoritmo_descifrado(texto_cifrado, clave_descifrado):
    """Esta funcion descifra el texto cifrado apartir de una clave de descifrado"""
    
    
    texto_plano = ""

     # Se invierte el signo de la clave
    # Esto hace que si la clave era positiva, ahora se use como negativa
    clave_descifrado = -clave_descifrado

    for letra in texto_cifrado:
        if letra not in ALFABETO: 
            texto_plano += letra
        else: 
            indice_letra_cifrada = ALFABETO.index(letra)# Se obtiene la posición (índice) de la letra cifrada dentro del alfabeto
           
           # Se calcula la nueva posición aplicando el desplazamiento
            # El módulo (%) asegura que el índice no se salga del rango del alfabeto
            indice_letra_descifrada = (indice_letra_cifrada - clave_descifrado) % len(ALFABETO)
            texto_plano += ALFABETO [indice_letra_descifrada]         
    return texto_plano 

def fuerza_bruta(texto_cifrado):
    """Esta función realiza fuerza bruta sobre el texto cifrado interceptado"""
    espacio_claves = range(len(ALFABETO)) # Se genera el rango de todas las posibles claves
    for clave in espacio_claves: 
        # Se intenta descifrar el texto con la clave actual
        texto_plano = algoritmo_descifrado(texto_cifrado, clave)
        lenguaje = detect(texto_plano)
        if lenguaje == "es":
            print(f"El texto de cifrado es: {texto_plano}")
            print(f"La clave de cifrado es: {clave}")
            return 
        


if __name__ == "__main__":
    texto_cifrado = input("Por favor introduce el texto cifrado: ").lower()
    #clave_descrifrado = int(input("Por fabor introduzca la clave de descifrado: "))
    #texto_plano = algoritmo_descifrado(texto_cifrado, clave_descrifrado)
    #print(texto_plano)
    fuerza_bruta(texto_cifrado)