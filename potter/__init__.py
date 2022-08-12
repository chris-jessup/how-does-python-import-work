
__all__ = []

def _magic():
    import time, random

    originalstring = '          Harry Potter says "imports are magic!"' 

    first, rest = [], list(originalstring)

    for i in range(len(originalstring)):
        print(''.join(first + rest), end='\r')
        time.sleep(0.1)

        random.shuffle(rest)
        first.append(originalstring[i])
        rest.pop(rest.index(originalstring[i]))
     
    print(originalstring)

_magic()
