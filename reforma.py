def calc(a, c, l):
    ap = l*c
    vs = l*c*a
    apr = 2*a*l+2*a*c
    return f'{ap}\n{vs}\n{apr}'

def main():
    a, c, l = float(input('')), float(input('')), float(input(''))
    print(calc(a, c, l))
if __name__ == '__main__':
    main()
