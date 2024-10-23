# ast_engine.py

class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left            # Left child node
        self.right = right          # Right child node
        self.value = value          # Value for operand nodes, e.g., 'age > 30'

    def __repr__(self):
        return f"ASTNode({self.node_type}, {self.value})"

# Function to parse rule string into AST
def create_rule(rule_string):
    tokens = rule_string.split(" ")
    stack = []

    for token in tokens:
        if token.upper() in ['AND', 'OR']:
            right = stack.pop()
            left = stack.pop()
            stack.append(ASTNode("operator", left, right, token))
        else:
            stack.append(ASTNode("operand", value=token))

    return stack.pop()

# Function to combine rules
def combine_rules(rules):
    combined_ast = None

    for rule in rules:
        rule_ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = rule_ast
        else:
            combined_ast = ASTNode("operator", combined_ast, rule_ast, "AND")

    return combined_ast

# Function to evaluate AST against user data
def evaluate_rule(ast, user_data):
    if ast.node_type == "operand":
        return evaluate_condition(ast.value, user_data)
    elif ast.node_type == "operator":
        left_result = evaluate_rule(ast.left, user_data)
        right_result = evaluate_rule(ast.right, user_data)

        if ast.value.upper() == "AND":
            return left_result and right_result
        elif ast.value.upper() == "OR":
            return left_result or right_result

    return False

def evaluate_condition(condition, data):
    parts = condition.split(" ")
    attribute, operator, value = parts[0], parts[1], int(parts[2])
    user_value = int(data.get(attribute, 0))

    if operator == '>':
        return user_value > value
    elif operator == '<':
        return user_value < value
    elif operator == '==' or operator == '=':
        return user_value == value
    return False
