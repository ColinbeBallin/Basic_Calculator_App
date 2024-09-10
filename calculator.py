print("Choose an operation: ")
print("a) Addition")
print("b) Subtraction")
print ("c) Multipication")
print("d) Division")
operation = input()
   
print("Type your first  number: ")
first_num = int(input())

print("Type a number: ")
next_num = float(input())


wish = "y"
while wish == "y":
    
    if operation == "a":
        answer = first_num + next_num
        first_num = answer
    elif operation == "b":
        answer = first_num - next_num
        first_num = answer
    elif operation == "c":
        answer = first_num * next_num
        first_num = answer
    elif operation == "d":
        answer = first_num / next_num
        first_num = answer
    else:
        print("Error, please pick the correct letter")
   
    print("Here is your answer : " + str(first_num))

    print("Do you wish to continue? (y/n)")
    wish = input()
    if wish == "n":
        print("Your final answer is: "+ str(first_num))
        print("Yippeee, hope you come again!!!")
    elif wish == "y":
        
        print("Choose an operation: ")
        print("a) Addition")
        print("b) Subtraction")
        print ("c) Multipication")
        print("d) Division")
        operation = input()
        print("Type your next number: ")
        next_num = int(input())

   
