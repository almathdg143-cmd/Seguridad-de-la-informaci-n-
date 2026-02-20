import string 
from langdetect import detect

ALFABETO = string.ascii_lowercase + string.digits

def algoritmo_descifrado(texto_cifrado, clave_descifrado):
    """Esta funcion descifra el texto cifrado apartir de una clave de descifrado"""
    
    
    texto_plano = ""
    clave_descifrado = -clave_descifrado

    for letra in texto_cifrado:
        if letra not in ALFABETO: 
            texto_plano += letra
        else: 
            indice_letra_cifrada = ALFABETO.index(letra)
            indice_letra_descifrada = (indice_letra_cifrada - clave_descifrado) % len(ALFABETO)
            texto_plano += ALFABETO [indice_letra_descifrada]         
    return texto_plano 

def fuerza_bruta(texto_cifrado):
    """Esta función realiza fuerza bruta sobre el texto cifrado interceptado"""
    espacio_claves = range(len(ALFABETO))
    for clave in espacio_claves: 
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