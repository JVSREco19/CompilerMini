import ply.lex as lex
import os

# Lista de palavras-chave reservadas em Mini
reserved = {
    'program': 'PROGRAM',
    'begin': 'BEGIN',
    'end': 'END',
    'declare': 'DECLARE',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'do': 'DO',
    'while': 'WHILE',
    'for': 'FOR',
    'read': 'READ',
    'write': 'WRITE',
    'integer': 'INTEGER',
    'decimal': 'DECIMAL',
    'not': 'NOT',
    'or': 'OR',
    'to':'TO',
    'and':'AND',
    'mod':'MOD'
}


# Lista de tokens
tokens = [
    'IDENTIFIER',
    'CONSTANT',
    'LITERAL',
    'RELOP',
    'ADD',
    'MINUS',
    'MULOP',
    'SHIFTOP',
    'LPAREN',
    'RPAREN',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'ASSIGN',
    'COMMENT',
    'QUESTION_MARK',
    
] + list(reserved.values())

# Expressões regulares para os tokens

t_CONSTANT = r'\d+'
t_LITERAL = r'"[^"]*"'
t_RELOP = r'<=|>=|<>|<|>|='
t_ADD = r'\+'
t_MINUS = r'-'
t_MULOP = r'\*|\/'
t_SHIFTOP = r'<<|>>|<<<|>>>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r':='
t_QUESTION_MARK = r'\?'

# Defina uma expressão regular para palavras-chave insensíveis a maiúsculas e minúsculas
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER') # Verifica se está nas palabras reservadas, se nao estiver então é um ID
    return t

# Expressão regular para ignorar comentários de uma linha
def t_COMMENT(t):
    r'%.*'
    pass
# Expressão regular para rastrear números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

errorsList = []



# Função de manipulação de erro
def t_error(t):
    errorsList.append(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Ignora espaços em branco e tabulações
t_ignore = ' \t'


def createLexer():
    lexer = lex.lex()
    
    return lexer

# Exemplo de uso do lexer
def runLexer(arquivo_txt):
    tokList = []
    # Processar o arquivo .txt
    conteudo = arquivo_txt.read()
    # Criação do analisador léxico
    lexer = lex.lex()
    # Alimenta o lexer com o programa de teste
    lexer.input(conteudo)
    # Tokeniza o programa e preenche a tabela de símbolos
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokList.append(tok)
        
    return tokList



# Exemplo de uso do lexer
if __name__ == '__main__':
    arquivos = os.listdir('./Testes/')
    for arquivo in arquivos:
        
        caminho_arquivo = os.path.join('./Testes/', arquivo)
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_txt:
            tokList = runLexer(arquivo_txt)
            for i in tokList:
                print (i)
            