def fib(n):
    try:
        a,b = 1,0
        for i in range(n+1):
            print('Fib(',i,')=',a)
            a, b = a + b, a
    except:
        raise

if __name__ == '__main__':
    try:
        n = int(input('フィボナッチ数を入力ください：\n 例：Fib(5)-> 5を入力\n'))
        fib(n)
    except Exception as e:
        print(e)