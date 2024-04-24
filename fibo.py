def recursive_nth_fibo(n):
    if n <= 1:
        return n
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    index = input('Kolik clenu Fibonacciho posloupnosti chcete zobrazit? ')
    index = int(index)
    seq = []
    for i in range(index):
        seq.append(recursive_nth_fibo(i))
    # jednoradkova syntax:
    # seq = [recursive_nth_fibo(i) for i in range(index)]
    print(seq)


if __name__ == "__main__":
    main()
