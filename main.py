
def readfile():
    with open('file.txt', 'r') as f:
        result = f.read()
        print(result)
        return result


def writefile():
    with open('file_2.txt', 'w') as f:
        f.write(readfile())


def boucle_for():
    for j in range(10):
        print('{}^2 = {} '.format(j, j**2))

def boucle_whiel():
    i = 0
    while i < 10:
        print('{}^4 = {}'.format(i, i**4))
        i += 1


def message():
    print("hello sabrina how are you")


if __name__ == '__main__':
    readfile()
    writefile()
    #boucle_for()
    #boucle_while()
   # message()





