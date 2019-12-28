KEYWORDS = ["class", "constructor", "function", "method", "field", "static", "var", "int", "char", "boolean", "void",
            "true", "false", "null", "this", "let", "do", "if", "else", "while", "return"]

SYMBOL = ["\(", "\)", "{", "}", "\[", "\]", "\.", ",", ";", "\+", "-", "\*", "\/", "&", "\|", "<", ">", "=", "~"]

VAR_TYPES = ["int", "char", "boolean", "void"]

SUB_ROUTINES = ["constructor", "function", "method"]

CLASS_VARS = ["field", "static"]

STATEMENTS = ["let", "do", "if", "while", "return"]

OP = ["+", "-", "*", "/", "&", "|", "<", ">", "="]

CONST_KW = ["true", "false", "null", "this"]

REG_STRING = "\\\"[^\\\"]*\\\""

REG_VAR_NAME = "[_a-zA-Z][\\w]*"

REG_NUMBER = "[\\d]+"

GROUP_DICT = {1: "stringConstant", 2: "keyword", 3: "symbol", 4: "identifier", 5: "integerConstant"}

HTML_TRANSLATOR = {"<": "&lt", ">": "&gt", "\"": "&quot", "&": "&amp"}

def regex_builder():
    reg = "(" + REG_STRING + ")"
    reg += "|("
    for key in KEYWORDS:
        reg += "\\b" + key + "\\b|"
    reg = reg[:-1] + ")|("
    for symbol in SYMBOL:
        reg += symbol + "|"
    reg = reg[:-1] + ")|(" + REG_VAR_NAME + ")|(" + REG_NUMBER + ")"
    return reg

def is_string_const(s):
    if s[0] == "\"" and s[-1] == "\"":
        return True
    else:
        return False


def is_identifier(s):
    if s[0] != "\"" and s[-1] != "\"":
        if s[0].isdigit():
            return False
        else:
            return True


def is_symbol(s):
    if s in SYMBOL:
        return True
    else:
        return False


def is_keyword(s):
    if s in KEYWORDS:
        return True
    else:
        return False
