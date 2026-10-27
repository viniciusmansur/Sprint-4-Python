import os # *
from time import sleep # *
import matplotlib.pyplot as plt
import requests

historicos = []
histcount = 0

def buscarCidade(nome):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": nome, "count": 1, "language": "pt", "countryCode": "BR"}
    resposta = requests.get(url, params=params, timeout=10)
    dic = resposta.json()
    resultados = dic.get("results")
    cidade = resultados[0]
    return cidade["latitude"], cidade["longitude"]

def buscarClima(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current": "cloud_cover,uv_index,precipitation,visibility,wind_gusts_10m", "daily": "sunrise,sunset,uv_index_max", "timezone": "auto", "forecast_days": 1}
    resposta = requests.get(url, params=params, timeout=10)
    dic = resposta.json()
    return dic

def main():
    global histcount
    while True:
        print(f"MENU EXPLICATIVO DA CÂMERA: \n \n1. Modo pet \n2. Modo documento \n3. Modo Live Suggestions \n4. Histórico \n5. Gráficos\n6. Condições para Foto\n0. Sair")
        op = input("Digite a opção que deseja visualizar: ")
        match op:
            case '1':
                histcount += 1
                opc1()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '2':
                histcount += 1
                opc2()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '3':
                histcount += 1
                opc3()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '4':
                opc4()
                os.system("cls" if os.name == "nt" else "clear") # *

            case '5': # *
                histcount += 1
                opc5() # *
                os.system("cls" if os.name == "nt" else "clear") # *

            case '6':
                histcount += 1
                opc6()
                os.system("cls" if os.name == "nt" else "clear")

            case '0':
                ponto = '.'
                for _ in range(3): # *
                    print(f"Saindo{ponto}")
                    sleep(0.8) # *
                    ponto += "."
                return
            
            case _:
                print("Opção inválida")

#Função Modo pet - descrição
def opc1():
    os.system("cls" if os.name == "nt" else "clear") # *
    historicos.append("Modo Pet")
    print("Modo Pet:")
    print("Esse modo é focado em tirar fotos de forma automática de pets assim que a câmera for estabilizada e reconhecer o animal.")
    input("Digite algo para voltar: ")

#Função Modo documento - descrição
def opc2():
    os.system("cls" if os.name == "nt" else "clear") # *
    historicos.append("Modo Documento")
    print("Modo Documento:")
    print("Esse modo escaneia textos e os envias para a área de transferencia do celular.")
    input("Digite algo para voltar: ")

#Função Modo live suggestions - descrição
def opc3():
    os.system("cls" if os.name == "nt" else "clear") # *
    historicos.append("Modo Live Suggestions")
    print("Modo Live Suggestions:")
    print("Esse modo analisa a cena atual e sugere quais alterações nas configurações da câmera seriam ideais para aquela ocasião.")
    input("Digite algo para voltar: ")

#Função Histórico - mostra a histórico
def opc4():
    barra = '-------------------------'
    os.system("cls" if os.name == "nt" else "clear") # *
    print("Seu histórico: ")
    print("Você acessou 1 modo." if histcount == 1 else f"Você acessou {histcount} modos.")
    print(barra)

    print(f"Histórico: ", end='')
    for i in historicos: # *
        print(i, end=' | ')

    print(f"\n{barra}")
    input("Digite algo para voltar: ")

def opc5():
    os.system("cls" if os.name == "nt" else "clear") # *
    historicos.append("Gráficos")
    while True:
        print("\nGRÁFICOS DA PESQUISA: \n1. Aceitação dos modos\n2. Modo Documento por faixa etária\n3. Aceitação do Live Suggestions\n4. Aceitação do Modo Pet\n0. Voltar")
        op = input("- ")
        match op:
            case '1':
                modos = ['Documento', 'Pet', 'Live Suggestions']
                aprovacao = [43, 39, 31]

                plt.bar(modos, aprovacao)
                plt.title('Aceitação dos Modos da Câmera')
                plt.xlabel('Modos')
                plt.ylabel('Quantidade de pessoas')
                plt.text(0, 43, '43')
                plt.text(1, 39, '39')
                plt.text(2, 31, '31')
                plt.ylim(0, 55)
                plt.show()

            case '2':
                idade = ['19 a 30 anos', 'Outras idades']
                documento = [34, 9]
 
                plt.bar(idade, documento)
                plt.title('Aceitação do Modo Documento por Idade')
                plt.xlabel('Faixa etária')
                plt.ylabel('Quantidade de pessoas')
                plt.text(0, 34, '34')
                plt.text(1, 9, '9')
                plt.ylim(0, 40)
                plt.show()

            case '3':
                perfil = ['Trabalham com\nredes sociais', 'Outros participantes']
                live = [14, 17]

                plt.bar(perfil, live)
                plt.title('Aceitação do Live Suggestions')
                plt.xlabel('Perfil dos participantes')
                plt.ylabel('Quantidade de pessoas')
                plt.text(0, 14, '14')
                plt.text(1, 17, '17')
                plt.show()

            case '4':
                avaliacao = ['Aprovaram', 'Não aprovaram']
                pet = [39, 16]
 
                plt.bar(avaliacao, pet)
                plt.title('Aceitação do Modo Pet')
                plt.xlabel('Avaliação')
                plt.ylabel('Quantidade de pessoas') 
                plt.text(0, 39, '39')
                plt.text(1, 16, '16')
                plt.ylim(0, 55)
                plt.show()

            case '0':
                break

            case _:
                print("Opção inválida")

def opc6():
    os.system("cls" if os.name == "nt" else "clear")
    historicos.append("Condições para Foto")
    print("Digite o nome da sua cidade")
    nome = input("- ")
    resultado = buscarCidade(nome)
    lat = resultado[0]
    lon = resultado[1]
    dic = buscarClima(lat, lon)
    print("Análise de clima: ")
    print(f"Para a cidade {nome}, os valores que alteram a qualidade de uma foto são:")
    print(f"Porcentagem de Nuvens: {dic['current']['cloud_cover']}%")
    print(f"Índice UV: {dic['current']['uv_index']}")
    print(f"Precipitação: {dic['current']['precipitation']}mm")
    print(f"Visibilidade: {dic['current']['visibility']}m")
    print("--------------------------------")
    if dic["current"]["cloud_cover"] >= 80:
        print("Céu muito encoberto: luz fraca e sem contraste. Aumente o ISO ou use o modo HDR")
    else:
        print("Céu limpo: luz normal e contraste OK. Nenhuma alteração sugerida")
    
    if dic["current"]["uv_index"] >= 8:
        print("UV muito alto: Sol forte, sombras duras. Evite fotografar de frente para o Sol ou use o modo HDR")
    else:
        print("UV normal: Sol ameno, sombras OK. Nenhuma alteração sugerida")

    if dic["current"]["precipitation"] > 0:
        print("Chuva identificada: chance de molhar ou borrar câmera. Proteja seu celular da chuva")
    else:
        print("Chuva não identificada: sem risco de molhar o celular. Nenhuma sugestão")

    if dic["current"]["visibility"] < 1000:
        print("Neblina forte: visibilidade reduzida e sem contraste. Aumente o ISO ou use o modo HDR")
    else:
        print("Visibilidade alta: sem neblina e contraste OK. Nenhuma alteração sugerida")

    input("\nDigite algo para voltar: ")

main()