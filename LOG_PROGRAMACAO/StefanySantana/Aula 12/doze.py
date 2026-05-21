# # 1  cadastro de funcionário 
# print("Seja bem vindo ao Cadastro de funcionários")
# print("Projeto Brigada: Sistema de Gestão de Segurança do Trabalho (SESMT)")
# nome = input("Digite seu nome:  ")
# setor = input("Você atua em que setor?  ").lower() # .lower() padroniza para letras minúsculas
# status = input("Qual o seu status de treinamento?  ")
# print(f"Obrigado Sr. {nome}, seu cadastro foi realizado com sucesso!\n")

# # 2 verificação de EPI
# print(f"Verificando EPIs para seu setor: {setor}... ")

# if setor == "elétrica" or setor == "eletrica":
#     print(f"Seus EPIs necessários para o setor de {setor} são: ")
#     print("- Óculos de proteção")
#     print("- Toucas descartáveis (para proteger o cabelo)")
#     print("- Sapatão")
#     print("ATENÇÃO! RETIRAR TODOS OS ADORNOS (piercings, brincos, colares, anéis...)\n") 
    
#     # A pergunta sobre altura deve ficar dentro do setor ou após a definição dos EPIs básicos
#     altura = input("Você faz trabalho em alturas? (responda com sim ou não): ").lower()
    
#     if altura == "sim":
#         print("Seus EPIs adicionais são: cinturão de segurança e talabarte!")
# else:
#     print("Setor não reconhecido ou sem EPIs específicos cadastrados.")


import tkinter as tk
from tkinter import messagebox

# Função do botão
def cadastrar():

    nome = caixa_nome.get()
    setor = caixa_setor.get().lower()
    status = caixa_status.get().lower()
    altura = caixa_altura.get().lower()

    mensagem = "Funcionário: " + nome + "\n"
    mensagem += "Setor: " + setor + "\n"
    mensagem += "Status do treinamento: " + status + "\n\n"

    # Verificação dos EPIs
    if setor == "eletrica":

        mensagem += "EPIs necessários:\n"
        mensagem += "- Óculos de proteção\n"
        mensagem += "- Touca descartável\n"
        mensagem += "- Sapatão\n"
        mensagem += "- Retirar adornos\n"

        if altura == "sim":
            mensagem += "- Cinturão de segurança\n"
            mensagem += "- Talabarte\n"

    else:
        mensagem += "Setor sem cadastro no nosso sistema."

    messagebox.showinfo("Cadastro realizado", mensagem)

janela = tk.Tk()
janela.title("Cadastro de Funcionário")
janela.geometry("800x400")

texto_nome = tk.Label(janela, text="Digite seu nome")
texto_nome.pack()

caixa_nome = tk.Entry(janela)
caixa_nome.pack()

texto_setor = tk.Label(janela, text="Digite seu setor")
texto_setor.pack()

caixa_setor = tk.Entry(janela)
caixa_setor.pack()

texto_status = tk.Label(janela, text="Status do treinamento")
texto_status.pack()

caixa_status = tk.Entry(janela)
caixa_status.pack()

texto_altura = tk.Label(janela, text="Trabalha em altura? (sim ou não)")
texto_altura.pack()

caixa_altura = tk.Entry(janela)
caixa_altura.pack()

botao = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao.pack(pady=20)

botao_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
botao_fechar.pack()

janela.mainloop()