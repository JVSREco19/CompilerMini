import ply.yacc as yacc
from MiniLexer import tokens, errorsList,createLexer
from symbols_table import SymbolTable
import os

symbolTable = SymbolTable()

current_rule = ""



opHash = {
    '=': lambda x, y: x == y,
    '>': lambda x, y: x > y,
    '>=': lambda x, y: x >= y,
    '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y,
    '<>': lambda x, y: x != y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'or': lambda x, y: x or y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    'mod': lambda x, y: x % y,
    'and': lambda x, y: x and y,
}


# Definição das regras gramaticais

def p_program(p):
  '''program : PROGRAM IDENTIFIER body'''
  global current_rule
  current_rule = "program"


def p_body(p):
  '''body : declare_opt BEGIN stmt_list END'''
  global current_rule
  current_rule = "body"

def p_declare_opt(p):
  '''declare_opt : DECLARE decl_list'''
  global current_rule
  current_rule = "declare_opt"

def p_decl_list(p):
  '''decl_list : decl  decl_list'''
  global current_rule
  current_rule = "decl_list"


def p_decl_list_single(p):
  '''decl_list : decl'''
  global current_rule
  current_rule = "decl_list_single"


def p_decl(p):
  '''decl : type ident_list SEMICOLON'''
  IDs = p[2].split(',')
  for i in IDs:
    symbolTable.add(i,0,{"Tipo":p[1],"Valor":None})
    global current_rule
    current_rule = "decl"
  
def p_type(p):
  '''type : INTEGER 
  | DECIMAL'''
  p[0] = p[1]
  global current_rule
  current_rule = "type"

def p_ident_list(p):
  '''ident_list : IDENTIFIER COMMA ident_list
  '''
  
  
  if(len(p)==4):
    p[0] = p[1] + p[2] + p[3]
  global current_rule
  current_rule = "ident_list"

  
def p_ident_list_single(p):
  '''ident_list : IDENTIFIER'''
  
  p[0] = p[1]
  global current_rule
  current_rule = "ident_list_single"

def p_stmt_list(p):
  '''stmt_list : stmt SEMICOLON stmt_list_aux
  '''
  global current_rule
  current_rule = "stmt_list"

def p_stmt_list_aux(p):
  '''stmt_list_aux : stmt_list
  | empty
  '''
  global current_rule
  current_rule = "stmt_list"
    
  
def p_stmt(p):
  '''stmt : if_stmt 
            | assign_stmt 
            | while_stmt 
            | do_while_stmt 
            | for_stmt 
            | read_stmt 
            | write_stmt 
  '''
  p[0] = p[1]
  global current_rule
  current_rule = "stmt"
  
def p_assign_stmt(p):
  '''assign_stmt : IDENTIFIER ASSIGN simple_expr'''

  if(symbolTable.contains(p[1])):
    p[0] = 1
  else:
    p[0] = 0
    print("Erro semantico")

  global current_rule
  current_rule = "assign_stmt"


def p_if_stmt(p):
  '''if_stmt : IF condition THEN stmt_list END
              | IF condition THEN stmt_list ELSE stmt_list END
  '''
  global current_rule
  current_rule = "if_stmt"
  
def p_do_while_stmt(p):
  '''do_while_stmt : DO stmt_list END SEMICOLON stmt_suffix'''
  
  global current_rule
  current_rule = "do_while_stmt"
  
def p_stmt_suffix(p):
  '''stmt_suffix : WHILE condition'''
  
  global current_rule
  current_rule = "stmt_suffix"
  
def p_for_stmt(p):
  '''for_stmt : FOR assign_stmt TO condition DO stmt_list END'''
  global current_rule
  current_rule = "for_stmt"
  
def p_while_stmt(p):
  '''while_stmt : WHILE condition DO stmt_list END'''
  global current_rule
  current_rule = "while_stmt"
  
def p_condition(p):
  '''condition : expression'''
  
  p[0] = p[1]
  
  global current_rule
  current_rule = "condition"
  
def p_read_stmt(p):
  '''read_stmt : READ LPAREN IDENTIFIER RPAREN'''
  if(symbolTable.contains(p[3])):
    p[0] = 1
  else:
    print("Erro semantico")

  global current_rule
  current_rule = "read_stmt"
 
def p_write_stmt(p):
  '''write_stmt : WRITE LPAREN writable RPAREN'''
  global current_rule
  current_rule = "write_stmt"
 
def p_writable(p):
  '''writable : simple_expr
              | LITERAL
  '''
  p[0] = p[1]
  global current_rule
  current_rule = "writable"
  
def p_expression(p):
  '''expression : simple_expr aux_expression
                
  '''
  global current_rule
  current_rule = "expression"
  # if(len(p)==2):
  #   p[0] = p[1]  
  # else:
  #   p[0] = opHash[p[2]](p[1],p[3])
  
def p_aux_expression(p):
  '''aux_expression : RELOP simple_expr
                  | empty
                
  '''
  global current_rule
  current_rule = "expression"
  # if(len(p)==2):
  #   p[0] = p[1]  
  # else:
  #   p[0] = opHash[p[2]](p[1],p[3])
    
def p_simple_expr(p):
  '''simple_expr : term
                  | simple_expr ADDOP term
                  | par_simple_expr QUESTION_MARK simple_expr COLON simple_expr
  '''
  global current_rule
  current_rule = "simple_expr "

  # if(len(p)==2):
  #   p[0] = p[1]
  # elif(len(p)==4):
  #   if(p[1] == '('):
  #     p[0] = p[2]
  #   else:
  #       p[0] = opHash[p[2]](p[1],p[3])
  # else:
  #   if(p[1]):
  #     p[0] = p[3]
  #   else:
  #     p[0] = p[5]
  
def p_par_simple_expr(p):
  '''par_simple_expr : LPAREN expression RPAREN

  '''
  global current_rule
  current_rule = "par_simple_expr "

def p_mulop(p):
  '''mulop : MULOP
            | AND
            | MOD
              
  '''
  p[0] = p[1]
  global current_rule
  current_rule = "mulop"

def p_ADDOP(p):
  '''ADDOP : MINUS
            | ADD
            | OR
              
  '''
  p[0] = p[1]
  global current_rule
  current_rule = "ADDOP"
  
def p_term(p):
  '''term : factor_a
          | term mulop factor_a
  '''
  global current_rule
  current_rule = "term"
  
  # if(len(p)== 2):
  #   p[0] = p[1]
  # else:
  #   p[0] = opHash[p[2]](p[1],p[3])

  
def p_factor_a(p):
  '''factor_a : factor
              | NOT factor
              | MINUS factor
  '''
  # if(len(p)==2):
  #   p[0] = p[1]
  # else:
  #   p[0] = not p[1]
    
  global current_rule
  current_rule = "factor_a"
  
def p_factor(p):
  '''factor : IDENTIFIER
            | LPAREN expression RPAREN
            | CONSTANT
 
  '''
  if(len(p)==2):
    if(p.slice[1].type == "IDENTIFIER"):
      if(symbolTable.contains(p[1])):
        p[0] = symbolTable.get()[p[1]]['attribute']['Valor']
      else:
        print("Erro semantico")
  else:
    p[0] = p[2]
    
  global current_rule
  current_rule = "factor"
    


def p_error(p):
    global current_rule
    if p:
        print(f"Syntax error at token {p.type} on line {p.lineno} and value {p.value} and rule :{current_rule}")

    else:
        print("Syntax error at EOF")
    
    current_rule = "error"


def p_empty(p):
  'empty :'
  
  pass

# Exemplo de uso do analisador sintático
if __name__ == '__main__':
  arquivos = os.listdir('./Testes/')
  for arquivo in arquivos:
    # Crie o analisador
    lex = createLexer()
    parser = yacc.yacc()
    caminho_arquivo = os.path.join('./Testes/', arquivo)
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_txt:
      symbolTable = SymbolTable()
      programa = arquivo_txt.read()
      print("Verificando o " + arquivo+'\n')
      result = parser.parse(programa)
      print('\n'+"Tabela de simbolos: "+'\n')
      for key,value in symbolTable.table.items():
        print(key + ": "+ str(value))
    
    symbolTable.clear()
