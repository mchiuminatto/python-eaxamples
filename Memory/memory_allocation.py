def foo(x):
    y = x**3
    print("foo locals", locals())
    return y

print(foo(3))
print("locals ", locals())

