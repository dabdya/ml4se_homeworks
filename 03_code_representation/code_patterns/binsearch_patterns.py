RECURRENT_BINSEARCH = \
"""{return_type} {function_name}(
    {argument_type} {argument_name}[], {argument_type} key, {argument_type} low, {argument_type} high) {{
    {argument_type} middle = low  + ((high - low) / 2);
    {useless_statement_0}
    if (high < low) {{
        return -1;
    }}
    {useless_statement_1}
    if (key == {argument_name}[middle]) {{
        {useless_statement_2}
        return middle;
    }} else if (key < {argument_name}[middle]) {{
        {useless_statement_3}
        return {function_name}(
          {argument_name}, key, low, middle - 1);
    }} else {{
        {useless_statement_4}
        return {function_name}(
          {argument_name}, key, middle + 1, high);
    }}
}}"""


LOOP_BINSEARCH = \
"""{return_type} {function_name}(
    {argument_type} {argument_name}[], {argument_type} key, {argument_type} low, {argument_type} high) {{
    {return_type} {result_name} = Integer.MAX_VALUE;
    {useless_statement_0}
    while (low <= high) {{
        {argument_type} mid = low  + ((high - low) / 2);
        {useless_statement_1}
        if ({argument_name}[mid] < key) {{
            {useless_statement_2}
            low = mid + 1;
        }} else if ({argument_name}[mid] > key) {{
            {useless_statement_3}
            high = mid - 1;
        }} else if ({argument_name}[mid] == key) {{
            {result_name} = mid;
            {useless_statement_4}
            break;
        }}
    }}
    {useless_statement_5}
    return {result_name};
}}"""

LIBRARY_BINSEARCH = \
"""{return_type} {function_name}({argument_type} {argument_name}[], {argument_type} q) {{
    {useless_statement_0}
    return Arrays.binarySearch({argument_name}, q);
}}"""

ALL = (RECURRENT_BINSEARCH, LOOP_BINSEARCH, LIBRARY_BINSEARCH)
