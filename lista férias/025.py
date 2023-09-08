class Relogio:
    def __init__(self, hora, minuto, segundo) -> int:
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    def anvacar(self,valor):
        self.segundo = self.seundo + valor
        if self.segundo == 60:
            self.minuto = self.minuto + 1
        elif self.segundo > 60:
            aumento = int(self.segundo /60)
            self.minuto = self.minuto + aumento
            self.segundo = self.segundo - (aumento * 60)      
        if self.minuto == 60:
            self.hora = self.hora + 1  
        elif self.minuto > 60:
             aumento = int(self.minuto /60)
             self.hora = self.hora + aumento
             self.minuto = self.minuto - (aumento * 60) 
        if self.hora == 24:
            self.hora = 00
        elif self.hora > 24:
            aumento = int(self.hora /24)
            self.hora = aumento
    def retroceder(self,valor):
         self.segundo = self.seundo - valor
         if self.segundo < 0:
            retrocede = valor/60
            self.segundo = 60 + self.segundo
            self.minuto = self.minuto - retrocede
         if self.minuto < 0:
             self.minuto = 60 + self.minuto
             self.hora = self.hora - 1
         if self.hora < 0:
             self.hora = 24 + self.hora
             