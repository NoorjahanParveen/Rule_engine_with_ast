import json

class ASTNode:
    def __init__(self, rule):
        self.rule = rule
        self.children = []

    def to_json(self):
        return {'rule': self.rule, 'children': [child.to_json() for child in self.children]}

class RuleEngine:
    @staticmethod
    def create_ast(rule_string):
        # Basic logic to create AST from rule string
        # You can implement a more sophisticated parser if needed
        return ASTNode(rule_string)

    @staticmethod
    def combine_asts(rule_strings):
        combined_node = ASTNode('Combined Rules')
        for rule in rule_strings:
            ast_node = RuleEngine.create_ast(rule.strip())
            combined_node.children.append(ast_node)
        return combined_node

    @staticmethod
    def evaluate_rule(user_data, rule_string):
        # Simple evaluation of user_data against a rule_string
        # Splitting by logical operators (AND, OR)
        conditions = rule_string.split(" OR ")
        results = []

        for condition in conditions:
            sub_conditions = condition.split(" AND ")
            sub_results = []
            for sub_condition in sub_conditions:
                # Assuming the condition format is "attribute operator value"
                attribute, operator, value = sub_condition.strip().split(" ")
                value = float(value) if '.' in value else int(value)

                if operator == ">":
                    sub_results.append(user_data[attribute] > value)
                elif operator == "<":
                    sub_results.append(user_data[attribute] < value)
                elif operator == "==":
                    sub_results.append(user_data[attribute] == value)
                elif operator == ">=":
                    sub_results.append(user_data[attribute] >= value)
                elif operator == "<=":
                    sub_results.append(user_data[attribute] <= value)
                # Add more operators as needed

            # Combine sub_results with AND logic
            results.append(all(sub_results))

        # Combine results with OR logic
        return any(results)
