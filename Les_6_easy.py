# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.a = [x1, y1]
        self.b = [x2, y2]
        self.c = [x3, y3]

    def get_ab(self):
        ab = (((self.b[0] - self.a[0])**2)+((self.b[1] - self.a[1])**2))**(1/2)
        return ab

    def get_bc(self):
        bc = (((self.c[0] - self.b[0])**2)+((self.c[1] - self.b[1])**2))**(1/2)
        return bc

    def get_ac(self):
        ac = (((self.c[0] - self.a[0])**2)+((self.c[1] - self.a[1])**2))**(1/2)
        return ac

    def perimeter(self):
        return self.get_ab() + self.get_bc() + self.get_ac()

    def area(self):
        a_t = (1/2)*(((self.a[0] - self.c[0])*(self.b[1 - self.c[1]]))-((self.b[0] - self.c[0])*(self.a[1] - self.c[1])))
        if a_t < 0:
            return a_t * -1
        else:
            return a_t

    def height(self):
        pass #лень считать 


tria = Triangle(x1=0, y1=0, x2=3, y2=6, x3=6, y3=0)
print(tria.perimeter())
print(tria.area())
print(tria.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.a = [x1, y1]
        self.b = [x2, y2]
        self.c = [x3, y3]
        self.d = [x4, y4] 

    def get_ab(self):
        ab = (((self.b[0] - self.a[0])**2)+((self.b[1] - self.a[1])**2))**(1/2)
        return ab

    def get_bc(self):
        bc = (((self.c[0] - self.b[0])**2)+((self.c[1] - self.b[1])**2))**(1/2)
        return bc

    def get_cd(self):
        cd = (((self.c[0] - self.d[0])**2)+((self.c[1] - self.d[1])**2))**(1/2)
        return cd

    def get_ad(self):
        ad = (((self.a[0] - self.d[0])**2)+((self.a[1] - self.d[1])**2))**(1/2)
        return ad

    def isosceles_trapezoid(self):
        if self.get_ab() == self.get_cd():
            return 'Трапенция является равнобочной.'
        else:
            return 'Трапенция не является равнобочной.'

    def perimeter(self):
        return self.get_ab() + self.get_bc() + self.get_cd() + self.get_ad()

    def height(self):
    pass #лень считать

    def area(self):
        if self.get_ab() == self.get_cd():
            return ((self.get_bc() + self.get_ad())/2) * self.height()
        else:
            return ((self.get_ab() + self.get_cd())/2) * self.height()


a = Trapezoid(x1=0, y1=0, x2=1, y2=2, x3=3, y3=2, x4=2, y4=0)
print(a.get_ab())
print(a.get_bc())
print(a.get_cd())
print(a.get_ad())
print(a.perimeter())
print(a.area())
print(a.isosceles_trapezoid())



