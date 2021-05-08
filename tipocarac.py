def cond(c):
    if ord('A')<=ord(c)<=ord('Z') and c in ['A', 'E', 'I', 'O', 'U']:
        return 'vogal'
    if ord('A')<=ord(c)<=ord('Z') and c not in ['A', 'E', 'I', 'O', 'U']:
        return 'consoante'
    if ord('0')<=ord(c)<=ord('9'):
        return 'número'
    else:
        return 'símbolo'

def main():
    x = input('').upper()
    print(cond(x))
if __name__ == '__main__':
    main()
