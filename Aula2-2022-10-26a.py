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

#Estrutura condicional - o famoso "SE" (if)
#Se  a pessoa for maior de idade mostre "Você é  maior de idade, ótimo! Já pode beber ou dirigir"
if  idade >=  18:
  print("você é maior de idade, ótimo! já pode   beber ou dirigir")
else:
  print("Você é jóvem ainda, jóvem ainda...")

#E se eu quisesse pergun tar o gênero  (M=Masculino e f= vFeminino
#mostre  (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("informe o gênero M=Masculino, F=Feminino, O=Outros: " )
if idade >= 18 and genero ==  "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")
else:
  print("...  e você não precisa/precisou prestar o serviço militar obrigatório")