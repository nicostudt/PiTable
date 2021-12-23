class DFS():

    def __init__(self):
        self.finished = False
        self.currentNeights = []
        self.maxDist = 1


    def create(self, tree, goal):
        self.tree = tree
        self.goalPos = goal
        self.usedNodes = []
        self.stack = []
        self.addToStack(tree.root)


    def update(self, dt):
        for i in range(len(self.usedNodes)):
            self.usedNodes[i][1] += dt

        self.step()
        return self.finished


    def step(self):
        if not self.stack:
            self.finished = True
            return

        if not self.currentNeights:
            currentNode = self.stack[-1]
            del self.stack[-1]
            self.currentNeights = [x for x in currentNode.children]

        # Step through next neights one by one each step
        if self.currentNeights:
            nextNode = self.currentNeights[0]
            self.addToStack(nextNode)

            """
            # Check if next is goal
            if nextNode.pos == self.goalPos:
                self.finished = True
                return
            """
            del self.currentNeights[0]
            return


    def addToStack(self, node):
        self.stack.append(node)
        self.usedNodes.append([node, 0])
        self.maxDist = max(self.maxDist, node.rootDist)

    def getStack(self):
        return self.stack

