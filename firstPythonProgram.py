name = "Bluecookies" # ===== string ======
firstName = "blue" 
age = 19 # ==== string ====
ageAsAString = "19" # ==== interger ====
bankAccountBalance = 39039.21 

# ====== displaying the values of the 3 variables above ======
print ( name, age, bankAccountBalance )
# ============================================================

# ======================= Operators ==========================
firstNumber = 18
secondNumber = 10

print ( firstNumber, secondNumber, 78, "Another String", sep="---", end="THE END" )
print ("Line 2", end="Line 2 end" )
print ( "This exist" )
# ============================================================

# ==================== Input and Output ======================
userName = input ( " Enter your name: ")

print ( "You typed in", userName )
# ============================================================

# =================== Decision structures =====================
userAge = 21

if userAge < 21:
    print ( "You are too y" )
    print ( "You are too yo" )
    print ( "You are too you" )
    print ( "You are too youn" )
    print ( "You are too young" )

elif userAge < 30:
    print ( "Your age is between 20 and 31" )
elif userAge < 40: 
    print ( "Your age is between 31 and 50" )
if userAge == 21:
    print ( "You are the right age, congrats!" )
else:
    print ( "W h a t" )
# ============================================================

# =================== Logical Operators ======================

REQUIRED_MONEY = 40
REQUIRED_AGE = 21

userAge = 17 
userMoney = 100

if userAge < REQUIRED_AGE or userMoney < REQUIRED_MONEY:
    print ( "Get out before I call the cops" )
else:
    print ( "Welcome, enjoy the party!" )
# ============================================================

# ========================== Loops ===========================
userAge = 1 

for currentNumber in range( 1, 31 ): # 1 to  30
    if currentNumber == 10:
        break
    
    print ( currentNumber )
# ======================= Display Math  ======================
def displayMath():
    print ( "The sum of 2 + 2 = 4" ) 

def displayMathAdvanced( firstNumber, secondNumber ):
    answer = firstNumber + secondNumber 
    print ( "The sum of", firstNumber, "and", secondNumber, "is", answer)

def displayMathSuperAdvance( firstNumber, secondNumber, thirdNumber ):
    difference = firstNumber - secondNumber - thirdNumber 
    return difference 


def applyBasicCalculations( firstNumber, secondNumber ):
    sum = firstNumber + secondNumber 
    difference = firstNumber - secondNumber 
    product = firstNumber * secondNumber 
    sum = firstNumber + secondNumber 

    return sum, difference, product, quotient 

def main():
    sum, differenceOutsideOfFuction, product, quotientRecieved = applyBsicCalculations ( 4,2 )
    print ( sum, differenceOutsideOfFuction, product, quotientRecieved )

main()

#displayMath ()   

#displayMathAdvance( 5,89 )

superAdvanceDifference = displayMathSuperAdvance( 10,2,4 )
print ( superAdvanceDifference )
# ============================================================

from multiprocessing.sharedctypes import Value 

def main():
    testFile = open( "testFile.txt", "w" )

    testFile.write( str( 2 ) + "\n" )
    testFile.write( str( 4 ) + "\n" )
    testFile.write( str( 6 ) + "\n" )
    testFile.write( str( 8 ) + "\n" )

def main ():
    testFile = open ( "testFile.txt", "r" )

    line = testFile.readline()
    line = line.rstrip("\n")

    while line !="":
        print( line )
        line = testFile.readline().rstrip("\n")

        testFile.close()

main()

from multiprocessing.sharedctypes import Value 

def main():
    try:
        testFile = open( "testFile.txt", "r" )

        line = testFile.readline()
        line = line.rstrip ("\n")

        while line !="":
            print ( line )
            line = testFile.readline().rstrip("\n")
    expect Exception as potential Error:
        print ( potentialError )
    else:
        print( "All system functioning" )
    finally:
        testFile.close()
        print( "End the program" )
    
main()
