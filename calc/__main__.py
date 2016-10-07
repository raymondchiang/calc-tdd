# raymond_calc_main

def calc(statement):
    add='+'
    minus='-'
    muti='*'
    allnum=statement.split(add)
    for x in range(len(allnum)):
        if '.' in allnum[x]:
            allnum[x]=float(allnum[x])
            continue
        allnum[x]=int(allnum[x])
    return sum(allnum)


if __name__ == '__main__':
    while True:
        print(calc(input('Input a statement:')))
