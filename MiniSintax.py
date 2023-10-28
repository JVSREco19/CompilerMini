import ply.yacc as yacc
from MiniLexer import tokens, errorsList,createLexer
import os
from symbols_table import SymbolTable 
# Definição das regras gramaticais


def p_program(p):
  'program : PROGRAM IDENTIFIER body'
  # Implemente ação semântica desejada para a regra program


def p_body(p):
  'body : declare_opt BEGIN stmt_list END'
  # Implemente ação semântica desejada para a regra body


def p_declare_opt(p):
  'declare_opt : DECLARE decl_list'
  # Implemente ação semântica desejada para a regra declare_opt

  
def p_decl_opt_empty(p):
  'declare_opt :'
  # Implemente ação semântica desejada para o caso em que declare_opt é vazio

  
def p_decl_list(p):
  'decl_list : decl  decl_list'
  # Implemente ação semântica desejada para a regra decl_list


def p_decl_list_single(p):
  'decl_list : decl'
  # Implemente ação semântica desejada para o caso em que decl_list contém apenas uma declaração


def p_decl(p):
  'decl : type ident_list SEMICOLON '
  # Implemente ação semântica desejada para a regra decl


def p_type(p):
  '''type : INTEGER 
  | DECIMAL'''
  # Implemente ação semântica desejada para a regra decl


def p_ident_list(p):
  'ident_list : IDENTIFIER COMMA ident_list'
  # Implemente ação semântica desejada para a regra ident_list

def p_ident_list_single(p):
  'ident_list : IDENTIFIER'
  # Implemente ação semântica desejada para o caso em que ident_list contém apenas um identificador

def p_stmt_list(p):
  '''stmt_list : stmt SEMICOLON stmt_list 
  '''
  # Implemente a ação semântica desejada para a regra if_stmt
def p_stmt_list_single(p):
  '''stmt_list : stmt SEMICOLON
  '''
  # Implemente a ação semântica desejada para a regra if_stmt

def p_stmt(p):
  '''stmt : if_stmt 
            | assign_stmt 
            | while_stmt 
            | do_while_stmt 
            | for_stmt 
            | read_stmt 
            | write_stmt 
  '''
  # Implemente a ação semântica desejada para a regra if_stmt

def p_assign_stmt(p):
  'assign_stmt : IDENTIFIER ASSIGN simple_expr'
  # Implemente a ação semântica desejada para a regra assign_stmt

def p_if_stmt(p):
  '''if_stmt : IF condition THEN stmt_list END
              | IF condition THEN stmt_list ELSE stmt_list END
  '''
  # Implemente a ação semântica desejada para a regra if_stmt

def p_do_while_stmt(p):
  'do_while_stmt : DO stmt_list stmt_suffix'
  print("Passou pelo do while")
  
  # Implemente a ação semântica desejada para a regra do_while_stmt

def p_stmt_suffix(p):
  'stmt_suffix : WHILE condition'
  # Implemente a ação semântica desejada para a regra stmt_suffix
  
def p_for_stmt(p):
  'for_stmt : FOR assign_stmt TO condition DO stmt_list END'
  # Implemente a ação semântica desejada para a regra for_stmt

def p_while_stmt(p):
  'while_stmt : WHILE condition DO stmt_list END'
  # Implemente a ação semântica desejada para a regra while_stmt

def p_condition(p):
  'condition : expression'
  # Implemente a ação semântica desejada para a regra while_stmt

def p_read_stmt(p):
  'read_stmt : READ LPAREN IDENTIFIER RPAREN'
  # Implemente a ação semântica desejada para a regra read_stmt

def p_write_stmt(p):
  'write_stmt : WRITE LPAREN writable RPAREN'
  # Implemente a ação semântica desejada para a regra write_stmt

def p_writable(p):
  '''writable : simple_expr
              | LITERAL
  '''
  # Implemente a ação semântica desejada para a regra writable

def p_expression(p):
  '''expression : simple_expr
                | expression RELOP expression
                | LPAREN expression RPAREN
  '''
  # Implemente a ação semântica desejada para a regra expression

def p_simple_expr(p):
  '''simple_expr : term
                  | simple_expr ADDOP simple_expr
                  | simple_expr mulop simple_expr
                  | LPAREN simple_expr RPAREN
                  | simple_expr QUESTION_MARK simple_expr COLON simple_expr
  '''
  # Implemente a ação semântica desejada para a regra simple_expr


def p_mulop(p):
  '''mulop : MULOP
            | AND
            | MOD
              
  '''
  # Implemente a ação semântica desejada para a regra simple_expr


def p_ADDOP(p):
  '''ADDOP : MINUS
            | ADD
            | OR
              
  '''
  # Implemente a ação semântica desejada para a regra simple_expr

def p_term(p):
  '''term : factor_a
          | term mulop factor_a
  '''
  # Implemente a ação semântica desejada para a regra term

def p_factor_a(p):
  '''factor_a : factor
              | NOT factor
              | MINUS factor
  '''
  # Implemente a ação semântica desejada para a regra factor_a

def p_factor(p):
  '''factor : IDENTIFIER
            | CONSTANT
            | LPAREN expression RPAREN
  '''
  # Implemente a ação semântica desejada para a regra factor







# Exemplo de uso do analisador sintático
if __name__ == '__main__':
    arquivos = os.listdir('./Testes/')
    for arquivo in arquivos:
              # Crie o analisador
        parser = yacc.yacc()
        lex = createLexer()
        
        caminho_arquivo = os.path.join('./Testes/', arquivo)
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_txt:
          programa = arquivo_txt.read()
          print(arquivo)
          result = parser.parse(programa)
         
