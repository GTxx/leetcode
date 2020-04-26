def test(input, expect, fn):
    result = fn(*input)
    if result != expect:
        print(f"fail, input: {input}, result: {result}, expect: {expect}")