def ehletra(c):
    if ord('A')<=ord(c)<=ord('Z') and c not in ['A', 'E', 'I', 'O', 'U']:
        return ord('A')<=ord(c)<=ord('Z') and c not in ['A', 'E', 'I', 'O', 'U']
    else:
        return ord('A')<=ord(c)<=ord('Z') and c not in ['A', 'E', 'I', 'O', 'U']

def main():
    x = input('').upper()
    print(ehletra(x))
if __name__ == '__main__':
    main()
