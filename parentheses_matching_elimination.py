# Check for balanced parentheses in an expression (string)

# Function to check parentheses
def check(myString):
    '''
    In every iteration, the innermost parentheses get eliminated (replaced with '').
    If we end up with an empty string, our initial one was balanced; otherwise,
    unbalanced
    '''
    # Declare parentheses
    parentheses = [ '()', '{}', '[]']
    # While any of the elements in parentheses exist in the string
    while any(e in myString for e in parentheses):
        # for each element in the paretheses
        for p in parentheses:
            # replace the parentheses with an empty string
            myString = myString.replace(p, '')
    # return 
    return "Balanced" if not myString else "Unbalanced"

def checkReturn(myString):
    return "Balanced" if check(myString) else "Unbalanced"

# Testing the code
string_01 = "{[]{()}}"
print(string_01, '-', check(string_01))

string_02 = "[{}{})(]"
print(string_02, '-', check(string_02))

string_03 = "{([}()])"
print(string_03, '-', check(string_03))

string_04 = "{([]())}"
print(string_04, '-', check(string_04))
