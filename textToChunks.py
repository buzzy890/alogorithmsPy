import math

def chunkenize(data:str, chunk_size:int): #my own algorithm
    chunkList = []
    iterationNumber = math.ceil((len(data)/chunk_size)) #returns the number of iterations to have chunks with maximum size as chunk_size and minimum as 1 character
    i = 0 #iterator
    c = 0 #current location in string
    while (i<=iterationNumber-1):
        chunk = data[c:c+chunk_size]
        chunkList.append(chunk)
        i+=1
        c+=chunk_size
    return chunkList

def chunkenize2(data: str, chunk_size: int): #chat gpt suggestion
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
