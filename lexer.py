import ply.lex as lex
import re

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'while': 'WHILE',
    'begin': 'BEGIN',
    'end': 'END',
    'var': 'VAR',
    'do': 'DO',
    'continue': 'CONTINUE',
    'break': 'BREAK',
    'integer': 'INT',
    'real': 'REAL',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'div': 'DIV',
    'mod': 'MOD',
    'print': 'PRINT',
    'read': 'READ',
    'string': 'STRI',
    'program': 'PROGRAM',
    'func': 'FUNC',
    'proc': 'PROC',
    'return': 'RETURN'

}
states = (
    ('string', 'exclusive'),
)

# без этой штуки ничего не интерпретируется, потому что этот массив делится между лексером и парсером и кроме того
# используется внутренней библиотекой
tokens = [
             'ASSIGN', 'EQUAL',
             'STRING', 'COLON', 'COMMA',
             'OPEN_PAREN', 'CLOSE_PAREN', 'INT_DIGIT',
             'PLUS', 'MINUS', 'MULTIPLE', 'STR', 'SEMICOLON',
             'ID', 'COMPARE', 'DOT', 'REAL_DIGIT', 'DIVIDE'
         ] + list(reserved.values())

# для каждого токена из массива мы должны написать его определение вида t_ИМЯТОКЕНА = регулярка
t_DIVIDE = r'\/'
t_DOT = r'\.'
t_COMPARE = r'\>\=|\<\=|\>|\<|\<\>'
t_EQUAL = r'\=='
t_COLON = r'\:'
t_ASSIGN = r'\='
t_SEMICOLON = r';'
t_COMMA = r','
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_INT_DIGIT = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLE = r'\*'
t_REAL_DIGIT = r'\d+\.\d+'


class Lexer:

    def __init__(self):
        self.type = None
        self.value = None

    def t_ID(self):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        self.type = reserved.get(self.value, 'ID')  # Check for reserved words
        return self

    # игнорируем комментарии
    def t_comment(self):
        r'(\{(.|\n)*?\})|(//.*)'
        pass

    def t_ANY_STRING(self):  # нужен в обоих состояниях, потому что двойные кавычки матчатся и там и там.
        r'"'
        if self.lexer.current_state() == 'string':
            self.lexer.begin('INITIAL')  # переходим в начальное состояние
        else:
            self.lexer.begin('string')  # парсим строку
        return self

    t_string_STR = r'(\\.|[^$"])+'  # парсим пока не дойдем до переменной или до кавычки, попутно игнорируем экранки

    # говорим что ничего не будем игнорировать
    t_string_ignore = ''  # это кстати обязательная переменная, без неё нельзя создать новый state

    # ну и куда же мы без обработки ошибок
    def t_string_error(self):
        print("Illegal character '%s'" % self.value[0])
        self.lexer.skip(1)

    # здесь мы игнорируем незначащие символы. Нам ведь все равно, написано $var=$value или $var   =  $value
    t_ignore = ' \r\t\f'

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    lexer = lex.lex(reflags=re.UNICODE | re.DOTALL | re.IGNORECASE)
