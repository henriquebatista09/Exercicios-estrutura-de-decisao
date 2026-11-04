estudante = input ("voce é estudante? sim/nao")
dia_semana = input (" qual o dia da semana? (terça/outro)")
tipo_sala = input (" qual o tipo de sala (vip/comum)")

if estudante == "sim" or dia_semana == "terça" or  tipo_sala == "comum":
    print ("desconto aplicado")

if estudante == "nao" or dia_semana == "terça" or  tipo_sala == "comum":
    print ("desconto nao aplicado")

if estudante == "sim" or dia_semana == "outro" or  tipo_sala == "comum":
    print ("desconto nao aplicado")

if estudante == "sim" or dia_semana == "terça" or  tipo_sala == "vip":
    print ("desconto nao aplicado")