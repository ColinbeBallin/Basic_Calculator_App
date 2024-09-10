print("Choose an operation: ")
print("a) Addition")
print("b) Subtraction")
print ("c) Multipication")
print("d) Division")
operation = input()
print("Type your first number: ")
first_num = int(input())
print("Type your second number: ")
second_num = int(input())
if operation == "a":
    answer = first_num + second_num
elif operation == "b":
    answer = first_num - second_num
elif operation == "c":
    answer = first_num * second_num
elif operation == "d":
    answer = first_num / second_num
else:
    print("Error, please pick the correct letter")

print(answer)
