import time

class ExecutionTimer:
    def __init__(self):
        pass

    def measure_execution_time(self, function):
        start = time.perf_counter()
        function()
        end = time.perf_counter()
        print(f"{function.__name__} took {end - start:.6f} seconds to run.")


def test_function():
    time.sleep(0.5)

if __name__ == "__main__":
    perf = ExecutionTimer()

    perf.measure_execution_time(test_function)
    pass