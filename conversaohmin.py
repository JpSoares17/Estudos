def proc(h, m, s):
    t = h*3600+m*60+s
    return f'{t}'

def main():
    h, m, s = int(input('')), int(input('')), int(input(''))
    print(proc(h, m, s))
if __name__ == '__main__':
    main()
