#la fréquence d’un caractère dans une chaîne
def frequence():
    
    ch=str(input("entrez votre chaine : "))
    strr=ch
    n=len(strr)
    c=str(input("entrer le caractere qui vous cherchez : ") )
    j=0

    for i in range (n):
        if strr[i]==c:
            j+=1
    return j

print("le nombre de repetition de ce caractere est :  ", frequence())