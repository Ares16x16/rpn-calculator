operators = set(['+', '-', '*', '/', '**'])
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_syntax_tree(expression):
    def has_precedence(op1, op2):
        if op2 in operators and precedence[op1] <= precedence[op2]:
            return True
        return False

    def apply_operator(operator, stack):
        right = stack.pop()
        left = stack.pop()

        node = Node(operator)
        node.left = left
        node.right = right

        stack.append(node)

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    stack = []
    output = []

    try:
        for token in tokens:
            if token.isdigit():
                output.append(Node(int(token)))
            elif token in operators:
                while stack and stack[-1].value in operators and has_precedence(token, stack[-1].value):
                    apply_operator(stack.pop().value, output)
                stack.append(Node(token))
            elif token == '(':
                stack.append(Node(token))
            elif token == ')':
                while stack and stack[-1].value != '(':
                    apply_operator(stack.pop().value, output)
                stack.pop()

        while stack:
            apply_operator(stack.pop().value, output)

        return output[0]

    except (ValueError, IndexError):
        raise ValueError("Invalid expression")



def evaluate_syntax_tree(node):
    if node.left is None and node.right is None:
        return node.value

    left_result = evaluate_syntax_tree(node.left)
    right_result = evaluate_syntax_tree(node.right)

    try:
        if node.value == '+':
            return left_result + right_result
        elif node.value == '-':
            return left_result - right_result
        elif node.value == '*':
            return left_result * right_result
        elif node.value == '/':
            return left_result / right_result
        elif node.value == '**':
            return left_result ** right_result
    except:
        print("Math Error")
        quit()


def calculate_expression(expression):
    try:
        syntax_tree = build_syntax_tree(expression)
        result = evaluate_syntax_tree(syntax_tree)
        return result
    except ValueError as e:
        print("Error:", str(e))

def add_spaces(expr, operators):
    i = 0
    while i < len(expr):
        # Handle special case **
        if expr[i] == '*':
            if i + 1 < len(expr) and expr[i+1] == '*':
                expr = expr[:i] + ' ** ' + expr[i+2:]
                i += 3
            else:
                expr = expr[:i] + ' * ' + expr[i+1:]
                i += 2
        elif expr[i] in operators:
            expr = expr[:i] + ' ' + expr[i] + ' ' + expr[i+1:]
            i += 3
        else:
            i += 1
    return expr

def evaluate_rpn(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '**'])

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid expression: insufficient operands")
            
            right_operand = stack.pop()
            left_operand = stack.pop()

            if token == '+':
                result = left_operand + right_operand
            elif token == '-':
                result = left_operand - right_operand
            elif token == '*':
                result = left_operand * right_operand
            elif token == '/':
                result = left_operand / right_operand
            elif token == '**':
                result = left_operand ** right_operand

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid expression: too many or too few operands")

    return stack.pop()


def convert_to_rpn(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
    stack = []
    output = []

    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            
            if not stack:
                raise ValueError("Invalid expression: mismatched parentheses")
            
            stack.pop()
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            
            stack.append(token)

    while stack:
        if stack[-1] == '(':
            raise ValueError("Invalid expression: mismatched parentheses")
        output.append(stack.pop())

    return ' '.join(output)


def calculate_expression_rpn(expression):
    try:
        rpn_expression = convert_to_rpn(expression)
        print(f"RPN expression: {rpn_expression}")
        result = evaluate_rpn(rpn_expression)
        return result
    except ValueError as e:
        print("Error:", str(e))
        
expression = "1**3**5*4/4+6**2" # No bracket for RPN
spaced_expression = add_spaces(expression,operators)
print(f"Expression: {spaced_expression}")

#Syntax Tree
result = calculate_expression(spaced_expression)
print(f"Result: {result}")

#RPN
result = calculate_expression_rpn(spaced_expression)
print(f"Result: {result}")
