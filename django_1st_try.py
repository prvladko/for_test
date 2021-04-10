#Методы part 2
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

porsche = Car(color='green', price=100000)

ferrari = Car(color='red', price=200000)

mini = Car()

print(porsche.color, porsche.price)
print(mini.color, mini.price)