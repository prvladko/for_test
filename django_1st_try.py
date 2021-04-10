# args kwargs
def plus(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a+b

plus(1,2,1,1,1,1,2,1,1,12,1,1,1,1, hello=True, goodbye=False, bipbop=4563)