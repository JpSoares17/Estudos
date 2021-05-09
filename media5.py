def media(s):
    return s/5

def main():
    s=0
    x=[]
    for i in range(5):
        n = int(input(''))
        s+=n
        x.append(n)
    m= media(s)
    print(f'{m}')
    for y in x:
        if y>m:
            print(y)
if __name__ == '__main__':
    main()
