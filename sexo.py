def cond(s, n):
    if s==1:
        return f'Ilmo Sr. {n}'
    if s==2:
        return f'Ilma Sra. {n}'

def main():
    n = input('')
    s = int(input(''))
    print(cond(s, n))
if __name__ == '__main__':
    main()
