#5-compter les chiffres d'un nombre donné
def compte_chiff(n):
    if n<10 :
        return n
    else:
        return compte_chiff(n//10)+ n%10
n=int(input("entrez un nombre : "))
print("la somme de chiffres de ce nombre est : ", compte_chiff(n))