import ply.yacc as yacc
from MiniLexer import tokens, errorsList,createLexer
import os
from symbols_table import SymbolTable 
# Definição das regras gramaticais


def p_program(p):
  '''program : PROGRAM IDENTIFIER body'''
  

def p_body(p):
  '''body : declare_opt BEGIN stmt_list END'''
  

def p_declare_opt(p):
  '''declare_opt : DECLARE decl_list'''
  
def p_decl_list(p):
  '''decl_list : decl  decl_list'''
  

def p_decl_list_single(p):
  '''decl_list : decl'''
  

def p_decl(p):
  '''decl : type ident_list SEMICOLON'''
  

def p_type(p):
  '''type : INTEGER 
  | DECIMAL'''
  

def p_ident_list(p):
  '''ident_list : IDENTIFIER COMMA ident_list'''
  
def p_ident_list_single(p):
  '''ident_list : IDENTIFIER'''
  
def p_stmt_list(p):
  '''stmt_list : stmt SEMICOLON stmt_list 
  '''
def p_stmt_list_single(p):
  '''stmt_list : stmt SEMICOLON
  '''
  
def p_stmt(p):
  '''stmt : if_stmt 
            | assign_stmt 
            | while_stmt 
            | do_while_stmt 
            | for_stmt 
            | read_stmt 
            | write_stmt 
  '''
  
def p_assign_stmt(p):
  '''assign_stmt : IDENTIFIER ASSIGN simple_expr'''
  
def p_if_stmt(p):
  '''if_stmt : IF condition THEN stmt_list END
              | IF condition THEN stmt_list ELSE stmt_list END
  '''
  
def p_do_while_stmt(p):
  '''do_while_stmt : DO stmt_list stmt_suffix'''

  
  
def p_stmt_suffix(p):
  '''stmt_suffix : WHILE condition'''
  
def p_for_stmt(p):
  '''for_stmt : FOR assign_stmt TO condition DO stmt_list END'''
  
def p_while_stmt(p):
  '''while_stmt : WHILE condition DO stmt_list END'''
  
def p_condition(p):
  '''condition : expression'''
  
def p_read_stmt(p):
 '''read_stmt : READ LPAREN IDENTIFIER RPAREN'''
  
def p_write_stmt(p):
  '''write_stmt : WRITE LPAREN writable RPAREN'''
  
def p_writable(p):
  '''writable : simple_expr
              | LITERAL
  '''
  
def p_expression(p):
  '''expression : simple_expr
                | expression RELOP expression
                
  '''
  
def p_simple_expr(p):
  '''simple_expr : term
                  | simple_expr ADDOP simple_expr
                  | simple_expr mulop simple_expr
                  | LPAREN simple_expr RPAREN
                  | simple_expr QUESTION_MARK simple_expr COLON simple_expr
  '''
  

def p_mulop(p):
  '''mulop : MULOP
            | AND
            | MOD
              
  '''
  

def p_ADDOP(p):
  '''ADDOP : MINUS
            | ADD
            | OR
              
  '''
  
def p_term(p):
  '''term : factor_a
          | term mulop factor_a
  '''
  
def p_factor_a(p):
  '''factor_a : factor
              | NOT factor
              | MINUS factor
  '''
  
def p_factor(p):
  '''factor : IDENTIFIER
            | CONSTANT
            | LPAREN expression RPAREN
  '''
  


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
         
