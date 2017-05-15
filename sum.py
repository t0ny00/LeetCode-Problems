def sum(list, targ):
    dic = {}
    for i in range(len(list)):
        if(not targ-list[i] in dic) : dic[list[i]]=i
        else :
            return [dic[targ-list[i]],i]

if __name__ == '__main__':
    lis = [2, 7, 11, 15]
    targ = 17
    print (sorted(sum (lis,targ)))