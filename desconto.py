def fator(p):
    pf = 0.9*p
    return '{:.2f}'.format(pf)

def main():
    p = float(input(''))
    print(fator(p))
if __name__ == '__main__':
    main()
