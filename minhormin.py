def hor(mint):
    h=mint//60
    mints=mint%60
    return f'{h}h{mints}min'

def main():
    minu = int(input(''))
    print(hor(minu))
if __name__ == '__main__':
    main()
