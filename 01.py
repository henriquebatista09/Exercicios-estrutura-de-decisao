idade = float (input("digite sua idade"))
altura = float (input("digite sua altura"))
autorização = input ("tem autorização dos pais")

if idade >=12 and altura >=140 or autorização == "sim" :
    print ("acesso liberado")

if idade <12 and altura <140 and autorização == "sim":
    print ("acesso liberado")

if idade <12 and altura <140 and autorização == "nao":
    print ("acesso negado")