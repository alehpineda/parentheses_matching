# Check for balanced parentheses in an expression (string)

# Function to check parentheses
def check(myString):
    '''
    In every iteration, the innermost parentheses get eliminated (replaced with '').
    If we end up with an empty string, our initial one was balanced or True; otherwise,
    unbalanced or False
    '''
    # if myString is empty return False
    if myString == '':
        return False
    # Lower case the string
    myString = myString.lower()
    # Declare parentheses
    parentheses = [ '()', '{}', '[]']
    # Eliminate characters and numbers
    for e in '1234567890qwertyuiopasdfghjklzxcvbnm+-*/':
        myString = myString.replace(e, '')
    # While any of the elements in parentheses exist in the string
    while any(e in myString for e in parentheses):
        # for each element in the paretheses
        for p in parentheses:
            # replace the parentheses with an empty string
            myString = myString.replace(p, '')
    # return 
    return True if not myString else False
