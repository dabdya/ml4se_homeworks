BUBBLE_SORT = \
"""{return_type} {function_name}({argument_type} {argument_name}[]) {{
    int n = {argument_name}.length;
    {useless_statement_0}
    for (int i = 0; i < n - 1; i++) {{
        {useless_statement_1}
        for (int j = 0; j < n - i - 1; j++) {{
            if ({argument_name}[j] > {argument_name}[j + 1]) {{
                {argument_type} temp = {argument_name}[j];
                {useless_statement_2}
                {argument_name}[j] = {argument_name}[j + 1];
                {useless_statement_3}
                {argument_name}[j + 1] = temp;
            }}
        }}
        {useless_statement_4}
    }}
}}"""

INSERTION_SORT = \
"""{return_type} {function_name}({argument_type} {argument_name}[]) {{
    int n = {argument_name}.length;
    {useless_statement_0}
    for (int i = 1; i < n; ++i) {{
        {argument_type} key = {argument_name}[i];
        {useless_statement_1}
        int j = i - 1;
        {useless_statement_2}
        while (j >= 0 && {argument_name}[j] > key) {{
            {argument_name}[j + 1] = {argument_name}[j];
            {useless_statement_3}
            j = j - 1;
        }}
        {useless_statement_4}
        {argument_name}[j + 1] = key;
    }}
}}"""

MERGE_SORT = \
"""{return_type} {function_name}({argument_type} {argument_name}[], {argument_type} l, {argument_type} r) {{
    if (l < r) {{
        int m = l + (r - l) / 2;
        {useless_statement_0}
        {function_name}({argument_name}, l, m);
        {function_name}({argument_name}, m + 1, r);

        int n1 = m - l + 1;
        int n2 = r - m;
        {useless_statement_1}
        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; ++i)
            L[i] = {argument_name}[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = {argument_name}[m + 1 + j];
        {useless_statement_2}
        int i = 0, j = 0;

        int k = l;
        while (i < n1 && j < n2) {{
            if (L[i] <= R[j]) {{
                {argument_name}[k] = L[i];
                {useless_statement_3}
                i++;
            }}
            else {{
                {argument_name}[k] = R[j];
                j++;
            }}
            {useless_statement_4}
            k++;
        }}
        
        while (i < n1) {{
            {argument_name}[k] = L[i];
            i++;
            {useless_statement_5}
            k++;
        }}
        
        while (j < n2) {{
            {argument_name}[k] = R[j];
            j++;
            {useless_statement_6}
            k++;
        }}
        {useless_statement_7}
    }}
}}"""

ALL = (BUBBLE_SORT, INSERTION_SORT, MERGE_SORT)
