class BasicTree:
    def __init__(self, data, children=None):
        if children is None:
            children = list()
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = '  ' * level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, BasicTree):
        self.children.append(BasicTree)


tree = BasicTree('Cars', [])

electric = BasicTree('electric', [])
gasoline = BasicTree('gasoline', [])

tree.add_child(electric)
tree.add_child(gasoline)

tesla = BasicTree('Tesla', [])
mercedes = BasicTree('Mercedes', [])

electric.add_child(tesla)
gasoline.add_child(mercedes)

print(tree)
