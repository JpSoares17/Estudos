def cas(n, n2):
    return len(n)+len(n2)

def solt(n):
    return len(n)
    

def main():
    n = input('')
    c = int(input(''))
    if c==1:
        n2 = input('')
        print(cas(n, n2))
    if c==2:
        print(solt(n))
if __name__ == '__main__':
    main()
