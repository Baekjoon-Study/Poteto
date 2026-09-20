# 1075

if __name__ == '__main__':
    n = input()[:-2] + '00'
    f = int(input())

    n = int(n)

    for _ in range(100):
        if n % f == 0:
            break
        n += 1

    print(str(n)[-2:])