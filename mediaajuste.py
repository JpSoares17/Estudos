def medcond(n1, n2, n3):
    m = (n1+n2+n3)/3
    if n3>8 and m<=9:
        m+=1
        return '{:.2f}'.format(m)
    if n3>8 and m>9:
        return '10'
    else:
        return '{:.2f}'.format(m)

def main():
    n1, n2, n3= float(input('')), float(input('')), float(input(''))
    print(medcond(n1, n2, n3))
if __name__ == '__main__':
    main()
