
def readfile():
    with open('file.txt', 'r') as f:
        result = f.read()
        print(result)
        return result


def writefile():
    with open('file_2.txt', 'w') as f:
        f.write(readfile())


def boucle_for():
    for i in range(10):
        print('{}^2 = {} '.format(i, i**2))


if __name__ == '__main__':
    #readfile()
    #writefile()
    boucle_for()



