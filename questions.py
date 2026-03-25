import random
# Se agregan categorias para seleccionar
categories = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "datos": ["lista", "entero", "cadena"],
    "general": ["programa"]
}
# Se imprimen las categorias disponibles:
print("Categorías disponibles:")
for cat in categories:
    print("-", cat)

category = input("Seleccione una categoría: ")
# Se valida que la opcion seleccionada sea correcta!
while category not in categories:
    category = input("Categoría inválida. Seleccione otra: ")

words = random.sample(categories[category], len(categories[category]))
score = 0
for word in words:
    guessed = []
    attempts = 6

    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
    # Se agrega suma de Puntos al completar la Palabra!
            score += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
    
        letter = input("Ingresá una letra: ")
    # Validacion para verificar si ingrese una letra!
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
    # Se agrega la eliminacion de puntaje!
            score -= 1 
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0
        break

print(f"Puntaje final: {score}")
