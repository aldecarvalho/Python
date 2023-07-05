import math
class Esfera:
    def _ini_(self, cor, raio):
        self .cor = cor
        self .raio = raio
    def volume (self):
        vol = (4/3)*math.pi*(self .raio **3)
        return vol

bola1 = Esfera('vermelha', 4)
bola2 = Esfera('azul', 7)

print(f 'O volume da bola 1 é    {bola1.volume()}cm^2')
print(f'A area superficial da bola 1 é {bola1, area()}cm^2')
print(bola1.volume())
prinf(Esfera.volume(bola1)) 