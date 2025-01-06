## Função = um conjunto de instruções que precisam ser repetidas durante a execução do sistema

# def funcao1():
#     print("Hello world")

# funcao1()

# def funcao2(argumento):
#     print(f"Sua idade é de {argumento}")

# funcao2(46)

# def funcao3(arg1, arg2):
#     return arg1*arg2

# resultado_conta_funcao3 = funcao3(20,2)
# print(resultado_conta_funcao3)


idade = int(input("Digite a sua idade:"))

def pode_ter_CNH(x):
    if x>= 18:
        print("Pode ter CNH")
    else:
        print("Não pode ter CNH")


pode_ter_CNH(idade)