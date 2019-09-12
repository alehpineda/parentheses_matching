# Check for balanced parentheses in an expression (string)

# Function to check parentheses
def check(myString):
    '''
    Each time, when an open parentheses is encountered push it in the stack,
    and when closed parenthesis is encountered, match it with the top of stack
    and pop it. if stack is empty at the end, return Balanced otherwise, Unbalanced.
    '''

    # Declare open and close parentheses
    open_parenthesis = [ '[', '{', '(']
    close_parenthesis = [ ']', '}', ')']

    # Empty stack
    stack = []
    # For each element in myString
    for e in myString:
        # If element is in open_parenthesis
        if e in open_parenthesis:
            # append to the stack
            stack.append(e)
        # Else if elemente is in close_parenthesis
        elif e in close_parenthesis:
            # position equals the element index in close_parenthesis
            position = close_parenthesis.index(e)
            # If the size of the stack is greather than 0 and
            # the open_parenthesis equals the last parenthesis in the stack
            if ((len(stack) > 0) and (open_parenthesis[position] == stack[len(stack) - 1])):
                # Remove it from the stack
                stack.pop()
            else:
                # Return "Unbalanced"
                return "Unbalanced"
    # If the stack is empty
    if len(stack) == 0:
        # Return "Balanced"
        return "Balanced"

# Testing the code
string_01 = "{[]{()}}"
print(string_01, '-', check(string_01))

string_02 = "[{}{})(]"
print(string_02, '-', check(string_02))

string_03 = "{([}()])"
print(string_03, '-', check(string_03))

string_04 = "{([]())}"
print(string_04, '-', check(string_04))