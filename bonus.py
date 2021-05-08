def bonus(a, s):
    b = a*s
    return '{:.2f}'.format(b)

def main():
    a = int(input(''))
    s = float(input(''))
    print(bonus(a, s))
if __name__ == '__main__':
    main()
