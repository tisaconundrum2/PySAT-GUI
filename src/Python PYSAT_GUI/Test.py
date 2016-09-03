def test():
    numbers = [x for x in range(1000)]
    for result in chunkit(numbers,100):
        print(result)

def chunkit(wholeList, chunkSize=100):
    """Yield successive n-sized chunks from wholeList."""
    for i in range(0, len(wholeList), chunkSize):
        last=i
        yield "{}-{}".format(i+last, i+(chunkSize+last))

test()

if __name__ == '__main__':
    test()