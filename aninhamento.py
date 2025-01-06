## aninhamento de Condicional
 # Lógica de programçao / Lógica Booliana
 # O que é preposição?
#Uma afirmação não ambiqua e tem valor defenitivo de verdadeiro
#
# p = ) céu é azul. == 1
 # " = O céu não é Aszul. == False == 0

## Exempol de Aninhamento.
# IBGE - Pesquisa com publico alvo que possua CNh ativa e  nascidos entre 1980 a 2000

# inputs
# ano-de-nascimento, cnh-ativa
# processamento:
#  se cnh ativa -> checar o intervalo do ano de nascimento
#  se não ativa -> Agradecer a participação
# output:
#  se estver dentro do intervalo -> pedir paar preencher o form.
#  se não estiver dentro do interrvalo -> Agrade3cer a participação

cnh_ativa = input("Voce posui CNH atva? Digite s para Sim e N para Não:")

if cnh_ativa == "s":
    ano_de_nascimento =  int(input("Digite seu ano de nascimento:"))
    if ano_de_nascimento <= 2000:
        if ano_de_nascimento>= 1980: 
            print("pedir para preencher o form")
        else:
            print("Agradecr a participação? menor qu interval")
    else:
        print("Agradecer a participação/maior que intervalo ")        
else:
    print("Agradecer a participação/ sem cnh ativa")  

# Manipulação de preposição composta E and ? Ou or

ano_de_nascimento =  int(input("Digite seu ano de nascimento:"))

if cnh_ativa == "s" and ano_de_nascimento <= 2000 and ano_de_nascimento >= 1998:
    print("pedir para reencher o form")

else:
    print("Agradecer a participação/ sem cnh ativa")  