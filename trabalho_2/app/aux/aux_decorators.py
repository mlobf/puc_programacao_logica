from functools import wraps
from time import perf_counter, sleep


def get_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 3)
        print(f"O tempo total foi ->", total_time)

    return wrapper
