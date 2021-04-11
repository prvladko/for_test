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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_to_take_off = 30

    def take_off(self):
        print('Крыша убрана')

    def __str__(self):
        return f'Кабриолет с {self.wheels} колесами и убираемой крышей'



porsche = Convertible(color='green', price=100000)
print(porsche.wheels)