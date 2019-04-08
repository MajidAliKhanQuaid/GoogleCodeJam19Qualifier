import math


def SortLastThree(_decrypted, _val1, _val2):
    size = len(_decrypted)
    commonValue = None

    zeroIndex = _decrypted[size - 2]
    firstIndex = _decrypted[size - 1]

    if firstIndex != _val1:

        if zeroIndex == _val1 or firstIndex == _val1:
            commonValue = _val1
        if zeroIndex == _val2 or firstIndex == _val2:
            commonValue = _val2

        if firstIndex is not commonValue:
            hold = _decrypted[size - 2]
            _decrypted[size - 2] = _decrypted[size - 1]
            _decrypted[size - 1] = hold

        if _val1 is not commonValue:
            hold = _val1
            _val1 = _val2
            _val2 = hold

    return _val1, _val2


def GetFactors(_num, _primes, _decryted):
    if _decryted is not None:
        size = len(_decryted)
        if _num % _decryted[size - 1] == 0:
            multiplier = int(_num / _decryted[size - 1])
            return SortLastThree(_decryted, _decryted[size - 1], multiplier)
        if _num % _decryted[size - 2] == 0:
            multiplier = int(_num / _decryted[size - 2])
            return SortLastThree(_decryted, _decryted[size - 2], multiplier)

    for prime in _primes:
        if _num % prime == 0:
            multiplier = int(_num / prime)
            if IsPrime(multiplier):
                return prime, multiplier

    raise ValueError('Factors Not Found')


def IsPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    #upper_lim = int(math.sqrt(n)) + 1
    upper_lim = int(math.sqrt(n)) + 1
    return len([i for i in range(3, upper_lim, 2) if n % i == 0]) == 0


def GetPrimes(_primes, _max):
    N = _max
    while len(_primes) != 26:
        # if N % 2 == 0:
        #     N = N - 1
        if IsPrime(N):
            if N not in _primes:
                primes.append(N)
        N = N - 1

    if len(primes) > 0:
        primes.sort()

    return primes


def GetPrimeFactors(n):
    l = [(x, int(n/x)) for x in range(2, int(math.sqrt(n))+1) if n % x == 0]
    for element in l:
        if IsPrime(element[0]) and IsPrime(element[1]):
            return element
    return None


if __name__ == '__main__':
    ascii = [chr(x) for x in range(65, 91)]
    Iterations = int(input())
    for i in range(Iterations):
        decrypted = None
        N, L = [int(x) for x in input().split(' ')]
        encrptyed = [int(x) for x in input().split(' ')]
        primes = []
        # Getting Prime Number List
        for enc in encrptyed:
            fac1, fac2 = GetPrimeFactors(enc)

            if fac1 not in primes:
                primes.append(fac1)
            if fac2 not in primes:
                primes.append(fac2)

        GetPrimes(primes, N)

        for e in encrptyed:
            f1, f2 = GetFactors(e, primes, decrypted)
            if decrypted is None:
                decrypted = []
                decrypted.append(f1)
                decrypted.append(f2)

            else:
                decrypted.append(f2)
        lstAscii = [ascii[primes.index(x)] for x in decrypted]
        strDecrypted = ''.join(lstAscii)
        print('Case #{case}: {dec}'.format(case=i+1, dec=strDecrypted))
