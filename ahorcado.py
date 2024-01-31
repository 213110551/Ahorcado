class Ahorcado:
    def jugar_ahorcado():
        palabra = input("escribe una palabra: ")
        letras = "_" * len(palabra)
        intentos = 0

        while True:
            print(letras)
            letra_t = input("escribe una letra: ")
            if letra_t in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra_t:
                        letras = letras[:i] + letra_t + letras[i + 1:]
            else:
                intentos += 1
                Ahorcado.dibujar_ahorcado(intentos, letras, palabra)

                if intentos == 6:
                    print("has perdido, se acabaron los intentos. :(")
                    break

            if letras == palabra:
                print("Felicidades has adivinado la palabra :)")
                break

    def dibujar_ahorcado(intentos, letras, palabra):
        intentos += 1
        if intentos == 1:
            print("     ")
            print("   O ")
        elif intentos == 2:
            print("     ")
            print("   O ")
            print("   0 ")
        elif intentos == 3:
            print("     ")
            print("   O ")
            print("  (0)")
        elif intentos == 4:
            print("     ")
            print("   O ")
            print("  (0)")
            print("   LL")
        elif intentos == 5:
            print("   ! ")
            print("   O ")
            print("  (0)")
            print("   LL")
        elif intentos == 6:
            print("---! ")
            print("   O ")
            print("  (0)")
            print("   LL")
            print("has perdido, se acabaron los intentos. :(")

        if letras == palabra:
            print("Felicidades has adivinado la palabra :)")