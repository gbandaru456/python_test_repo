from functools import wraps

def print_decorator(func):
    @wraps(func)
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
    
@print_decorator
def sya_hollo():
    print('Hello world')

sya_hollo()
        
