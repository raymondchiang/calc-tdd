from colorama import Fore, init
init(autoreset=True)
#-------------------------------
def str2int(lis):       #Convert str to int
    for x in range(len(lis)):
        lis[x]=conv_type(lis[x])
    return lis

def conv_type(number):
    if '.' in number:
        return float(number)
    return int(number)
#-------------------------------
def del_block(s):
    s+=['end',]
    x=0
    while(True):
        if s[x]=='end':
            del(s[x])
            break
        if s[x]==' ':
            del(s[x])
            x-=1
        x+=1
    return s
#-------------------------------
def split_str(stri):   #Split number and symbol
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
    return number,symbol
#-------------------------------
def mut_div(arr,sym): #calculate add,min,mut,div
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
    return sum(arr)
#-------------------------------
def pare(statement):   # parentheses " () ", To judge have parentheses or not
    fir_par_loc=0      # --->" ( "
    end_par_loc=0      # --->" ) "
    curr_par=0		   #content in one of parentheses
    have_par=False
    for x in range(len(statement)):
        if statement[x]=='(':
            have_par=True
            fir_par_loc=x
            curr_par+=1
        if statement[x]==')':
            break
        elif curr_par==2:
            curr_par=0
        end_par_loc+=1
    if have_par:
        return (fir_par_loc,end_par_loc)
    else:
        return (None,None)
#-------------------------------
def complete_statement(s):
    s=list(s)+['end',]
    x=0
    while(True):
        if (s[x]=='-'  or s[x]=='+')and s[x+1]=='(':
            s.insert(x+1,'1')
            x+=1
        x+=1
        if s[x]=='end':
            break
    x=0
    while(True):
        if s[x] in ['0','1','2','3','4','5','6','7','8','9']:
            if s[x+1]=='(':
                s.insert(x+1,'*')
                x+=1
        x+=1
        if s[x]=='end':
            del(s[x])
            break
    return s
#-------------------------------
def calc(statement):
    symbol=[]
    curr_state=[]    #current statement
    fir_par=0        # --->" ( "
    end_par=0        # --->" ) "
    statement=list(statement)
    statement=del_block(statement)
    statement=complete_statement(statement)
    while(True):
        fir_par,end_par=pare(statement)

        if fir_par==None:    # There is no any parentheses in the statement
            statement,symbol=split_str(statement)
            statement=str2int(statement)
            return mut_div(statement,symbol)

        curr_state=(statement[fir_par+1:end_par])
        curr_state,symbol=split_str(curr_state)
        curr_state=str2int(curr_state)
        curr_state=str(mut_div(curr_state,symbol))
        curr_state=list(curr_state)
        curr_state=curr_state[::-1]

        for x in range(end_par+1-fir_par):
            del(statement[fir_par])

        for x in range(len(curr_state)):
            statement.insert(fir_par,curr_state[x])
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
