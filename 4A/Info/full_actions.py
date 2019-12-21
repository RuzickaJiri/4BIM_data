import parglare

# Corresponding actions
action = parglare.get_collector()

# Logical expressions
@action
def program(_, nodes):
    return {"type": "program",
            "stmts": nodes[0]} # discard the None that matched EOF

@action
def log_paren(_, nodes):
    return nodes[1]

def make_log_binop(nodes, typ):
    return {"type": "logical",
            "log_type": typ,
            "l_expr": nodes[0],
            "r_expr": nodes[2]}

@action
def log_inf(_, nodes):
    return make_log_binop(nodes, "log_inf")

@action
def log_sup(_, nodes):
    return make_log_binop(nodes, "log_sup")

@action
def log_eq(_, nodes):
    return make_log_binop(nodes, "log_eq")

@action
def log_conj(_, nodes):
    return make_log_binop(nodes, "log_conj")

@action
def log_disj(_, nodes):
    return make_log_binop(nodes, "log_disj")

@action
def log_negation(_, nodes):
    return {"type": "logical",
            "log_type": "log_neg",
            "expr": nodes[1]} # discard the 'not'

@action
def log_literal(_, value):
    log_expr = {"type": "logical",
                "log_type": "log_lit", "value": True}
    if value == "false":
        log_expr["value"] = False
    return log_expr

# Math expressions

@action
def math_paren(_, nodes):
    return nodes[1]

def make_math_binop(nodes, typ):
    return {"type": "math",
            "math_type": typ,
            "l_expr": nodes[0],
            "r_expr": nodes[2]}

@action
def math_plus(_, nodes):
    return make_math_binop(nodes, "math_plus")

@action
def math_minus(_, nodes):
    return make_math_binop(nodes, "math_minus")

@action
def math_times(_, nodes):
    return make_math_binop(nodes, "math_times")

@action
def math_div(_, nodes):
    return make_math_binop(nodes, "math_div")


@action
def math_literal(_, value):
    return {"type": "math",
            "math_type": "math_lit",
            "value": int(value)}

@action
def math_var(_, nodes):
    return {"type": "math",
            "math_type": "math_var",
            "name": nodes[0]}

# Statements

@action
def skip(_, nodes):
    return {"type": "stmt",
            "stmt_type": "skip"}

@action
def assign(_, nodes):
    return {"type": "stmt",
            "stmt_type": "assign",
            "var_name": nodes[0],
            "expr": nodes[2]}

@action
def block(_, nodes):
    return {"type": "stmt",
            "stmt_type": "block",
            "stmts": nodes[1]}

@action
def loop(_, nodes):
    return {"type": "stmt",
            "stmt_type": "loop",
            "cond_expr": nodes[2],
            "loop_block": nodes[4]}

@action
def cond(_, nodes):
    return {"type": "stmt",
            "stmt_type": "cond",
            "cond_expr": nodes[2],
            "if_block": nodes[4],
            "else_block": nodes[6]}

@action
def print_log(_, nodes):
    return {"type": "stmt",
            "stmt_type": "print_log",
            "log_expr": nodes[2]}

@action
def print_math(_, nodes):
    return {"type": "stmt",
            "stmt_type": "print_math",
            "math_expr": nodes[2]}
