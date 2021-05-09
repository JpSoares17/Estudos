def eh_par(x, y, z):
    q=0
    x = [x, y, z]
    for i in x:
        if i%2==0:
            q+=1
    return q

def descomp(n):
    c = n//100
    n = n%100
    d = n//10
    u = n%10
    return c, d, u

def main():
    n = int(input(''))
    x, y, z = descomp(n)
    if 99<n<1000:
        print(f'{eh_par(x, y, z)}')
if __name__ == '__main__':
    main()
