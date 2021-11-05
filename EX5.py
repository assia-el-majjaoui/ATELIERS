MY_LIST=[1,3,9,0,4 ]
my_dict={"Assia":1,"Douae":4}
print(MY_LIST)
print(my_dict['Assia'])
print(my_dict['Douae'])
if my_dict['Assia' ]==1 or 3 or 9 or 0 or 4:
 MY_LIST1=my_dict['Assia']
print("le 1 er element commun est :",MY_LIST1)
if my_dict['Douae']==1 or 3 or 9 or 0 or 4:
 MY_LIST2=my_dict['Douae']
print("le 2 element commun est :",MY_LIST2)
MY_LIST=[MY_LIST1]+[MY_LIST2]
print("la nouvelle list est :", MY_LIST)