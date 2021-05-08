def main():
    r = float(input(''))
    pi=3.141592
    c = 2*pi*r
    a = pi*r**2
    ae = 4*pi*r**2
    ve = (4/3)*pi*r**3
    print('{:.6f}\n{:.6f}\n{:.6f}\n{:.6f}'.format(c, a, ae, ve))
if __name__ == '__main__':
    main()
