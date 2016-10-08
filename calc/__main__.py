from colorama import Fore, init
init(autoreset=True)
#-------------------------------
def str_to_int(lis):
    for x in range(len(lis)):
        lis[x]=conv_type(lis[x])
    return lis

def conv_type(number):
    if '.' in number:
        return float(number)
    return int(number)
#-------------------------------
def split_str(stri):
    number=[]
    symbol=[]
    curr_num=[]
    for x in range(len(stri)):
        if stri[x]=='-':
            if len(curr_num):
                symbol+='+'
                number+=[''.join(curr_num),]
            curr_num=['-']
        elif stri[x] in ['+','*','/']:
            symbol+=stri[x]
            number+=[''.join(curr_num),]
            curr_num=[]
        else:
            curr_num+=stri[x]
        if x==len(stri)-1:
            number+=[''.join(curr_num),]
    return number, symbol
#-------------------------------
def muti_divi(arr,sym):
    sym+=['end',]
    length=len(sym)
    s=0
    while s<length:
        if sym[s]=='end':
            break
        if sym[s]=='*':
            arr[s]*=arr[s+1]
            del(arr[s+1])
            del(sym[s])
            continue
        if sym[s]=='/':
            arr[s]/=arr[s+1]
            del(arr[s+1])
            del(sym[s])
            continue
        s+=1
    del(sym[len(sym)-1])
    return (arr,sym)
#-------------------------------
def calc(statement):
    symbol=[]
    num=[]
    num,symbol=split_str(statement)
    num=str_to_int(num)
    num,symbol=muti_divi(num,symbol)
    return sum(num)
#-------------------------------
if __name__ == '__main__':
    while True:
        inputs = input('Input a statement: ' + Fore.YELLOW)
        evals = eval(inputs)
        print(Fore.CYAN + 'Excepted  : ' + str(evals))
        calcs = calc(inputs)
        color = Fore.GREEN if evals == calcs else Fore.RED
        print(color + 'Result    : ' + str(calcs))
        print()
