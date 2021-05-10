def main():
    p=0
    imp=0
    for i in range(100):
        n=int(input(''))
        if n%2==0:
            p+=1
        if n%2!=0:
            imp+=1
    print(f'{p}\n{imp}')
if __name__ == '__main__':
    main()
    
