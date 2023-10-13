class SymbolTable:
    def __init__(self):
        self.table = {}

    def add(self, name, level, attribute):
        if name not in self.table:
            self.table[name] = {'level': level, 'attribute': attribute}

    def contains(self, name):
        return name in self.table

    def get_attributes(self, name):
        if name in self.table:
            return self.table[name]
        else:
            return None

    def get(self):
        return self.table

    def remove(self, name):
        if name in self.table:
            del self.table[name]
        else:
            print(f"Erro: Variável '{name}' não encontrada na tabela de símbolos.")

    def clear(self):
        self.table = {}
        
    

