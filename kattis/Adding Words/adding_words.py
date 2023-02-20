# Jacobus Burger (2023)
# Adding Words

# this is a matter of simulation
variables = {}  # name: value
while True:
    try:
        command = input().split()
    except:
        # EOF
        break
    if command[0] == "def":
        # define variables in variable table
        variables[command[1]] = int(command[2])
    if command[0] == "calc":
        # calculate answer
        equation = command[1:-1]
        equation = [str(variables[token]) if token in variables else token for token in equation]
        try:
            solution = eval(' '.join(equation))
            if solution in variables.values():
                answer_variable = list(variables.keys())[list(variables.values()).index(solution)]
                print(' '.join(command[1:]), answer_variable)
            else:
                print(' '.join(command[1:]), "unknown")
        except:
            print(' '.join(command[1:]), "unknown")
    if command[0] == "clear":
        # clear variables
        variables = {}
