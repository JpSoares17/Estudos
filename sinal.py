def cond(x):
    if x=='V':
        return 'Siga'
    if x=='A':
        return 'Atenção'
    if x=='E':
        return 'Pare'

def main():
    x = input('').upper()[0]
    print(cond(x))
if __name__ == '__main__':
    main()
