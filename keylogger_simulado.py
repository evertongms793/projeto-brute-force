texto = input("Digite algo: ")

with open("log.txt", "a") as arquivo:
    arquivo.write(texto + "\n")

print("Teclas registradas (simulação)")
