import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Variáveis globais
historicos = []
histcount = 0

# --- Funções dos Modos ---

def opc1():
    global histcount
    histcount += 1
    historicos.append("Modo Pet")
    mensagem = "Esse modo é focado em tirar fotos de forma automática de pets assim que a câmera for estabilizada e reconhecer o animal."
    messagebox.showinfo("Modo Pet", mensagem)

def opc2():
    global histcount
    histcount += 1
    historicos.append("Modo Documento")
    mensagem = "Esse modo escaneia textos e os envias para a área de transferencia do celular."
    messagebox.showinfo("Modo Documento", mensagem)

def opc3():
    global histcount
    histcount += 1
    historicos.append("Modo Live Suggestions")
    mensagem = "Esse modo analisa a cena atual e sugere quais alterações nas configurações da câmera seriam ideias para aquela ocasião."
    messagebox.showinfo("Modo Live Suggestions", mensagem)

def opc4():
    texto_qtd = "Você acessou 1 modo." if histcount == 1 else f"Você acessou {histcount} modos."
    
    if historicos:
        texto_hist = " | ".join(historicos)
    else:
        texto_hist = "Nenhum modo acessado ainda."
        
    mensagem = f"{texto_qtd}\n{'-'*25}\nHistórico: {texto_hist}"
    messagebox.showinfo("Histórico", mensagem)

# --- Funções dos Gráficos (Matplotlib) ---

def graf_aceitacao_modos():
    modos = ['Documento', 'Pet', 'Live Suggestions']
    aprovacao = [43, 39, 31]

    plt.bar(modos, aprovacao, color=['blue', 'orange', 'green'])
    plt.title('Aceitação dos Modos da Câmera')
    plt.xlabel('Modos')
    plt.ylabel('Quantidade de pessoas')
    plt.text(0, 43, '43', ha='center', va='bottom')
    plt.text(1, 39, '39', ha='center', va='bottom')
    plt.text(2, 31, '31', ha='center', va='bottom')
    plt.ylim(0, 55)
    plt.show()

def graf_documento_idade():
    idade = ['19 a 30 anos', 'Outras idades']
    documento = [34, 9]

    plt.bar(idade, documento, color='purple')
    plt.title('Aceitação do Modo Documento por Idade')
    plt.xlabel('Faixa etária')
    plt.ylabel('Quantidade de pessoas')
    plt.text(0, 34, '34', ha='center', va='bottom')
    plt.text(1, 9, '9', ha='center', va='bottom')
    plt.ylim(0, 40)
    plt.show()

def graf_live_suggestions():
    perfil = ['Trabalham com\nredes sociais', 'Outros participantes']
    live = [14, 17]

    plt.bar(perfil, live, color='teal')
    plt.title('Aceitação do Live Suggestions')
    plt.xlabel('Perfil dos participantes')
    plt.ylabel('Quantidade de pessoas')
    plt.text(0, 14, '14', ha='center', va='bottom')
    plt.text(1, 17, '17', ha='center', va='bottom')
    plt.ylim(0, 25)
    plt.show()

def graf_pet():
    avaliacao = ['Aprovaram', 'Não aprovaram']
    pet = [39, 16]

    plt.bar(avaliacao, pet, color=['green', 'red'])
    plt.title('Aceitação do Modo Pet')
    plt.xlabel('Avaliação')
    plt.ylabel('Quantidade de pessoas') 
    plt.text(0, 39, '39', ha='center', va='bottom')
    plt.text(1, 16, '16', ha='center', va='bottom')
    plt.ylim(0, 55)
    plt.show()

# --- Submenu de Gráficos ---

def opc5():
    global histcount
    histcount += 1
    
    # Cria uma nova janela (Toplevel) para o menu de gráficos
    janela_graficos = tk.Toplevel(janela_principal)
    janela_graficos.title("Gráficos da Pesquisa")
    janela_graficos.geometry("350x250")
    
    tk.Label(janela_graficos, text="Selecione o gráfico:", font=("Arial", 12, "bold")).pack(pady=10)
    
    tk.Button(janela_graficos, text="1. Aceitação dos modos", width=30, command=graf_aceitacao_modos).pack(pady=5)
    tk.Button(janela_graficos, text="2. Modo Documento por faixa etária", width=30, command=graf_documento_idade).pack(pady=5)
    tk.Button(janela_graficos, text="3. Aceitação do Live Suggestions", width=30, command=graf_live_suggestions).pack(pady=5)
    tk.Button(janela_graficos, text="4. Aceitação do Modo Pet", width=30, command=graf_pet).pack(pady=5)
    tk.Button(janela_graficos, text="0. Voltar", width=15, command=janela_graficos.destroy).pack(pady=10)

# --- Janela Principal ---

janela_principal = tk.Tk()
janela_principal.title("Menu da Câmera")
janela_principal.geometry("350x350")

tk.Label(janela_principal, text="MENU EXPLICATIVO DA CÂMERA", font=("Arial", 12, "bold")).pack(pady=15)

# Botões do Menu Principal
tk.Button(janela_principal, text="1. Modo Pet", width=25, command=opc1).pack(pady=5)
tk.Button(janela_principal, text="2. Modo Documento", width=25, command=opc2).pack(pady=5)
tk.Button(janela_principal, text="3. Modo Live Suggestions", width=25, command=opc3).pack(pady=5)
tk.Button(janela_principal, text="4. Histórico", width=25, command=opc4).pack(pady=5)
tk.Button(janela_principal, text="5. Gráficos", width=25, command=opc5).pack(pady=5)

# O botão de Sair chama o método destroy() da janela principal, fechando o app
tk.Button(janela_principal, text="0. Sair", width=15, fg="red", command=janela_principal.destroy).pack(pady=20)

# Inicia o loop da interface gráfica
janela_principal.mainloop()