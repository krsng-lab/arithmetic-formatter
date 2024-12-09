def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return('Error: Too many problems.')
        return

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if parts[0].isnumeric() and parts[2].isnumeric():
            if len(parts[0]) < 5 and len(parts[2]) < 5:
                if parts[1] == '+':
                    sum = int(parts[0]) + int (parts[2])
                elif parts [1] == '-':
                    sum = int(parts[0]) - int(parts[2])
                else:
                    return("Error: Operator must be '+' or '-'.")
            else: 
                return('Error: Numbers cannot be more than four digits.')
        else:
            return('Error: Numbers must only contain digits.')

        parts = problem.split()
        width = max(len(parts[0]), len(parts[2])) + 2
        first_line.append(f"{parts[0]:>{width}}")
        second_line.append(f"{parts[1]} {parts[2]:>{width-2}}")
        dashes.append('-' * width)
        if show_answers:
            answer = str(eval(problem))
            answers.append(f"{answer:>{width}}")
            
    # Join the lines with spaces
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)
    return arranged_problems
