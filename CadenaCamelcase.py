def dividir_camel_case(cadena):
    palabras = []
    palabra_actual = ""

    for letra in cadena:
        if letra.isupper() and palabra_actual:
            palabras.append(palabra_actual)
            palabra_actual = letra
        else:
            palabra_actual += letra

    if palabra_actual:
        palabras.append(palabra_actual)

    return palabras

# Solicitud al usuario
cadena = input("Ingrese una cadena en CamelCase: ")

# Obtener palabras y mostrarlas
palabras = dividir_camel_case(cadena)
print(f"Número de palabras: {len(palabras)}")
print("Palabras encontradas:")
for palabra in palabras:
    print(palabra)




