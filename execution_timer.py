import time

# def timer(function):
#     def f(*args, **kwargs):
#         start = time.perf_counter()
#         rv = function(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"**{function.__name__}** took {end - start:.6f} seconds to run.")
#         return rv
#     return f()

def timer_simple(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    print(f"**{func.__name__}** took {end - start:.6f} seconds")


def test_function():
    time.sleep(0.5)


def test_add(x, y=10):
    return x+y


if __name__ == "__main__":
    timer_simple(test_function)
    timer_simple(test_add,3,4)

