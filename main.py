import ctypes
import sys
import time
from termcolor import cprint

import llvmlite.binding as llvm
from codegeneration import Block, GenerateCode, prTr
from lexer import Lexer
from parser import build_tree, getTable


def run(llvm_ir):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()

    pmb = llvm.create_pass_manager_builder()
    pmb.opt_level = 1
    pm = llvm.create_module_pass_manager()
    pmb.populate(pm)
    pm.run(mod)

    engine = llvm.create_mcjit_compiler(mod, target_machine)
    init_ptr = engine.get_function_address('__init')
    init_func = ctypes.CFUNCTYPE(None)(init_ptr)
    init_func()
    main_ptr = engine.get_function_address('main')
    main_func = ctypes.CFUNCTYPE(None)(main_ptr)
    main_func()


def UnusedVariables(llvm_ir):
    optimized_ir = ""
    lines = llvm_ir.split('\n')
    variables = set()

    for line in lines:
        if line.startswith('%') and '=' in line:
            parts = line.split('=')
            lhs = parts[0].strip()
            rhs = parts[1].strip()

            if any(var in rhs for var in variables):
                variables.add(lhs)
                optimized_ir += line + '\n'
        else:
            optimized_ir += line + '\n'
    return optimized_ir


def ConstantPropagation(args):
    return True


def ConstantFolding(args):
    return True


def ComSubExpElim(args):
    return True


def main():
    from interpritator import compile_llvm

    if len(sys.argv) == 2:
        source = open(sys.argv[1]).read()
    else:
        file_name = input('Enter code file name or use `python main.py filename`:\n')
        source = open(file_name).read()

    print("--------------------------------Tokens---------------------------------------------")
    Lexer.lexer.input(source)
    while True:
        tok = Lexer.lexer.token()
        if not tok:
            break
        print(tok)

    tree = build_tree(source)
    cprint("\n---------------------AST---------------------", 'red')
    cprint(tree, 'red')
    cprint("\n---------------------SYMBOLS_TABLE---------------------", 'green')
    tmp = getTable(tree)
    for i in tmp:
        cprint(f"{i} -- {tmp[i]}", 'green')
    # print(getTable(tree))

    block = Block()
    block.init_name('Main')
    block = GenerateCode(block, tree, 'global', False, getTable(tree))
    cprint("\n---------------------THREE-ADDRESS CODE---------------------", 'cyan')
    prTr(block, 1)

    llvm_code = compile_llvm(block)
    with open('Code.ll', 'wb') as f:
        f.write(llvm_code.encode('utf-8'))
        f.flush()

    cprint("\n---------------------LLVM CODE---------------------", 'blue')
    cprint(llvm_code, 'blue')
    cprint("\n---------------------RESULTS--------------------", 'cyan')
    print(llvm_code)
    optimized_code = UnusedVariables(llvm_code)
    optimized_code = ConstantPropagation(optimized_code)
    optimized_code = ConstantFolding(optimized_code)
    optimized_llvm_code = ComSubExpElim(optimized_code)
    print(optimized_llvm_code)


    run(llvm_code)




if __name__ == '__main__':
    start = time.time()
    main()
    cprint(f"running time: {time.time() - start} sec", 'magenta')
