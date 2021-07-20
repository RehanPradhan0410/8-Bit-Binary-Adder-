#Importing all the necessary function files
import checkRange
import conversion
import BinaryAddition

#Declaring lists and boolean variables
firstConvertedNumber=[]
secondConvertedNumber=[]
addedBinary=[]
continueInput=True
checkingRange=False



def main():
    #This Function will run until continueInput is True
    while (continueInput==True):
        try:
            print("")
            print("---------------------******WELCOME TO THE PROGRAM******---------------------")
            print("")
            
            #Taking The Input and Checking The Range of The First Number and Then Converting The Decimal Number Into Binary 
            inputNum1=int(input("Enter First Decimal number: "))
            checkingRange=checkRange.checkNumberRange(inputNum1)#Checks the range of the input number by calling a function which returns a boolean value

            while (checkingRange==True):
                print("")
                inputNum1=int(input("Please Input The First Decimal Number In The Range of 0 to 255: "))
                checkingRange=checkRange.checkNumberRange(inputNum1)
            firstConvertedNumber=conversion.convertIntoBinary(inputNum1)#Converting the decimal number into 8-bit binary number
            displayingConverted1=conversion.listToString (firstConvertedNumber)#Turning the firstConvertedNumber List into a string

            
            #Taking The Input and Checking The Range of The Second Number and Then Converting The Decimal Number Into Binary
            print("")
            inputNum2=int(input("Enter Second Decimal Number: "))
            print("")
            checkingRange=checkRange.checkNumberRange (inputNum2) #Checks the range of the input number by calling a function which returns a boolean value

            while (checkingRange==True):
                 print ("")
                 inputNum2=int(input("Please Input The Second Decimal Number In The Range of 0 to 255: "))
                 checkingRange=checkRange.checkNumberRange(inputNum2)
            secondConvertedNumber=conversion.convertIntoBinary (inputNum2) #Converting the decimal number into 8-bit binary number
            displayingConverted2=conversion.listToString (secondConvertedNumber)#Turning the secondConvertedNumber List into a string

            if (inputNum1 + inputNum2>255): # checking if the operation exceeds 8-bit operation or not
                print ("You Have Entered Values For 9-Bit operation!!! This Program is For 8-bit Binary Addition Only!!! ")
            else:
                #Displaying The Converted Numbers
                print("The First Decimal Number",inputNum1,"Has Been Converted Into Binary ("+displayingConverted1+")2")
                print("")
                print("The Second Decimal Number",inputNum2,"Has Been Converted Into Binary ("+displayingConverted2+")2")
                print ("")
                print ("The Sum Of These Converted Binary Is:-")
                print ("")

                #Adding The Converted Numbers and Displaying It
                addedBinary=BinaryAddition.binaryAddition(firstConvertedNumber,secondConvertedNumber)
                BinaryAddition.display (firstConvertedNumber,secondConvertedNumber,addedBinary)
            
            
        #Works When User Input Anything Rather Than Integer Value
        except:
            print("")
            print("The Program Accepts Only Integer Values As Input!")

        print("")    
        print("If You Want To Run The Program Again Type (Yes) | If You want To Exit The Program Type (No)")
        print("")
        #Restarting The Program Accourding To The Command of The User
        runAgain=input("Answer: ")
        print("")
        if (runAgain=='No' or runAgain=='no' or runAgain=='NO'):
            print ("--------------------------------------------------------------")
            print("Thank You For Using The Program! Have A Nice Day Ahead!!!")
            print("---------------------------------------------------------------")
            break

main()
    
    
        

