import parglare

# Corresponding actions
action = parglare.get_collector()

# Logical expressions
@action
def program(_, nodes):
    return nodes[0] # discard the None that matched EOF

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
def log_var(_, nodes):
    return {"type": "logical",
            "log_type": "log_var",
            "name": nodes[0]}
@action
def log_literal(_, value):
    log_expr = {"type": "logical",
                "log_type": "log_lit", "value": True}
    if value == "false":
        log_expr["value"] = False
    return log_expr
