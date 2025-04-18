import math

test = {
    'set':[1,2,5,8,9],
    'query':5,
    'output':2
}

def binary_search(list:list, query, u, v):
    p = u + math.floor(((v-u+1)/2))
    while (u<=v):
        if(list[p]==query):
            return f'index {p} : {list[p]}'
        elif(list[p]<query):
            u = p+1
            binary_search(list, query, u)
        else: #(list[p]>query)
            v = p-1
            binary_search(list,query,u,v)

res=binary_search(test['set'],test['query'],0,len(test['set'])-1)
print(res)