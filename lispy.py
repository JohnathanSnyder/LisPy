#! /usr/bin/env python3.3
# LisPY
# Johnathan Snyder

import sys
import types
from parser import *
from environment import *
from lexer import *

def eval_program(tree,env):
    for app in tree:
        eval_application(app,env)

def eval_application(tree,env):
    if len(tree) >= 1:
        func = eval_expr(tree[0],env)
        if isinstance(func,types.FunctionType):
            return func(tree[1:],env)
        else:
            params = func[0]
            body = func[1]
            def_env = func[2]
            args = eval_args(tree[1:],env)
            new_env = Environment(def_env)
            i = 0
            for p in params:
                new_env.insert(p.value,args[i])
                i += 1
            return eval_expr(body,new_env)

    else:
        print(tree)
        print("Eval Error: Not a function application!")


def eval_expr(tree,env):
    if isinstance(tree,list):
        return eval_application(tree,env)
    elif tree.lex_type == Lexeme.ID:
        return env.lookup(tree.value)
    else:
        return tree

def eval_args(tree,env):
    evaled_args = []
    for arg in tree:
        evaled_args.append(eval_expr(arg,env))
    return evaled_args

def eval_plus(tree,env):
    val = 0
    lex_type = Lexeme.INT
    args = eval_args(tree,env)
    for arg in args:
        val += arg.value
        if arg.lex_type == Lexeme.FLOAT:
            lex_type = Lexeme.FLOAT
    return Lexeme(val,lex_type)

def eval_minus(tree,env):
    lex_type = Lexeme.INT
    args = eval_args(tree,env)
    val = args[0].value
    args = args[1:]
    for arg in args:
        val -= arg.value
        if arg.lex_type == Lexeme.FLOAT:
            lex_type = Lexeme.FLOAT
    return Lexeme(val,lex_type)

def eval_mult(tree,env):
    val = 1
    lex_type = Lexeme.INT
    args = eval_args(tree,env)
    for arg in args:
        val *= arg.value
        if arg.lex_type == Lexeme.FLOAT:
            lex_type = Lexeme.FLOAT
    return Lexeme(val,lex_type)

def eval_div(tree,env):
    args = eval_args(tree,env)
    val = args[0].value
    args = args[1:]
    for arg in args:
        val /= arg.value
    if isinstance(val,int):
        lex_type = Lexeme.INT
    else:
        lex_type = Lexeme.FLOAT
    return Lexeme(val,lex_type)

def eval_mod(tree,env):
    args = eval_args(tree,env)
    val = args[0].value
    args = args[1:]
    for arg in args:
        val %= arg.value
    return Lexeme(val,Lexeme.INT)

def eval_eq(tree,env):
    return Lexeme(eval_expr(tree[0],env).value == eval_expr(tree[1],env).value,Lexeme.BOOL)

def eval_def(tree,env):
    sym_name = tree[0]
    if isinstance(sym_name,list):
        sym = sym_name[0]
        params = sym_name[1:]
        body = tree[1]
        env.insert(sym.value,[params,body,env])
    else:
        env.insert(sym_name.value,eval_expr(tree[1],env))

def eval_if(tree,env):
    condition = eval_expr(tree[0],env)
    if condition.value:
        return eval_expr(tree[1],env)
    else:
        if len(tree) == 3:
            return eval_expr(tree[2],env)

def eval_cond(tree,env):
    for case in tree:
        condition = eval_expr(case[0],env)
        if not isinstance(condition,list):
            if condition.lex_type == Lexeme.BOOL:
                if condition.value:
                    return eval_expr(case[1],env)


def eval_list(tree,env):
    return eval_args(tree,env)

def eval_cons(tree,env):
    args = eval_args(tree,env)
    item = args[0]
    items = args[1]
    return [item] + items

def eval_car(tree,env):
    arg = eval_expr(tree[0],env)
    return arg[0]

def eval_cdr(tree,env):
    arg = eval_expr(tree[0],env)
    return arg[1:]

def eval_element_at(tree,env):
    args = eval_args(tree,env)
    items = args[0]
    index = args[1]
    return items[index.value]

def eval_make_dict(tree,env):
    return dict()

def eval_insert_dict(tree,env):
    args = eval_args(tree,env)
    dictionary = args[0]
    key = args[1]
    item = args[2]

    dictionary[key.value] = item
    return dictionary

def eval_get_dict(tree,env):
    args = eval_args(tree,env)
    dictionary = args[0]
    key = args[1]

    return dictionary[key.value]

def eval_quote(tree,env):
    return tree

def eval_lambda(tree,env):
    params = tree[0]
    body = tree[1]
    return [params,body,env]

def eval_null(tree,env):
    arg = eval_expr(tree[0],env)
    return Lexeme(arg == [],Lexeme.BOOL)

def eval_print(tree,env):
    for args in tree:
        print(eval_expr(args,env),end="")


def insert_builtins(env):
    env.insert("print",eval_print)
    env.insert("def",eval_def)
    env.insert("+",eval_plus)
    env.insert("-",eval_minus)
    env.insert("*",eval_mult)
    env.insert("/",eval_div)
    env.insert("=",eval_eq)
    env.insert("if",eval_if)
    env.insert("list",eval_list)
    env.insert("quote",eval_quote)
    env.insert("'",eval_quote)
    env.insert("car",eval_car)
    env.insert("cdr",eval_cdr)
    env.insert("lambda",eval_lambda)
    env.insert("cond",eval_cond)
    env.insert("null?",eval_null)
    env.insert("cons",eval_cons)
    env.insert("mod",eval_mod)
    env.insert("element-at",eval_element_at)
    env.insert("make-dict",eval_make_dict)
    env.insert("insert-dict",eval_insert_dict)
    env.insert("get-dict",eval_get_dict)

def init_lispy_env():
    p = Parser("mainlib.lisp")
    tree = p.program()
    env = Environment()
    insert_builtins(env)
    eval_program(tree,env)
    return env


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No input file specified!')
        exit()

    env = init_lispy_env()
    p = Parser(sys.argv[1])
    tree = p.program()
    eval_program(tree,env)

