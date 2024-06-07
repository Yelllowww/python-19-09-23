class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def set_x(self,novo_x):
        if type(novo_x) == int:
            self.x = novo_x
        else:
            print("Dados inconsistentes")
    def get_y(self):
        return self.y
    def set_y(self,novo_y):
        self.y = novo_y
    def __str__(self):
        return f"O elemento X é igual a {self.x}, e o elemento Y é igual a {self.y}"
    def distancia_origem(self):
        distancia = 2**(0 - self.x) + (0 - self.y)**2           # (xb - xa)² + (yb - ya)²
        return distancia
    def distancia_ponto(self,ponto):
        distancia = 2**(ponto.get_x() - self.x) + (ponto.get_y() - self.y)**2           # (xb - xa)² + (yb - ya)²
        return distancia
    def mais_distante(self,ponto):
        if (2**(0 - self.x) + (0 - self.y)**2) > (2**(0 - int(ponto.get_x())) + (0 - int(ponto.get_y())**2)):
            print("O ponto 1 é mais distante da origem")
        else:
            print("O ponto 2 é mais distante da origem")
    def retorna_mais_distante(self,ponto):
        if (2**(0 - self.x) + (0 - self.y)**2) > (2**(0 - int(ponto.get_x())) + (0 - int(ponto.get_y())**2)):
            return "O ponto 1 é mais distante da origem"
        else:
            return "O ponto 2 é mais distante da origem"
    def mostra_ponto_medio(self,ponto):
        resultado = ((self.x + int(ponto.get_x()) / 2)) + ((self.y + int(ponto.get_y()) / 2))
        return resultado
    def retorna_obj_ponto_medio(self,ponto):
        x = ((self.x + int(ponto.get_x()) / 2))
        y = ((self.y + int(ponto.get_y()) / 2))
        obj = Point(x,y)
        return obj
if __name__ == '__main__':
    objetoP1 = Point()
    objetoP2 = Point(2,3)
    objetoP3 = Point(3)
    objetoP4 = Point(3,2)
    print(objetoP1.get_x())
    print(objetoP1.get_y())
    print(objetoP2.get_x())
    print(objetoP2.get_y())
    print(objetoP3.get_x())
    print(objetoP3.get_y())
    print(objetoP4.get_x())
    print(objetoP4.get_y())
    print("Distância entre um ponto à origem:",objetoP2.distancia_origem())
    print("Distância entre dois pontos:",objetoP2.distancia_ponto(objetoP4))
    print(objetoP2.mais_distante(objetoP4))
    print(objetoP2.retorna_mais_distante(objetoP4))
    print("Ponto médio entre os pontos:",objetoP2.mostra_ponto_medio(objetoP4))
    print(objetoP2.retorna_obj_ponto_medio(objetoP4))


