def cond(d, m):
    if m==1 and d>19:
        return 'Aquário'
    if m==1 and d<=19:
        return 'Capricórnio'
    if m==2 and d>18:
        return 'Peixes'
    if m==2 and d<19:
        return 'Aquário'
    if m==3 and d<=20:
        return 'Peixes'
    if m==3 and d>=21:
        return 'Áries'
    if m==4 and d<=19:
        return 'Áries'
    if m==4 and d>=20:
        return 'Touro'
    if m==5 and d<=20:
        return 'Touro'
    if m==5 and d>=21:
        return 'Gêmeos'
    if m==6 and d<=21:
        return 'Gêmeos'
    if m==6 and d>=22:
        return 'Câncer'
    if m==7 and d<=22:
        return 'Câncer'
    if m==7 and d>=23:
        return 'Leão'
    if m==8 and d<=22:
        return 'Leão'
    if m==8 and d>=23:
        return 'Virgem'
    if m==9 and d<=22:
        return 'Virgem'
    if m==9 and d>=23:
        return 'Libra'
    if m==10 and d<=22:
        return 'Libra'
    if m==10 and d>=23:
        return 'Escorpião'
    if m==11 and d<=21:
        return 'Escorpião'
    if m==11 and d>=22:
        return 'Sagitário'
    if m==12 and d<=21:
        return 'Sagitário'
    if m==12 and d>=22:
        return 'Capricórnio'

def main():
    d, m = int(input('')), int(input(''))
    print(cond(d, m))
if __name__ == '__main__':
    main()
