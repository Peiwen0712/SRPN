 #Coursework 1: SRPN
import random

stack = []
SRPN_MIN = -2147483648
SRPN_MAX = 2147483647

#t-saturation
MAX_SIZE = 23 


#calc part
def process_calc_command(command):
    if command.strip() == '#':
        return None

    result = None

    if command == "=":
        result = stack[-1]
    elif command == '-':
        if len(stack) < 2:
            result = "Stack underflow."
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)
    elif command == '+':
        if len(stack) < 2:
            result = "Stack underflow."
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
    elif command == '*':
        if len(stack) < 2:
            result = "Stack underflow."
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
    elif command == '/':
        if len(stack) < 2:
            result = "Stack underflow."
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            # t-obscure
            if num1 == 0:
                stack.append(num2)
                stack.append(num1)
                result = "Divide by 0."
            else:
                stack.append(num2 // num1)
    elif command == '%':
        if len(stack) < 2:
            result = "Stack underflow."
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 % num1)
    elif command == '^':
        if len(stack) < 2:
            result = "Stack underflow."
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            # t-multiple/05
            if num1 < 0:
                stack.append(num2)
                stack.append(num1)
                result = "Negative power."
            else:
                stack.append(num2 ** num1)


    elif command == 'd':
        result = "\n".join([str(x) for x in stack])
  
    elif command.isdigit() or (command[1:].isdigit() and command[0] == '-'):
        if len(stack) == MAX_SIZE:
            result = "Stack overflow."
        else:
            stack.append(int(command))

    elif command == 'r':
        if len(stack) == MAX_SIZE:
            result = "Stack overflow."
        else:
            random_num = random.randint(SRPN_MIN, SRPN_MAX)
            stack.append(random_num)
    else:
        for character in command:
            if not character.isalpha():
                stack.clear()
                continue

            if len(stack) == MAX_SIZE:
                result = "Stack overflow."
                break
            else:
                stack.append(0)

    if stack:
        if stack[-1] < SRPN_MIN:
            stack[-1] = SRPN_MIN
        if stack[-1] > SRPN_MAX:
            stack[-1] = SRPN_MAX


    return result

#Obscure functionality
def process_command(command):
    command = remove_hash(command).strip()
    result = None

    if ' ' in command:
        input = command.strip().split()
        for character in input:
            if  character[1:].isdigit() or character.isdigit():
                result = process_calc_command(character)
            else:
                for x in character:
                    result = process_calc_command(character)                
    else:
        result = process_calc_command(command)

    return result

def remove_hash(command):
    after_remove = ''
    for character in command:
        if character == '#':
            break
        after_remove += character

    if after_remove.strip() == '':
        after_remove = '#'
    return after_remove

#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__": 
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()
