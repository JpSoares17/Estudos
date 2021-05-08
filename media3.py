def med(a, b, c):
    m = (a+b+c)/3
    return f'{m}'

def main():
    a, b, c = int(input('')), int(input('')), int(input(''))
    print(med(a, b, c))
if __name__ == '__main__':
    main()
