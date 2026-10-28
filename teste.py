arquivo = open("teste.txt", "r+", enconding="UTF-8")

if arquivo.read() == "":
    arquivo.write("Teste")
else:
    arquivo.seek(0)
    print(arquivo.read())