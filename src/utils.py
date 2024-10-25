"""import json
import json
from rule_engine import ASTNode

# Convert AST to JSON (for saving in DB)
def ast_to_json(ast):
    if ast is None:
        return None
    return {
        "type": ast.type,
        "left": ast_to_json(ast.left),
        "right": ast_to_json(ast.right),
        "value": ast.value
    }

# Convert JSON to AST (for loading from DB)
def json_to_ast(ast_json):
    if ast_json is None:
        return None
    return Node(
        type=ast_json['type'],
        left=json_to_ast(ast_json['left']),
        right=json_to_ast(ast_json['right']),
        value=ast_json['value']
    )
    """

