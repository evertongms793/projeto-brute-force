usuarios = ["Everton", "Emanuelly", "Eloa"]
senhas = ["1234", "0000", "2024"]

senha_correta = "2024"

for usuario in usuarios:
    for senha in senhas:
        if senha == senha_correta:
            print(usuario, "- acesso liberado")
        else:
            print(usuario, "- acesso negado")
