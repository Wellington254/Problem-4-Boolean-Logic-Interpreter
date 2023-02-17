
#syntax_parser is a dictionary that maps symbols to Python boolean operators.

while True:
    user_exp=input('enter boolean expression to evaluate\n')

    templist=[*user_exp]
    l=len(templist)
    
    for b in range(len(templist)):
        if templist[b]== 'T':
            templist[b]=True

    for c in range(len(templist)):
        if templist[c]== 'F':
            templist[c]=False

    for i in range(len(templist)-1):
        if templist[i]== '~':
            
            right_not=templist[i+1]
            templist[i+1]= not right_not
            del templist[i]
    

    for j in range(len(templist)-1):
        if templist[j]== '.':
            right_of_and=templist[j+1]
            left_of_and=templist[j-1]
            templist[j+1]=left_of_and and right_of_and
            templist[j]=0
            templist[j-1]=0
        
    for k in range(len(templist)-1):
        if templist[k]== '+':
            right_of_or=templist[k+1]
            left_of_or=templist[k-1]
            templist[k+1]=left_of_or or right_of_or
            templist[k]=0
            templist[k-1]=0

    print(templist[len(templist)-1])




