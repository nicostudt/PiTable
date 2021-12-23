from games.lab.Node import Node


class Tree:

    def __init__(self):
        self.nodes = {}
        self.root = None
        self.leafs = []

    def createNode(self, pos):
        node = Node(pos)
        self.nodes[node.id] = node

    def getNode(self, pos):
        return self.nodes[hash(pos)]

    def setRoot(self, pos):
        self.root = self.getNode(pos)
        self.root.rootDist = 0

        for node in self.root.neighbors:
            node.wayNeights += 1

        self.leafs.append(self.root)

    def appendTo(self, parentNode, childNode):
        parentNode.children.append(childNode)

        childNode.parent = parentNode
        childNode.rootDist = parentNode.rootDist + 1

        for node in childNode.neighbors:
            node.wayNeights += 1

        self.leafs.append(childNode)