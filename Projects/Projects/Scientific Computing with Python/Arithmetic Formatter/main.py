def add(temp):
    a,b=temp
    ta,tb='',''
    if (len(a)>len(b)):
        offset=len(a)-len(b)        
        for _ in range(offset):
            tb+=' '
        b=tb+b

    else:
        offset=len(b)-len(a)
        for _ in range(offset):
            ta+=' '
        a=ta+a
    return a,b

def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    printa=[]
    printb=[]
    printruler=[]
    printr=[]
    for i in problems:
        temp=i.split(' ')
        a=temp[0]
        modifier=temp[1]
        b=temp[2]
        if modifier!='+' and modifier!='-':
            return  "Error: Operator must be '+' or '-'."
        if max(len(a),len(b))>4:
            return 'Error: Numbers cannot be more than four digits.'
        try:
            inta=int(a)
            intb=int(b)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        if modifier=='+':
            result=inta+intb
        else:
            result=inta-intb

        pa,pb=add([a,b])
        pa='  '+pa
        pb=modifier+' '+pb
        presult=''
        for _ in range(len(pa)-len(str(result))):
            presult+=' '
        presult+=str(result)
        printruler.append('-'*len(presult))
        printa.append(pa)
        printb.append(pb)
        printr.append(presult)
    if show_answers==1:
        rs='\n'.join(['    '.join(printa),'    '.join(printb),'    '.join(printruler),'    '.join(printr)])
    else:
        rs='\n'.join(['    '.join(printa),'    '.join(printb),'    '.join(printruler)])
    return rs
    

    

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
)