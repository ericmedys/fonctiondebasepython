
def readfile():
    with open('file.txt', 'r') as f:
        result = f.read()
        print(result)
        return result


def writefile():
    with open('file_2.txt', 'w') as f:
        f.write(readfile())


if __name__ == '__main__':
    #readfile()
    writefile()



