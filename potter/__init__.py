
__all__ = []

def _magic():
    import time, random

    originalstring = '          Harry Potter says "imports are magic!"' 
    string = list(originalstring)

    d = {}
    for i, ch in enumerate(string):
        d[i] = ch

    first, rest = [], string

    for i in range(len(string)):
        print(''.join(first + rest), end='\r')
        time.sleep(0.1)

        random.shuffle(string)
        first.append(originalstring[i])
        rest.pop(rest.index(originalstring[i]))
     
    print(originalstring)

_magic()
