# args kwargs
def plus(*args):
    result = 0
    for x in args:
        result += x
    return result



summa = plus(1,2,1,1,1,1,2,1,1,12,1,1,1,1)
print(summa)