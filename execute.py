
class BasicExecute:
    
    def __init__(self, tree, env):
        self.env = env
        self.tree = tree
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)



    def walkTree(self, node):
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if node is None:
            return None

        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        if node[0] == 'num':
            return node[1]

        if node[0] == 'str':
            return node[1]
        if node[0] == 'big':
            is1 = self.walkTree(node[1]) > self.walkTree(node[2])
            return is1
   
        if node[0] == 'small':
            is1 = self.walkTree(node[1]) < self.walkTree(node[2])
            return is1
        if node[0] == 'add':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'mul':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'div':
            return self.walkTree(node[1]) / self.walkTree(node[2])
        elif node[0] == 'ifsame':
            is1 = self.walkTree(node[1]) == self.walkTree(node[2])
            return is1
        elif node[0] == 'if':
            # print(parsed)
            # print(node[1][1][0])
            result = self.walkTree(node[1][0])
            if result:
                block = self.walkTree(node[1][1][0])
                return block
        elif node[0] == 'ifelse':
            # print(parsed)
            #print(node[1][2][0])
            result = self.walkTree(node[1][0])
            if result:
                block = self.walkTree(node[1][1][0])
                return block
            else:
                block = self.walkTree(node[1][2][0])
                return block
        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]
        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '"+node[1]+"' found!")
                return 0
