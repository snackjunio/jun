def main():
    try:
        a = int(input('nを入力ください：'))
        for r in range(1,a+1,1):
            for b in range(1,(a-r)+1,1):
                print('\t',end='')
            for c in range(1,(2*r-1)+1,1):
                print('  ',c,end='')
            print('\n')
    except:
        raise

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)