"""Simple decorator implementation"""

from functools import wraps
from typing import Callable
from time import perf_counter, sleep


def get_time(func):
    """Simple decorator implementation"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Simple decorator implementation"""

        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 3)

        print(f"O tempo total foi ->", total_time)

    return wrapper


def repeat(times: int, msg: str):
    """repeat function call x amount of times"""

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = None
            for _ in range(times):
                value = func(*args, **kwargs)
            print(f"There is something to say to you------> {msg}")
            return value

        return wrapper

    return decorator


@repeat(2, "message in the botle")
def func1():
    print("hello")


@repeat(30, "Oi sono un ragazzo i mi chiamo Marcos")
def func2(a: int, b: int):
    print(a, b)


func1()
func2(1, 4)
