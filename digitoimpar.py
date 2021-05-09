def cond(q):
    if q==0:
        return 'Nenhum dígito é ímpar.'
    if q==1:
        return 'Apenas um dígito é ímpar.'
    if q==2:
        return 'Os dois dígitos são ímpares.'
        

def descomp(n):
    d = n//10
    u = n%10
    return d, u

def eh_impar(x, y):
    x = [x, y]
    q=0
    for i in x:
        if i%2!=0:
            q+=1
    return q
            

def main():
    n = int(input(''))
    x, y = descomp(n)
    z = eh_impar(x, y)
    if 9<n<100:
        print(cond(z))
if __name__ == '__main__':
    main()
