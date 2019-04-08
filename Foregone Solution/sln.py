def PairGenerator(_num, _case):
    lst = list(str(_num))
    for i in range(len(lst)):
        if lst[i] is '4':
            lst[i] = '3'

    firstNum = int(''.join(lst))
    secondNum = _num - firstNum
    print('Case #{case}: {first} {second}'.format(
        case=_case, first=firstNum, second=secondNum))


def Main():
    N = int(input())
    for i in range(N):
        fouredValue = int(input())
        PairGenerator(fouredValue, i+1)


if __name__ == '__main__':
    Main()
