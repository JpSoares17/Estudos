def cond(a, aa, m, ma, d, da):
    i = a-aa
    if ma>m or (m==ma and da>d):
        i-=1
    return i

def main():
    d, m, a = int(input('')), int(input('')), int(input(''))
    da, ma, aa = int(input('')), int(input('')), int(input(''))
    print(cond(a, aa, m, ma, d, da))
if __name__ == '__main__':
    main()
