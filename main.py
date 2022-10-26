# comando imput (): quero permiotir que 
#o usuario digite algo...
nome =  input("Digite seu nome: ")
#ped  a aidade para o usuario   "Qual sua idade ?"
idade  = int(input("digite sua idade: "))

#comando  de saída...exib ir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba  "sua idade"
print(f"Sua idade é {idade}")

#e se eu quisesse mostrar o dobro da idade informada?
dobro  =  idade * 2
print("O dobro da idade informada é {}".format(dobro))
