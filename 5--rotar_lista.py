num = [1,2,3,4,5,6]

def rotar (lst, x):
    guardar = list(lst)
    for i in range(len(lst)):

        if x<0:
            lst[i+x] = guardar[i]
        else:
            lst[i] = guardar[i-x]
        
rotar(num, -5)

print (num)

 
   
 







