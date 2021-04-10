# args kwargs

def plus(*args):
    result = 0
    for x in args:
        result += x
    return result



summa = plus(1,2,1,1,1,1,2,1,1,12,1,1,1,1)
print(summa)

# Основы ООП

class Car():
    wheels = 4
    doors = 4
    windows = 4
    seets = 5

    def start(self):
        print(self.color)
        print('Двигатель запущен')

porsche = Car()
porsche.color = 'black'
porsche.start()

ferrari = Car()
ferrari.color = 'red'

mini = Car()
mini.color = 'yellow'

print(mini.color)

#Методы ^^^ part 1