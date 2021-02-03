# numberOne = int(input("What is the first number? "))
# numberTwo = int(input("What is the second number? "))
# operator = input("What mathematical operation do you want to perform? ")



# if operator == '+':
#     print(numberOne + numberTwo)
# elif operator == '-':
#     print(numberOne - numberTwo)
# elif operator == '/':
#     print(numberOne / numberTwo)
# else:
#     print(numberOne * numberTwo)

with open("C:/Users/RICHARD.DALLMAN/Desktop/DevOpsAcademy/Module1/Workshop//calc.txt", mode="r") as f:
    text_string = f.read().splitlines()
    result = 0
    for text in text_string:
        line = text.split()
        operator = line[1]
        numberOne = int(line[2])
        numnberTwo = int(line[3])
        if operator == 'x':           
            result += (numberOne * numnberTwo)
            # print(numberOne * numnberTwo)
        elif operator == '/':
            result += (numberOne / numnberTwo)
            print(numberOne / numnberTwo)
        elif operator == '+':
            result += (numberOne + numnberTwo)
            print(numberOne + numnberTwo )
        elif operator == '%':
            result += (numberOne % numnberTwo)
            print(numberOne % numnberTwo)
        elif operator == "^":
            result += (numberOne ^ numnberTwo)
            print(numberOne ^ numnberTwo)
        else:
            result = result + (numberOne - numnberTwo)
            print(numberOne - numnberTwo)

        # print(line)
    # print(text_string)
    print("result: " + str(result))
    f.close()


# def divide(number_one, number_two):
#     return int(number_one // number_two)

# def add(number_one, number_two):
#     return int(number_one / number_two)

# def multiply(number_one, number_two):
#     return int(number_one * number_two)

# def substract(number_one, number_two):
#     return int(number_one - number_two)


# with open("C:/Users/RICHARD.DALLMAN/Desktop/DevOpsAcademy/Module1/Workshop//goto.txt", mode="r") as f:
#     text_string = f.read().splitlines()
#     statements = []
#     for text in text_string:
#         line_number = 0
#         current_statement = text
        
#         line = text.split()
#         statements.append(line)
#         if(len(line) == 2):
#             # f.readline(line[1])     
#             line_number = int(line[1])
#             f.readline(line_number)
#             continue
#         else:
#             number_one = int(line[3])
#             nummber_two = int(line[4])
#             operator = line[2]
#             if operator == '+':
#                 line_number = add(number_one, nummber_two)
#             elif operator == '-':
#                 line_number = substract(number_one, nummber_two)
#             elif operator == '/':
#                 line_number = divide(number_one, nummber_two)
#             else:
#                 line_number = multiply(number_one, nummber_two)
#             f.readline(line_number)
            
#             if (current_statement in statements):
#                 print("statement found before " + str(line_number))
#                 break
#             else:
#                 statements.append(current_statement)
#     f.close()