def cond(d1, d2, m1, m2, a1, a2):
    if a1>a2 or (a1==a2 and m1>m2) or (a1==a2 and m1==m2 and d1>d2):
        return f'{d1}/{m1}/{a1}'
    if a2>a1 or (a1==a2 and m2>m1) or (a1==a2 and m1==m2 and d2>d1):
        return f'{d2}/{m2}/{a2}'
    if a1==a2 and m1==m2 and d1==d2:
        return f'{d1}/{m1}/{a1}'

def main():
    d1, m1, a1 = int(input('')), int(input('')), int(input(''))
    d2, m2, a2 = int(input('')), int(input('')), int(input(''))
    print(cond(d1, d2, m1, m2, a1, a2))
if __name__ == '__main__':
    main()
