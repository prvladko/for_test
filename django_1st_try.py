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

porsche = Car()
porsche.color = 'black'

ferrari = Car()
ferrari.color = 'red'

mini = Car()
mini.color = 'yellow'

print(mini.color)