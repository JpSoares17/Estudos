def eh_vogal(c):
    if c in ['A', 'E', 'I', 'O', 'U']:
        return c in ['A', 'E', 'I', 'O', 'U']
    else:
        return c in ['A', 'E', 'I', 'O', 'U']

def main():
    c = input('').upper()
    print(eh_vogal(c))
if __name__ == '__main__':
    main()
