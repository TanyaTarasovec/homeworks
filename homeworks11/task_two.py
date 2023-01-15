class decorator:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        res = self._func(*args, **kwargs)
        print("Hello World")
        return res


@decorator
def test(a, b):
    return a, b


print(test(1, 2))
