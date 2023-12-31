from collections import defaultdict
from termcolor import cprint


def is_block():
    return True


class Block:
    def __init__(self):
        self.name = []
        self.instructions = []
        self.return_type = None
        self.params = []

    def append(self, instruction):
        self.instructions.append(instruction)

    def init_name(self, name):
        self.name = name


bool_ops = {
    '>', '<', '==', '<>', '>=', '<=', 'and', 'or'
}
binary_ops = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    'div': 'div',
    'mod': 'mod',
    '<': 'lt',
    '<=': 'le',
    '>': 'gt',
    '>=': 'ge',
    '==': 'eq',
    '<>': 'ne',
    'and': 'and',
    'or': 'or',
    '/': 'div'
}

unary_ops = {
    '+': 'uadd',
    '-': 'usub',
    'Not': 'not'
}
type_conv = {'integer': 'int', 'real': 'float', 'boolean': 'bool'}
default = {'integer': 0, 'real': 0.0}

versions = defaultdict(int)


def new_temp(type_obj):
    """
    Create a new temporary variable of a given type.
    """
    name = "__%s_%d" % (type_obj, versions[type_obj])
    versions[type_obj] += 1
    return name


def GenerateCode(parent_block, tree, scope, IsMain, table):
    for part in tree.parts:
        if type(part) != str and part:
            if part.type == 'Var':
                if scope == 'global':
                    new = Block()
                    new.init_name('__init')
                    new.return_type = 'void'
                    parent_block.append(new)
                else:
                    new = Block()
                    new.init_name(part.type)
                    parent_block.append(new)
                if scope != 'global' and not (scope.startswith(' ')):
                    new.append(('alloc_' + type_conv[table[scope].get(scope)[0]], scope))
                    id = new_temp(type_conv[table[scope].get(scope)[0]])
                    new.append(('literal_' + type_conv[table[scope].get(scope)[0]], 0, id))
                    new.append(('store_' + type_conv[table[scope].get(scope)[0]], id, scope))
                for i in range(0, len(part.parts), 2):
                    for g in range(len(part.parts[i].parts)):
                        if scope != 'global':
                            tradr = 'alloc_' + type_conv[part.parts[i + 1].parts[0]]
                        else:
                            tradr = 'global_' + type_conv[part.parts[i + 1].parts[0]]
                        id = part.parts[i].parts[g]

                        new.append((tradr, id))
                        newtmpe = new_temp(type_conv[part.parts[i + 1].parts[0]])
                        new.append(('literal_' + type_conv[part.parts[i + 1].parts[0]],
                                    default[part.parts[i + 1].parts[0]], newtmpe))
                        new.append(('store_' + type_conv[part.parts[i + 1].parts[0]], newtmpe, id))
                if scope == 'global':
                    new.append(('return_void',))
                GenerateCode(new, part, scope, IsMain, table)
            if part.type == 'Arguments':
                new = Block()
                new.init_name('Var2')
                parent_block.append(new)
                index = 0
                for i in range(0, len(part.parts), 2):

                    for g in range(len(part.parts[i].parts)):
                        tradr = 'parm_' + type_conv[part.parts[i + 1].parts[0]]
                        parent_block.params.append(type_conv[part.parts[i + 1].parts[0]])
                        id = part.parts[i].parts[g]
                        new.append((tradr, id, index))
                        index = index + 1

                GenerateCode(new, part, scope, IsMain, table)
            if part.type == 'SubDeclaration':
                scope = part.parts[0].type[5:]
                new = Block()
                new.init_name(part.parts[0].type)
                if part.parts[0].type.startswith('func'):
                    new.return_type = type_conv[part.parts[0].parts[1].parts[0]]
                if part.parts[0].type.startswith('proc'):
                    new.return_type = 'void'
                parent_block.append(new)
                GenerateCode(new, part, scope, IsMain, table)
                for ins in new.instructions:  # если встречаем блоки var1 и var 2 (то есть аргументы и вары функции ,
                    # то мерджим два блока )
                    for ins2 in new.instructions:  # естесственно через зад
                        if ins.name == 'Var' and ins2.name == 'Var2':
                            for a in range(len(ins.instructions)):
                                ins2.append(ins.instructions[a])
                            ins2.init_name('Var')
                            i = (new.instructions.index(ins))
                            new.instructions.pop(i)
                if part.parts[0].type.startswith('func'):
                    rtrn = new_temp(type_conv[part.parts[0].parts[1].parts[0]])
                    ex = ('load_' + type_conv[part.parts[0].parts[1].parts[0]], part.parts[0].type[5:], rtrn)
                    new.append(ex)
                    ex = ('return_' + type_conv[part.parts[0].parts[1].parts[0]], rtrn)
                    new.append(ex)
                scope = 'global'
            elif part.type == 'Compound statement':
                if parent_block.name != 'WHILEbody_Block' and scope == 'global' and (not IsMain):
                    new = Block()
                    new.init_name('main')
                    new.return_type = 'void'
                    IsMain = True
                    parent_block.append(new)
                    GenerateCode(new, part, scope, IsMain, table)
                elif parent_block.name != 'WHILEbody_Block':
                    new = Block()
                    new.init_name('default')
                    parent_block.append(new)
                    GenerateCode(new, part, scope, IsMain, table)
                else:
                    GenerateCode(parent_block, part, scope, IsMain, table)
                # print(2)
            elif part.type == 'If clause':
                ifBlock = Block()
                ifBlock.init_name('IfBlock')
                parent_block.append(ifBlock)
                condition = Block()
                condition.init_name('IFcondition')
                body = Block()
                body.init_name('IFbody')
                ifBlock.append(condition)
                ifBlock.append(body)
                GenerateCode(condition, part.parts[0], scope, IsMain, table)
                GenerateCode(body, part.parts[1], scope, IsMain, table)
            elif part.type == 'While clause':
                whileBlock = Block()
                whileBlock.init_name('WhileBlock')
                parent_block.append(whileBlock)
                condition = Block()
                condition.init_name('WHILEcondition')
                wbody = Block()
                wbody.init_name('WHILEbody')
                whileBlock.append(condition)
                whileBlock.append(wbody)
                GenerateCode(condition, part.parts[0], scope, IsMain, table)
                GenerateCode(wbody, part.parts[1], scope, IsMain, table)

            elif part.type == 'print':
                # print(part)
                if type(part.parts[0]) is str:
                    typer = table[scope].get(part.parts[0])[0]
                    tmp1 = new_temp(type_conv[typer])
                    parent_block.append(('load_' + type_conv[typer], part.parts[0], tmp1))
                    parent_block.append(('print_' + type_conv[typer], tmp1))
                else:
                    tmp = new_temp('str')
                    parent_block.append(('literal_string', part.parts[0].parts[0], tmp))
                    parent_block.append(('print_string', tmp))

            elif part.type == 'Assign':
                if scope.startswith(' '):
                    scope = scope[1:]
                exp = []
                # print(part)
                name = GenerateForExres(part.parts[1], scope, exp, table)
                # print(name)
                if type(part.parts) is not str:
                    if type(part.parts[1].parts[0]) != str:
                        if part.parts[1].parts[0].type == 'Func':
                            if type(part.parts[1].parts[0].parts) is not str:
                                for a in exp:
                                    parent_block.append(a)
                                vap = []
                                vap.append('call_func')
                                vap.append(part.parts[1].parts[0].parts[0])
                                for g in range(len(name)):
                                    # print(name)
                                    vap.append(name[g])
                                # print(vap)

                                tmp1 = new_temp(
                                    type_conv[table[scope].get(part.parts[0].parts[0])[0]])
                                vap.append(tmp1)
                                parent_block.append(tuple(vap))
                                if (type_conv[table[scope].get(part.parts[0].parts[0])[0]] != type_conv[
                                    table[scope].get(part.parts[0].parts[0])[0]]):
                                    print('ERROR , You are assigning ', type_conv[
                                        table[part.parts[1].parts[0].parts[0]].get(part.parts[0].parts[0])[0]], ' to ',
                                          type_conv[table[scope].get(part.parts[0].parts[0])[0]])
                                    tmp3 = new_temp('float')
                                    parent_block.append(('convert_to_float', tmp1, tmp3))
                                    tmp1 = tmp3

                                parent_block.append(('store_' + type_conv[
                                    table[scope].get(part.parts[0].parts[0])[0]], tmp1,
                                                     part.parts[0].parts[0]))
                        else:
                            nameType = name[2:5]
                            if nameType == 'flo':
                                nameType = 'float'
                            for a in exp:
                                parent_block.append(a)
                            if nameType != type_conv[table[scope].get(part.parts[0].parts[0])[0]]:
                                print('ERROR , You are assigning ', nameType, ' to ',
                                      type_conv[table[scope].get(part.parts[0].parts[0])[0]])
                                tmp3 = new_temp('float')
                                parent_block.append(('convert_to_float', name, tmp3))
                                name = tmp3
                            parent_block.append(('store_' + nameType, name, part.parts[0].parts[0]))
                    else:
                        nameType = name[2:5]
                        if nameType == 'flo':
                            nameType = 'float'
                        for a in exp:
                            parent_block.append(a)
                        if nameType != type_conv[table[scope].get(part.parts[0].parts[0])[0]]:
                            print('ERROR , You are assigning ', nameType, ' to ',
                                  type_conv[table[scope].get(part.parts[0].parts[0])[0]])
                            tmp3 = new_temp('float')
                            parent_block.append(('convert_to_float', name, tmp3))
                            name = tmp3
                        parent_block.append(('store_' + nameType, name, part.parts[0].parts[0]))
            elif part.type == 'BR':
                if part.parts[0] == 'break':
                    parent_block.append(tuple(['break']))
                if part.parts[0] == 'continue':
                    parent_block.append(tuple(['continue']))

            elif part.type == 'Call proc':
                exp = ['call_proc', part.parts[0]]

                for g in range(len(part.parts[1].parts[0].parts)):
                    gen = []
                    name = GenerateForExres(part.parts[1].parts[0].parts[g], scope, gen, table)
                    for a in gen:
                        parent_block.append(a)
                    exp.append(name)
                parent_block.append(tuple(exp))
            elif part.type == 'Expression in parentheses':
                exp = []
                GenerateForExres(part, scope, exp, table)
                for a in exp:
                    parent_block.append(a)
            elif part.type == 'Expression':
                exp = []
                GenerateForExres(part, scope, exp, table)
                for a in exp:
                    parent_block.append(a)
            else:
                GenerateCode(parent_block, part, scope, IsMain, table)

    return parent_block


def GenerateForExres(tree, scope, exp, table):
    if scope.startswith(' '):
        scope = scope[1:]
    if type(tree) is not str:
        if tree.type == 'Func':
            p = []

            for g in range(len(tree.parts[1].parts)):
                if table[scope].get(tree.parts[1].parts[g].parts[0]) is not None:
                    typer = table[scope].get(tree.parts[1].parts[g].parts[0])[0]
                    tmp1 = new_temp(type_conv[typer])
                    exp.append(('load_' + type_conv[typer], tree.parts[1].parts[g].parts[0], tmp1))

                else:
                    if tree.parts[1].parts[g].parts[0].find('.') != -1:
                        typer = 'real'
                        value = float(tree.parts[1].parts[g].parts[0])
                    else:
                        typer = 'integer'
                        value = int(tree.parts[1].parts[g].parts[0])
                    tmp1 = new_temp(type_conv[typer])
                    exp.append(('literal_' + type_conv[typer], value, tmp1))
                p.append(tmp1)
            return p
        elif len(tree.parts) == 1 and type(tree.parts[0]) != str and tree.type == 'Not':
            name = GenerateForExres(tree.parts[0], scope, exp, table)
            ended = new_temp('bool')
            exp.append(('not_bool', name, ended))
            return ended

        elif len(tree.parts) == 1 and type(tree.parts[0]) == str:
            if table[scope].get(tree.parts[0]) != None:
                typer = table[scope].get(tree.parts[0])[0]
                tmp1 = new_temp(type_conv[typer])
                exp.append(('load_' + type_conv[typer], tree.parts[0], tmp1))
            else:
                if tree.parts[0].find('.') != -1:
                    typer = 'real'
                    value = float(tree.parts[0])
                else:
                    typer = 'integer'
                    value = int(tree.parts[0])
                tmp1 = new_temp(type_conv[typer])
                exp.append(('literal_' + type_conv[typer], value, tmp1))
            return tmp1
        elif len(tree.parts) == 2 and type(tree.parts[0]) == str and type(
                tree.parts[1]) != str:  # если второй операнд сложное выражение
            if table[scope].get(tree.parts[0]) is not None:
                typer = table[scope].get(tree.parts[0])[0]
                tmp1 = new_temp(type_conv[typer])
                exp.append(('load_' + type_conv[typer], tree.parts[0], tmp1))
            else:
                if tree.parts[0].find('.') != -1:
                    typer = 'real'
                    value = float(tree.parts[0])
                else:
                    typer = 'integer'
                    value = int(tree.parts[0])
                tmp1 = new_temp(type_conv[typer])
                exp.append(('literal_' + type_conv[typer], value, tmp1))
            name = GenerateForExres(tree.parts[1], scope, exp, table)
            if tmp1[2:5] != name[2:5] or tree.type == '/':
                typer = 'real'
                if tmp1[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', tmp1, tmp3))
                    tmp1 = tmp3
                if name[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', name, tmp3))
                    name = tmp3
            if tree.type in bool_ops:
                ended = new_temp('bool')
            else:
                ended = new_temp(type_conv[typer])
            exp.append((binary_ops[tree.type] + '_' + type_conv[typer], tmp1, name, ended))
            return ended

        elif len(tree.parts) == 2 and type(tree.parts[1]) == str and type(
                tree.parts[0]) != str:  # если первый операнд сложное выражение
            if table[scope].get(tree.parts[1]) is not None:
                typer = table[scope].get(tree.parts[1])[0]
                tmp1 = new_temp(type_conv[typer])
                exp.append(('load_' + type_conv[typer], tree.parts[1], tmp1))
            else:
                if tree.parts[1].find('.') != -1:
                    typer = 'real'
                    value = float(tree.parts[1])
                else:
                    typer = 'integer'
                    value = int(tree.parts[1])
                tmp1 = new_temp(type_conv[typer])
                exp.append(('literal_' + type_conv[typer], value, tmp1))
            name = GenerateForExres(tree.parts[0], scope, exp, table)
            if tmp1[2:5] != name[2:5] or tree.type == '/':
                typer = 'real'
                if tmp1[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', tmp1, tmp3))
                    tmp1 = tmp3
                if name[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', name, tmp3))
                    name = tmp3
            if tree.type in bool_ops:
                ended = new_temp('bool')
            else:
                print(tree.type)
                ended = new_temp(type_conv[typer])
            exp.append((binary_ops[tree.type] + '_' + type_conv[typer], tmp1, name, ended))
            return ended

        elif len(tree.parts) == 2 and type(tree.parts[0]) != str and type(
                tree.parts[1]) != str:  # если оба являются сложными выражениями
            name = GenerateForExres(tree.parts[0], scope, exp, table)
            name2 = GenerateForExres(tree.parts[1], scope, exp, table)
            typer = name[2:5]
            if name[2:5] != name2[2:5] or tree.type == '/':
                typer = 'real'
                if name[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', name, tmp3))
                    name = tmp3
                if name2[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', name2, tmp3))
                    name2 = tmp3
            if typer == 'boo':
                typer = 'boolean'
            if typer == 'flo':
                typer = 'real'
            if typer == 'int':
                typer = 'integer'
            if tree.type in bool_ops:
                ended = new_temp('bool')
            else:
                ended = new_temp(type_conv[typer])
                exp.append((''))
            exp.append(((binary_ops[tree.type] + '_' + type_conv[typer]), name, name2, ended))
            return ended

        elif len(tree.parts) == 2 and type(tree.parts[0]) == str and type(
                tree.parts[1]) == str:  # если оба операнда оказались не составными
            if table[scope].get(tree.parts[0]) is not None:
                typer = table[scope].get(tree.parts[0])[0]
                tmp1 = new_temp(type_conv[typer])
                exp.append(('load_' + type_conv[typer], tree.parts[0], tmp1))
            else:
                if tree.parts[0].find('.') != -1:
                    typer = 'real'
                    value = tree.parts[0]
                else:
                    typer = 'integer'
                    value = tree.parts[0]
                tmp1 = new_temp(type_conv[typer])
                exp.append(('literal_' + type_conv[typer], value, tmp1))
            if table[scope].get(tree.parts[1]) is not None:
                typer = table[scope].get(tree.parts[1])[0]
                tmp2 = new_temp(type_conv[typer])
                exp.append(('load_' + type_conv[typer], tree.parts[1], tmp2))
            else:
                if tree.parts[1].find('.') != -1:
                    typer = 'real'
                    value = float(tree.parts[1])
                else:
                    typer = 'integer'
                    value = int(tree.parts[1])
                tmp2 = new_temp(type_conv[typer])
                exp.append(('literal_' + type_conv[typer], value, tmp2))
            if tmp1[2:5] != tmp2[2:5] or tree.type == '/':
                typer = 'real'
                if tmp1[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', tmp1, tmp3))
                    tmp1 = tmp3
                if tmp2[2:5] == 'int':
                    tmp3 = new_temp('float')
                    exp.append(('convert_to_float', tmp2, tmp3))
                    tmp2 = tmp3
            if tree.type in bool_ops:
                ended = new_temp('bool')
            else:
                ended = new_temp(type_conv[typer])
            exp.append((binary_ops[tree.type] + '_' + type_conv[typer], tmp1, tmp2, ended))
            return ended
        else:
            for part in tree.parts:
                end = GenerateForExres(part, scope, exp, table)
    return end


def prTr(block, sink):
    for a in block.instructions:

        if a.__class__ is not tuple:

            print(' ' * sink * 3 + a.name, end='')
            if a.return_type is not None:
                print('   | ' + a.return_type, a.params, end='')
            print('\t')

            prTr(a, sink + 1)
        else:

            print(' ' * sink * 3, end='')
            cprint(a, 'cyan')
