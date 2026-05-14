# 1  cadastro de funcionário 
print("Seja bem vindo ao Cadastro de funcionários")
print("Projeto Brigada: Sistema de Gestão de Segurança do Trabalho (SESMT)")
nome = input("Digite seu nome:  ")
setor = input("Você atua em que setor?  ").lower() # .lower() padroniza para letras minúsculas
status = input("Qual o seu status de treinamento?  ")
print(f"Obrigado Sr. {nome}, seu cadastro foi realizado com sucesso!\n")

# 2 verificação de EPI
print(f"Verificando EPIs para seu setor: {setor}... ")

if setor == "elétrica" or setor == "eletrica":
    print(f"Seus EPIs necessários para o setor de {setor} são: ")
    print("- Óculos de proteção")
    print("- Toucas descartáveis (para proteger o cabelo)")
    print("- Sapatão")
    print("ATENÇÃO! RETIRAR TODOS OS ADORNOS (piercings, brincos, colares, anéis...)\n") 
    
    # A pergunta sobre altura deve ficar dentro do setor ou após a definição dos EPIs básicos
    altura = input("Você faz trabalho em alturas? (responda com sim ou não): ").lower()
    
    if altura == "sim":
        print("Seus EPIs adicionais são: cinturão de segurança e talabarte!")
else:
    print("Setor não reconhecido ou sem EPIs específicos cadastrados.")