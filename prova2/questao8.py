class Mãe:
    def cor_olho(self):
        print('olhos verdes da mãe')
class Pai: 
    def tom_voz(self):
        print('voz grave do pai')
class Filho(Mãe,Pai):
    def cor_olho(self):
        print('olhos marrons do pai')
    def tom_voz(self):
        print('voz doce da mãe')
if __name__ == '__main__':
    fi = Filho()
    fi.cor_olho()
    fi.tom_voz()