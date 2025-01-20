def generator(i):
    for n in range(i):
        yield i


print(generator(100))