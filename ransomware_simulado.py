arquivo = "teste.txt"

# Criptografar
with open(arquivo, "r") as f:
    conteudo = f.read()

conteudo_crip = conteudo[::-1]

with open(arquivo, "w") as f:
    f.write(conteudo_crip)

print("Arquivo criptografado (simulação)")

# Descriptografar
with open(arquivo, "r") as f:
    conteudo = f.read()

conteudo_original = conteudo[::-1]

with open(arquivo, "w") as f:
    f.write(conteudo_original)

print("Arquivo recuperado!")
