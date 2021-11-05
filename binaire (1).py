#2-convertir le nombre decimal en nombre binaire
def convertir():
   f,bin,res=1,0,0
   dec = int(input("entrer le nombre decimal "))
   
   while(dec!=0):
      res = dec % 2
      bin = bin + res * f 
      f = f * 10
      dec = dec//2
      
   return bin 
print("le nombre decimal en nombre binaire est : " ,convertir())
