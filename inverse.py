#7-inverse les lettres d’une chaîne de caractères
def inverse_chaine():
  chaine = str (input( "entrez votre chaine de caractere :  "))
  
  str1=chaine
  n= len(str1)
  print(" l'inverse de chaine de caractere est : " )
  for i in range ( 1,n+1):
   print( str1[-i] ,end="")
inverse_chaine()