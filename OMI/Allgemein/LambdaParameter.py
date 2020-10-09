# Beispiel für eine Function als Parameter

def runlambda(f, args):
    return f(args)


def f1(x):
    return x**x


#print(f1(5))

print(runlambda(f1, 5))


