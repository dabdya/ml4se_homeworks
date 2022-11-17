import random
import re


USELESS_STATEMENTS = [
    "",
    "long item_ = 4;", 
    "string greet_ = \"hello world\";",
    "int variable_ = 45 + 96;",
    "int nums_[] = new int[4];",
    "boolean b1_ = Boolean.parseBoolean(\"true\");",
    "StringBuilder sb = new StringBuilder();",
    ""
]


class CodeFormatter:
    def __init__(self) -> None:
        self.mappings = dict(
            function_name = ("factorial", "f", "sort", "s"),
            argument_name = ("n", "number", "arr", "a"),
            return_type = ("int", "long"),
            argument_type = ("int", "long"),
            result_name = ("result", "res", "r"),
            lambda_expr = (
                "(long x, long y) -> x * y",
                "(int lhs, int rhs) -> lhs * rhs"
            )
        )
        
        useless_statements_dict = {
            f"useless_statement_{i}": USELESS_STATEMENTS 
            for i in range(len(USELESS_STATEMENTS))
        }
        
        self.mappings.update(useless_statements_dict)
    
    def format(self, pattern: str) -> str:
        placeholders = set(re.findall("{([\w\d]+)}", pattern))
        
        map_ = {
            k: random.choice(v)
            for k, v in self.mappings.items() if k in placeholders
        }
        
        return pattern.format(**map_)
