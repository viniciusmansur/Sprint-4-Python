try:
    arquivo = open("teste.txt", "r+", encoding="UTF-8")
except:
    arquivo = open("teste.txt", "w+", encoding="UTF-8")
    arquivo.write("Vinícius")
    arquivo.seek(0)
    print(arquivo.read())
else:
    print(arquivo.read())
finally:
    arquivo.close()

# if arquivo.read() == "":
#     arquivo.write("Vinícius")
#     print(arquivo)
# else:
#     arquivo.seek(0)
#     print(arquivo.read())