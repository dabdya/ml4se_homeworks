RECURRENT_FACTORIAL = \
"""{return_type} {function_name}({argument_type} {argument_name}) {{
    {useless_statement_0}
    if ({argument_name} == 0) {{
        {useless_statement_1}
        return 1; 
    }} else {{
        {useless_statement_2}
        return {argument_name} * {function_name}({argument_name}-1);
    }}
}}"""

RECURRENT_TERNARY_FACTORIAL = \
"""{return_type} {function_name}({argument_type} {argument_name}) {{
    {useless_statement_0}
    return {argument_name} == 0 ? 1 : {argument_name} * {function_name}({argument_name}-1);
}}"""

LOOP_FACTORIAL = \
"""{return_type} {function_name}({argument_type} {argument_name}) {{
    {useless_statement_0}
    {return_type} {result_name} = 1;
    {useless_statement_1}
    for (int i = 1; i <= {argument_name}; i++) {{
        {useless_statement_2}
        {result_name} = {result_name} * i;
    }}
    {useless_statement_3}
    return {result_name};
}}"""

STREAM_FACTORIAL = \
"""{return_type} {function_name}({argument_type} {argument_name}) {{
    {useless_statement_0}
    return LongStream.rangeClosed(1, {argument_name}).reduce(1, {lambda_expr});
}}"""

ALL = (RECURRENT_FACTORIAL, RECURRENT_TERNARY_FACTORIAL, LOOP_FACTORIAL, STREAM_FACTORIAL)
