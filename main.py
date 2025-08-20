class ContaBancaria:
    def __init__(self,titular, saldo=0):
        
        self._saldo = saldo
        self.titular = titular
 
# Método para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False
    
    # Getter para obter o saldo
    
    def get_saldo(self):
        return self._saldo
    