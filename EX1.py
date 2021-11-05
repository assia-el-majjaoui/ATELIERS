
MY_LIST=[3,18,9,22,7,45,34,50]
MY_LIST1=[]
MY_LIST2=[]
MY_LIST3=[]
print(MY_LIST)
print("l'indix pair est :")
for element in MY_LIST: 
    if (MY_LIST.index(element)%2==0):
      print( "l'index : ",MY_LIST.index(element))
      print("l'element est :",element) 
      MY_LIST1.append(element ) 
print("la liste des indix pair est" , MY_LIST1) 
        
print("l'indix impair est :")     
for element in MY_LIST:       
    if (MY_LIST.index(element)%2==1):
      print("l'indix : " ,MY_LIST.index(element))
      print("l'element est : ",element)
      MY_LIST2.append(element ) 
print("la liste des indix pair est" ,MY_LIST2)      
MY_LIST3 =MY_LIST1 +MY_LIST2
print( "la liste finale est :" ,MY_LIST3)