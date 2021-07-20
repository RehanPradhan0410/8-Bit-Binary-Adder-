def binaryAddition (a,b):#Adds two 8-bit binary numbers
    #crating list to store the addition, to store reversed addition and for carryin
    addition=[]
    revAddition=[]
    c=[0,0,0,0,0,0,0,0]
    for i in range (7,-1,-1):
        sum=a[i] ^ b[i] ^ c[i]
        c[i-1]=(c[i] & (a[i] ^ b[i])) | (a[i] & b[i])
        addition.append(sum)

    #appending the elements of list addition into another list revAddition from the last index as the addition is stored in decending order
    for i in range (len(addition)-1,-1,-1):
        revAddition.append(addition[i])
    return revAddition

def display (a,b,List): # displays the added binary as well as the converted numbers
    
    for value in a:
        print (value,end="")

    print("")
    for value in b:
        print (value,end="")
    print("")
    print("+")
    print("---------")
    
    
    for value in List:
        print (value,end="")

    print("")
        


