#Расширение классов
class Car():
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seets = 5
        self.color = kwargs.get('color', 'black')
        self.price = kwargs.get('price', 0)

    def __str__(self):
        return f'Автомобиль с {self.wheels} колесами'

class Convertible(Car):
    def take_off(self):
        print('Крыша убрана')

class Coupe(Convertible):
    def somth(self):
        return


porsche = Coupe(color='green', price=100000)
print(porsche.wheels)
porsche.take_off()