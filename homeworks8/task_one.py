def text_up(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
    return wrap


@text_up
def get_text(*args):
    return ' '.join(args)


print(get_text('Hello', 'word'))
