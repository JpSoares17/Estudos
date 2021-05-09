def cond(k):
    if k<18.5:
        return 'Abaixo do peso'
    if k>=18.5 and k<25:
        return 'Peso normal'
    if k>=25 and k<30:
        return 'Sobrepeso'
    if k>=30 and k<35:
        return 'Obeso leve'
    if k>=35 and k<40:
        return 'Obeso moderado'
    if k>=40:
        return 'Obeso mórbido'

def imc(m, a):
    return m/a**2

def main():
    m, a = float(input('')), float(input(''))
    k = imc(m, a)
    print(f'{k}', cond(k), sep='\n')
if __name__ == '__main__':
    main()
