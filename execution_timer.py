import time

def timer(function):
    def f(*args, **kwargs):
        start = time.perf_counter()
        rv = function(*args, **kwargs)
        end = time.perf_counter()
        print("#########")
        print(f"**{function.__name__}** took {end - start:.6f} seconds to run.")
        return rv
    return f


def async_timer(func):
    async def f(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        print("#########")
        print(f"**{func.__name__}** took {end - start:.6f} seconds to run.")
        return result
    return f

@timer
def test_function():
    time.sleep(0.5)


@timer
def test_add(x, y=10):
    return x+y


if __name__ == "__main__":
    test_function()
    test_add(3,4)

