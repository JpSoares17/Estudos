def cond(c):
    if ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9'):
        return ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9')
    else:
        return ord('A')<=ord(c)<=ord('Z') or ord('0')<=ord(c)<=ord('9')

def main():
    x = input('').upper()
    print(cond(x))
if __name__ == '__main__':
    main()
