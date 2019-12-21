def log_eval(memory, log_expr):
    if log_expr["type"] != "logical":
        raise ValueError('Expected logical expression but got {}'.format(log_expr["type"]))
    
    if log_expr["log_type"] == "log_lit":
        # Ajouter le code ici pour les constantes...
        return log_expr["value"]
    if log_expr["log_type"] == "log_var":
        return memory[log_expr["name"]]
    if log_expr["log_type"] == "log_neg":
        return not log_eval(memory, log_expr["expr"])
    if log_expr["log_type"] == "log_conj":
        return log_eval(memory, log_expr["l_expr"]) and log_eval(memory, log_expr["r_expr"])
    if log_expr["log_type"] == "log_disj":
        return log_eval(memory, log_expr["l_expr"]) or log_eval(memory, log_expr["r_expr"])

    else:
        raise ValueError('logical {} not implemented!'.format(log_expr["log_type"]))