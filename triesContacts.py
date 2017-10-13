class node:
    def __init__(self):
        self.children = {}
        self.numEntries = 0


def addNode(parent, word, place):
    child = node()
    children = parent.children
    if word[place - 1] in children:
        child = children[word[place - 1]]
    if place == len(word):
        child.numEntries = 1
    else:
        addNode(child, word, place + 1)
    parent.numEntries += 1
    children[word[place - 1]] = child


def findEndOfWord(node, word, place):
    if place == len(word):
        return node
    children = node.children
    if word[place] not in children:
        return None
    child = children[word[place]]
    return findEndOfWord(child, word, place + 1)


contacts = node()


def add(name):
    addNode(contacts, name, 1)


def find(partial):
    node = findEndOfWord(contacts, partial, 0)
    if node == None:
        print(0)
    else:
        print(node.numEntries)


stringToMethod = {
    "add": add,
    "find": find
}

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    stringToMethod[op](contact)
