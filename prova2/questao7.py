class Animal:
    titulo = 'Dados do animal:'
    def raca(self):
        return "Animal não definido"
    def numero_patas(self):
        return "Animal não definido"
    def tipo_ambiente(self):
        return "Animal não definido"
class Carcara(Animal):
    def raca(self):
        return "Carcará"
    def numero_patas(self):
        return "Duas patas"
    def tipo_ambiente(self):
        return "Sertão nordestino"
class Bode(Animal):
    def raca(self):
        return "Bode(masculino de cabra)"
    def numero_patas(self):
        return "4 patas"
    def tipo_ambiente(self):
        return "ambientes secos em geral"
if __name__ == '__main__':
    animal1 = Bode()
    animal2 = Carcara()
    print(animal1.titulo,' | ', animal1.raca() , ' | ' , animal1.numero_patas() , ' | ' ,animal1.tipo_ambiente())
    print(animal2.titulo,' | ', animal2.raca() , ' | ' , animal2.numero_patas() , ' | ' ,animal2.tipo_ambiente())
   