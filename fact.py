    #1-la somme de serie :
som=0
def fac(n):
    reseltat=1
    for i in range( 1,n+1):
        reseltat *=  i
    return reseltat
som=fac(1)/1 + fac(2)/2 +fac(3)/3 + fac(4)/4 +fac(5)/5
print("la somme de cette serie est : " , som)


