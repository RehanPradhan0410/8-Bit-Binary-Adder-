
def convertIntoBinary (num):#converts the entered decimal number into 8-bit binary
    #declaring lists to store the number and reversed list
    #declaring a counter to run the while loop 8 times
    bit=[]
    actualBinaryNum=[]
    counter=0

    while (counter!=8):
        remainder=num%2
        bit.append(remainder)
        num=num//2
        counter=counter+1
    #appending the bit list to actualBinaryNum from the last index as the conversion is stored in decending order
    for i in range (len(bit)-1,-1,-1):
        actualBinaryNum.append(bit[i])
    return actualBinaryNum

#Converts the list into a string and returns it 
def listToString(list):
    convertedList = ""

    for i in range(len(list)):
        convertedList = convertedList + str(list[i])
    return convertedList









