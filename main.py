# Generador de contraseñas

# Importamos la librería secrets para elegir caracteres de forma segura
import secrets

print(" === GENERADOR DE CONTRASEÑAS === ")

# Pedimos al usuario la longitud de la contraseña
longitud = 0

# Repetimos hasta obtener una longitud válida
while longitud <= 0:
    try:
        longitud = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? "))
    except ValueError:
        print("Eso no es un número")


# Validamos las respuestas de tipo s/n
def respuesta(mensaje):
    mensaje = mensaje.lower().strip()

    while mensaje != "s" and mensaje != "n":
        mensaje = input("Por favor, ingresa 's' para sí o 'n' para no: ").lower().strip()

    return mensaje


# Guardamos los caracteres disponibles para la contraseña
contrasenia = ""

minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()

numeros = "0123456789"
simbolos = "!@#$%&*?+-_="

caracteres = minusculas + mayusculas

# Preguntamos si se deben incluir números
incluir_numeros = respuesta(input("¿Incluir números? (s/n): "))

if incluir_numeros == "s":
    caracteres += numeros

# Preguntamos si se deben incluir símbolos
incluir_simbolos = respuesta(input("¿Incluir símbolos? (s/n): "))

if incluir_simbolos == "s":
    caracteres += simbolos


# Generamos la contraseña carácter por carácter
for _ in range(longitud):
    contrasenia += secrets.choice(caracteres)

# Mostramos la contraseña generada
print(f"Tu contraseña es: {contrasenia}")