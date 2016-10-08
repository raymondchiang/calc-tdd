#-------------------------------
def conv_type(number):
    if '.' in number:
        return float(number)
    return int(number)
#-------------------------------
def str_to_int(lis):
    for x in range(len(lis)):
        lis[x]=conv_type(lis[x])
    return lis
#-------------------------------
def split_str(stri):
    number=[]
    symbol=[]
    curr_num=[]
    if stri[0]=='-':
        stri='0'+stri
    for x in range(len(stri)):
        if stri[x]=='+' or stri[x]=='-' or stri[x]=='*' or stri[x]=='/' :
            symbol+=stri[x]
            number+=[''.join(curr_num),]
            curr_num=[]
        else:
            curr_num+=stri[x]
        if x==len(stri)-1:
            number+=[''.join(curr_num),]
    return (number,symbol)
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
def add_minus(num,sym):
    ans=num[0]
    for x in range(len(sym)):
        if sym[x]=='+':
            ans+=num[x+1]
        else:
            ans-=num[x+1]
    return ans
#-------------------------------
def calc(statement):
    symbol=[]
    num=[]
    ans=0
    num,symbol=split_str(statement)
    num=str_to_int(num)
    num,symbol=muti_divi(num,symbol)
    ans=add_minus(num,symbol)
    return (ans)
#-------------------------------
if __name__ == '__main__':
    while True:
        print(calc(input('Input a statement:')))
