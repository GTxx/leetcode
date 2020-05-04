def iterable(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True


def test(input, expect, fn):
    if isinstance(input, (list, tuple)):
        result = fn(*input)
    else:
        result = fn(input)
    if result != expect:
        print(f"fail, input: {input}, result: {result}, expect: {expect}")