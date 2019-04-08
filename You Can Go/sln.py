N = int(input())
for i in range(N):
    count = input()
    movement = input()
    lstOpponent = list(movement)
    lstMe = list(movement)
    for j in range(len(lstMe)):
        if lstMe[j] == 'S':
            lstMe[j] = 'E'
        else:
            lstMe[j] = 'S'
    print('Case #{case}: {pattern}'.format(case=i+1, pattern=''.join(lstMe)))
