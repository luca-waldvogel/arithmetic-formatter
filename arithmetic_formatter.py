def find_first_number(problems):
    first_number = []
    for problem in problems:
        number = ''
        for char in problem:
            if char in ' +-':
                break
            number += char
        first_number.append(number)
    return first_number

def find_second_number(problems):
    second_number = []
    for problem in problems: 
        problem_reverted = problem[::-1]
        number = ''
        for char in problem_reverted:
            if char in ' +-':
                break
            number += char
        second_number.append(number[::-1])
    return second_number

def find_operators(problems):
    operators = []
    for problem in problems:
        operator = ''
        for char in problem:
            if char in '+-*/':
                operator += char
                operators.append(operator)
    return operators

def find_length(first_number, second_number):
    length = []
    for i in range(len(first_number)):
        length += str(max(len(first_number[i]), len(second_number[i])) + 2)
    return length

def find_answer(first_number, second_number, operators):
    answers = []
    for i in range(len(first_number)):
        if operators[i] == '+':
            answer = int(first_number[i]) + int(second_number[i])
        elif operators[i] == '-':
            answer = int(first_number[i]) - int(second_number[i])
        else:
            pass
        answers.append(str(answer))
    return answers

def find_error(problems, first_number, second_number, operators):
    for i in range(len(problems)):
        if len(problems) > 4:
            error = 'Error: Too many problems.'
        elif operators[i] not in '+-':
            error = "Error: Operator must be '+' or '-'."
        elif not first_number[i].isdigit():
            error = 'Error: Numbers must only contain digits.'
        elif len(first_number[i]) > 4 or len(second_number[i]) > 4:
            error = 'Error: Numbers cannot be more than four digits.'
        else:
            error = None
    return error

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
            error = 'Error: Too many problems.'
            return error
    first_number = find_first_number(problems)
    for number in first_number:
        if not number.isdigit():
            error = 'Error: Numbers must only contain digits.'
            return error
        elif len(number) > 4:
            error = 'Error: Numbers cannot be more than four digits.'
            return error
        
    second_number = find_second_number(problems)
    for number in second_number:
        if not number.isdigit():
            error = 'Error: Numbers must only contain digits.'
            return error
        elif len(number) > 4:
            error = 'Error: Numbers cannot be more than four digits.'
            return error
    operators = find_operators(problems)
    for operator in operators:
        if operator in '*/':
            error = "Error: Operator must be '+' or '-'."
            return error
    length = find_length(first_number, second_number)
    answer = find_answer(first_number, second_number, operators)
    solution = ''
    
    #first_row
    for i in range(len(first_number)):
        first_row = ''
        for j in range(int(length[i])-len(first_number[i])):
            first_row += ' '
        first_row += first_number[i]
        if i == (len(first_number)-1):
            pass
        else:
            first_row += '    ' 
        solution += first_row
    solution += '\n'

    #second_row
    for i in range(len(second_number)):
        second_row = ''
        second_row += operators[i]
        for j in range(int(length[i])-len(second_number[i])-1):
            second_row += ' '
        second_row += second_number[i]
        if i == (len(second_number)-1):
            pass
        else:
            second_row += '    ' 
        solution += second_row
    solution += '\n'

    #third_row
    for i in range(len(length)):
        third_row = ''
        j = 1
        while j <= int(length[i]):
            third_row += '-'
            j += 1
        if i == (len(length)-1):
            pass
        else:
            third_row += '    ' 
        solution += third_row
    
    #optional_answer_row
    if show_answers:
        solution += '\n'
        for i in range(len(answer)):
            optional_answer_row = ''
            for j in range(int(length[i])-len(answer[i])):
                optional_answer_row += ' '
            optional_answer_row += answer[i]
            if i == (len(first_number)-1):
                pass
            else:
                optional_answer_row += '    ' 
            solution += optional_answer_row
    
    return solution

print(f'{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
