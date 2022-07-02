s = input("Entrada: ")

nova_string = ""

for caractere in s:
    if caractere.isalpha():
        if caractere in "aeiou":
            nova_string += caractere.upper()
        else:
            nova_string += caractere

print(f"Saída: {nova_string}")
