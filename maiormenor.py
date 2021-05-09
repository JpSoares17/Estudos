def cond(n):
    ma = n
    me = n
    for i in range(4):
        nr = int(input(''))
        if nr>ma:
            ma=nr
        if nr<me:
            me=nr
    return ma, me

def main():
    n = int(input())
    mr, ms = cond(n)
    print(f'{mr}\n{ms}')
if __name__ == '__main__':
    main()
