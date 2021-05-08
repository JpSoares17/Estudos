def divi(do, dv):
    return do//dv, do%dv

def main():
    d1, d2 = float(input('')), float(input(''))
    q, r = divi(d1, d2)
    print('{:.4f}\n{:.4f}'.format(q, r))
if __name__ == '__main__':
    main()
