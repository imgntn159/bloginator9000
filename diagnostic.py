import time
from functools import wraps

def funcTime(f):
    @wraps(f)
    def inner(*args):
        start = time.time()
        function = f(*args)
        print f.func_name + str(args) + ": " + str(time.time() - start)
        return function
    return inner
