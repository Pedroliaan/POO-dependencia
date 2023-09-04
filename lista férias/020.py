class Animal:
    def emitir_som(self):
        return "som"
class Gato(Animal):
   def emitir_som(self):
       return "Miau"

class Cachorro(Animal):
   def emitir_som(self):
       return "Auau"
   
class Vaca(Animal):
   def emitir_som(self):
       return "MUUUUUU"
   
def fazer_sons(animais):
    for animal in animais:
        animal.emitir_som()
