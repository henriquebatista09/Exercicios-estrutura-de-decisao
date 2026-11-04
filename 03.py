renda = float(input("qual sua renda mensal?"))
score = float (input("qual seu score de credito? 0/1000"))
bens = (input("possui bens como garantia? sim/nao"))
historico = (input("tem historico inadiplente? sim/nao"))

if renda >=3000 and score >=600 and historico == "nao":
     print("empretimo aprovado")

if historico == "nao" and bens == "sim":
     print("emprestimo aprovado")

if bens == "nao" and historico == "sim":
     print ("emprestimo reprovado")

if bens == "sim" and historico == "sim":
     print ("emprestimo reprovado")

if bens == "sim" and historico == "nao":
     print ("emprestimo aprovado")