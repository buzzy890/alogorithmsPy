import math
import uuid

class ListElement:
    def __init__(self, id, data, headId, prevId=None, nextId=None, isHead=False):
        self.id = id
        self.isHead=isHead
        self.nextId=nextId
        self.data = data
        self.headId = headId
        self.prevId=prevId

def createLinkedlist(data:str, chunk_size:int):
    dataChunks = chunkenize(data, chunk_size)
    elementList = []
    id = str(uuid.uuid4())
    headId = id
    prevId = None
    for i in range(len(dataChunks)):
        isHead = True if i == 0 else False
        nextId=str(uuid.uuid4()) if (i != (len(dataChunks)-1)) else None #pre-generates the id of the next node
        newEl = ListElement(id, dataChunks[i], headId, prevId, nextId, isHead)
        elementList.append(newEl)
        prevId = id #important moment. You write current ID to prevID before changing it to already chanerated Id of the next node
        id = nextId
    return elementList

def chunkenize(data: str, chunk_size: int): #chat gpt suggestion
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

testData = ["smdjrnjhgfe", "dieij", "ji", "", "Curiosity fuels the mind like sunlight fuels the growth of a tree"]

linkedList = createLinkedlist(testData[4],5)
for i in range(len(linkedList)):
    print(f"data: {linkedList[i].id} prevID: {linkedList[i].nextId}")