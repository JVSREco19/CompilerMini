import ply.lex as lex

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
    'and': 'AND',
    'or': 'OR',
    'mod': 'MOD',
}

# Tabela de símbolos
symbol_table = {}

# Lista de tokens
tokens = [
    'IDENTIFIER',
    'CONSTANT',
    'LITERAL',
    'RELOP',
    'ADDOP',
    'MULOP',
    'SHIFTOP',
    'LPAREN',
    'RPAREN',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'ASSIGN',
    'COMMENT'
] + list(reserved.values())

# Expressões regulares para os tokens

t_CONSTANT = r'\d+'
t_LITERAL = r'".*?"'
t_RELOP = r'<=|>=|<>|<|>|='
t_ADDOP = r'\+|-'
t_MULOP = r'\*|/|\band\b|\bmod\b'
t_SHIFTOP = r'<<|>>|<<<|>>>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r':='
t_IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
# Expressão regular para ignorar comentários de uma linha
def t_COMMENT(t):
    r'%.*'
    pass

# Expressão regular para rastrear números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função de manipulação de erro
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Ignora espaços em branco e tabulações
t_ignore = ' \t'

# Função para adicionar variáveis à tabela de símbolos
def add_to_symbol_table(name, type):
    if name in symbol_table:
        
        #print(f"Erro: Variável '{name}' já declarada na linha {symbol_table[name]['line']}.")
        pass
    else:
        symbol_table[name] = {'type': type, 'line': lexer.lineno}



# Exemplo de uso do lexer
if __name__ == '__main__':
    import os
    
    
    
    arquivos = os.listdir('./Testes/')
    for arquivo in arquivos:
        caminho_arquivo = os.path.join('./Testes/', arquivo)
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_txt:
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
                if tok.type == 'IDENTIFIER':
                    add_to_symbol_table(tok.value, 'unknown')
                print(tok)
            
            print("------------------------------------------------")
            
            # Exibindo a tabela de símbolos após o término da análise
            print("\nTabela de Símbolos:")
            for var, info in symbol_table.items():
                print(f"Nome: {var}, Tipo: {info['type']}, Linha de Declaração: {info['line']}")
            
            # Tabela de símbolos
            symbol_table = {}
            print("\n###############################################")