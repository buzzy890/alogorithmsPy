import math
import random


class ListElement:
    def __init__(self, id, nextId=None, isHead=False):
        self.id = id
        self.isHead=isHead
        self.nextId=nextId
        data = []

def createLinkedlist():
    ran = random.randint(2, 10)
    elementList = []
    id = random.random()
    for i in range(ran):
        nextId=random.random() if (i != (ran-1)) else None #next = random.random
        newEl = ListElement(id, nextId)
        elementList.append(newEl)
        id = nextId
    return elementList

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

def chunkenize(data: str, chunk_size: int): #chat gpt suggestion
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

testData = ["smdjrnjhgfe", "dieij", "ji", ""]

for i in range(len(testData)):
    print(chunkenize(testData[i],5))

# linkedList = createLinkedlist()
# for i in range(len(linkedList)):
#     print(f"id: {linkedList[i].id} next {linkedList[i].nextId} ")