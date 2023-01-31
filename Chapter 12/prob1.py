def readFile(fileName):
    try:
        with open(fileName,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {fileName} is not found ")

readFile('1.txt')
readFile('2.txt')
readFile('3.txt') 