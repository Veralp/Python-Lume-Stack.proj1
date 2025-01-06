# condição -> comparar -> Operadores relacionais

#10 == 10 true
#10 != 10 false
#10 > 10 false
#10 < 10 false
#10 >= 10 true
#10 <= 10 true

# OBS Tipagem dinamica FORTE - Tem que ter o mesmo tipo de data

# EXERCICIO
# Tirar cnh
#INPUT
#processar - idade >= 18 - pode ter CNH // idade < 18 -nao pode ter CNH.
#Retotna - Pode ter CNH // Nao pode ter CNH.
# casting - é trasformar o tipo da variavel. (colocou um int na frente do input)

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Pode ter CNH")
else:
    print ("Não pode ter CNH")

