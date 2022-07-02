def referenciaAutor(nome):
    nomes = nome.split()
    ultimo_nome = nomes[-1].upper()
    outros_nomes = " ".join(nomes[:-1])
    return f"{ultimo_nome}, {outros_nomes};"


def MatrizNula(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(linhas):
            linha.append(0)
        matriz.append(linha)
    return matriz


def ordenaMatriz(matriz):
    numeros = []
    nova_matriz = MatrizNula(len(matriz), len(matriz[0]))
    for linha in matriz:
        numeros.extend(linha)
    numeros.sort()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            nova_matriz[i][j] = numeros.pop(0)
    return nova_matriz


def inputMatriz(linhas, colunas):
    matriz = []
    for i in range(1, linhas + 1):
        while True:
            linha = list(map(int, input(f"Linha {i}: ").split()))
            if len(linha) != colunas:
                print("Quantidade inválida de colunas!")
            else:
                matriz.append(linha)
                break
    return matriz


def formatarMatriz(matriz):
    linhas = []
    for linha in matriz:
        linhas.append(" ".join(map(str, linha)))
    return "\n".join(linhas)


# Algoritmo 1
print("~ Referência de Autor ~")
nome = input("Qual é o seu nome completo? ")
print(f'Sua referência de autor é "{referenciaAutor(nome)}"')

print()

# Algoritmo 2
print("~ Ordenação de matriz ~")

n = int(input("Quantidade de dimensões: "))

matriz = inputMatriz(n, n)

print(f"\nEssa matriz fica assim quando ordenada:\n{formatarMatriz(ordenaMatriz(matriz))}")
