'''
Escribe un programa que pueda identificar si una palabra o frase es un palíndromo (https://es.wikipedia.org/wiki/Pal%C3%ADndromo).
'''
def palindromoCheck(inputWord):
    if inputWord  == inputWord[::-1]:
      print(f'{inputWord} es un palíndromo')
    else:
      print(f'{inputWord} NO es un palíndromo')

#Testing Function
palindromoCheck("malayalam")
palindromoCheck("manuel")
palindromoCheck("MalaYaLam")
palindromoCheck("Amar da drama")
palindromoCheck("rock")
palindromoCheck("Amo la pacífica paloma")