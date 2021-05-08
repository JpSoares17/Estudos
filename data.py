def form(d, m, a):
    return f'{d}/{m}/{a}'

def main():
    d, m, a = int(input('')), int(input('')), int(input(''))
    print(form(d, m, a))
if __name__ == '__main__':
    main()
