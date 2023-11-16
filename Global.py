def mutante(ADN):
    # defino las variables
    n = len(ADN)
    secuencias = 0


    for i in range(n):
        for j in range(n - 3):
            # Reviso secuencias horizontales
            if ADN[i][j] == ADN[i][j + 1] == ADN[i][j + 2] == ADN[i][j + 3]:
                secuencias += 1

            # Reviso secuencias verticales
            if ADN[j][i] == ADN[j + 1][i] == ADN[j + 2][i] == ADN[j + 3][i]:
                secuencias += 1

    # Reviso secuencias diagonales
    for i in range(n - 3):
        for j in range(n - 3):
            if ADN[i][j] == ADN[i + 1][j + 1] == ADN[i + 2][j + 2] == ADN[i + 3][j + 3]:
                secuencias += 1
            if ADN[i][j + 3] == ADN[i + 1][j + 2] == ADN[i + 2][j + 1] == ADN[i + 3][j]:
                secuencias += 1

    return secuencias > 1

def ingresar_secuencias():
    ADN = []
    while len(ADN) < 6:
        secuencia = input("Ingrese una secuencia de ADN (6 caracteres entre A, T, C, G): ").upper()
        if len(secuencia) == 6 and all(caracter in "ATCG" for caracter in secuencia):
            ADN.append(secuencia)
        else:
            print("Secuencia inválida, intente nuevamente.")
    return ADN

def main():
    print("------------------------------------")
    print("BIENVENIDO AL SISTEMA DE ESCANEO DE MUTANTES")
    print("------------------------------------")
    dna = ingresar_secuencias()
    if mutante(dna):
        print("------------------------------------")
        print("¡SE HA DETECTADO UN MUTANTE!")
        print("------------------------------------")
    else:
        print("------------------------------------")
        print("ADN normal, no se detectaron mutaciones...")
        print("------------------------------------")

if __name__ == "__main__":
    main()