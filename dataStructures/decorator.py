import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.9f} seconds")
        return result
    return wrapper

@timer
def compute_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

compute_squares(1000000) 