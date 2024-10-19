import re
from typing import Dict, Any, List, Union
from dataclasses import dataclass

@dataclass
class Node:
    type: str
    left: Union['Node', None] = None
    right: Union['Node', None] = None
    value: Any = None

def tokenize(rule_string: str) -> List[str]:
    return re.findall(r'\(|\)|AND|OR|[^()\s]+', rule_string)

def parse_condition(tokens: List[str]) -> Node:
    attribute = tokens.pop(0)
    operator = tokens.pop(0)
    value = tokens.pop(0)
    return Node(type="operand", value={"attribute": attribute, "operator": operator, "value": value})

def parse_expression(tokens: List[str]) -> Node:
    if tokens[0] == '(':
        tokens.pop(0)  # Remove opening parenthesis
        left = parse_expression(tokens)
        op = tokens.pop(0)
        right = parse_expression(tokens)
        tokens.pop(0)  # Remove closing parenthesis
        return Node(type="operator", value=op, left=left, right=right)
    else:
        return parse_condition(tokens)

def create_rule(rule_string: str) -> Node:
    tokens = tokenize(rule_string)
    return parse_expression(tokens)

def combine_rules(rules: List[str]) -> Node:
    if not rules:
        raise ValueError("No rules provided")
    if len(rules) == 1:
        return create_rule(rules[0])

    combined_ast = create_rule(rules[0])
    for rule in rules[1:]:
        new_ast = create_rule(rule)
        combined_ast = Node(type="operator", value="AND", left=combined_ast, right=new_ast)

    return combined_ast

def evaluate_node(node: Node, data: Dict[str, Any]) -> bool:
    if node.type == "operand":
        attribute = node.value["attribute"]
        operator = node.value["operator"]
        value = node.value["value"]

        if attribute not in data:
            raise ValueError(f"Attribute '{attribute}' not found in data")

        if operator == "=":
            return data[attribute] == value
        elif operator == ">":
            return data[attribute] > float(value)
        elif operator == "<":
            return data[attribute] < float(value)
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_node(node.left, data) and evaluate_node(node.right, data)
        elif node.value == "OR":
            return evaluate_node(node.left, data) or evaluate_node(node.right, data)
        else:
            raise ValueError(f"Unsupported operator: {node.value}")

def evaluate_rule(ast: Node, data: Dict[str, Any]) -> bool:
    return evaluate_node(ast, data)
