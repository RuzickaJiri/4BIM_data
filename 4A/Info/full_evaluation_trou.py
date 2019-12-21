def log_eval(memory, log_expr):
    if log_expr["type"] != "logical":
        raise ValueError('Expected logical expression but got {}'.format(log_expr["type"]))
    
    if log_expr["log_type"] == "log_lit":
        return log_expr["value"]

    elif log_expr["log_type"] == "log_neg":
        expr_val = log_eval(memory, log_expr["expr"])
        return not expr_val

    elif log_expr["log_type"] == "log_conj":
        l_val = log_eval(memory, log_expr["l_expr"])
        r_val = log_eval(memory, log_expr["r_expr"])
        return l_val and r_val

    elif log_expr["log_type"] == "log_disj":
        l_val = log_eval(memory, log_expr["l_expr"])
        r_val = log_eval(memory, log_expr["r_expr"])
        return l_val or r_val
    
    elif log_expr["log_type"] == "log_inf":
        l_val = math_eval(memory, log_expr["l_expr"])
        r_val = math_eval(memory, log_expr["r_expr"])
        return l_val < r_val
    
    elif log_expr["log_type"] == "log_sup":
        l_val = math_eval(memory, log_expr["l_expr"])
        r_val = math_eval(memory, log_expr["r_expr"])
        return l_val > r_val
    
    elif log_expr["log_type"] == "log_eq":
        l_val = math_eval(memory, log_expr["l_expr"])
        r_val = math_eval(memory, log_expr["r_expr"])
        return l_val == r_val

    else:
        raise ValueError('logical {} not implemented!'.format(log_expr["log_type"]))


def math_eval(memory, math_expr):
    if math_expr["type"] != "math":
        raise ValueError('Expected math expression but got {}'.format(math_expr["type"]))

    if math_expr["math_type"] == "math_lit":
        return math_expr["value"]
    
    elif math_expr["math_type"] == "math_var":
        var_name = math_expr["name"]
        if var_name in memory:
            return memory[var_name]
        else:
            raise NameError("variable '{}' not declared".format(var_name))
    
    elif math_expr["math_type"] == "math_plus":
        l_val = math_eval(memory, math_expr["l_expr"])
        r_val = math_eval(memory, math_expr["r_expr"])
        return l_val + r_val
    
    elif math_expr["math_type"] == "math_minus":
        l_val = math_eval(memory, math_expr["l_expr"])
        r_val = math_eval(memory, math_expr["r_expr"])
        return l_val - r_val
    
    elif math_expr["math_type"] == "math_times":
        l_val = math_eval(memory, math_expr["l_expr"])
        r_val = math_eval(memory, math_expr["r_expr"])
        return l_val * r_val
    
    elif math_expr["math_type"] == "math_div":
        l_val = math_eval(memory, math_expr["l_expr"])
        r_val = math_eval(memory, math_expr["r_expr"])
        return l_val // r_val
    
    else:
        raise ValueError('math {} not implemented!'.format(math_expr["math_type"]))


def stmt_eval(memory, stmt):
    if stmt["type"] != "stmt":
        raise ValueError('Expected statement but got {}'.format(stmt["type"]))

    # Remplir ici !
        
    return memory


def program_eval(memory, prog):

    if prog["type"] != "program":
        raise ValueError('Expected program but got {}'.format(prog["type"]))

    for stmt in prog["stmts"]:
        memory = stmt_eval(memory, stmt)

    return memory
