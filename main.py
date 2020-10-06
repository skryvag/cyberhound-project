import os

def Seletor(dificuldade):
  if dificuldade == "1":
    os.system('python FACIL.py')
  if dificuldade == "2":
    os.system('python NORMAL.py')
  if dificuldade == "3":
    os.system('python DIFICIL.py')
  if dificuldade != "0":
   	exit()

print ("Escolha a dificuldade")
print ("1 - Facil")
print ("2 - Normal")
print ("3 - Dificil")
print ("0 - Sair")
dificuldade = input()

Seletor(dificuldade)