from colorama import Fore, init
init(autoreset=True)

#-------------------------------
def conv_sym(num):
    if '.' in num:
        return float(num)
    return int(num)
#-------------------------------
def conv_str(lis):
    for x in range(len(lis)):
        lis[x]=conv_sym(lis[x])
    return lis
#-------------------------------
def calc(statement):
    add='+'
    minus='-'
    symbol=[]
    num=[]
    curr_num=[]
    ans=0
    if statement[0]==minus:
        statement='0'+statement
    for x in range(len(statement)):
        if statement[x]==add or statement[x]==minus:
            symbol+=statement[x]
            num+=[''.join(curr_num),]
            curr_num=[]
        else:
            curr_num+=statement[x]
        if x==len(statement)-1:
            num+=[''.join(curr_num),]

    num=conv_str(num)
    ans=num[0]
    for x in range(len(num)-1):
        if symbol[x]==add:
            ans+=num[x+1]
        else:
            ans-=num[x+1]
    return ans

if __name__ == '__main__':
    while True:
        inputs = input('Input a statement: ' + Fore.YELLOW)
        evals = eval(inputs)
        print(Fore.CYAN + 'Excepted  : ' + str(evals))
        calcs = calc(inputs)
        color = Fore.GREEN if evals == calcs else Fore.RED
        print(color + 'Result    : ' + str(calcs))
        print()
