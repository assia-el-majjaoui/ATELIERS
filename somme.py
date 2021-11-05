#3-la somme des nombres de 1 a n 
def som_recu(n):
    if (n <= 1 ):
        return n
    else:    
        return ( som_recu( n-1 ) + n )
n=int(input("entrez le nombre : "))
print("la somme des nombres est : ",som_recu(n))