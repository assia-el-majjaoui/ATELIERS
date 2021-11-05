# 4-la suite de Fibonacci en utilisant la récursivité
def suite_fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (suite_fibonacci(n-1) + suite_fibonacci(n-2))
n = int(input("Entrez le nombre de termes:"))   
print("Suite de Fibonacci est :")
for i in range(n):
    print(suite_fibonacci(i) , end=" ") 