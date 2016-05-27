class KnowledgeNode(object):
    _kid = None         # type: int
    _name = None        # type: str
    _fathers = []       # type: list[Knowledge]
    _children = []      # type: list[Knowledge]
    _describe = None    # type: str

    def put_name(self, name: str):
        self._name = name

    def put_describe(self, describe: str):
        self._describe = describe

    def put_father(self, father):
        """
        :type father KnowledgeNode
        """
        # TODO: Following PEP484
        self._fathers.append(father)

    def put_fathers(self, fathers: list):
        for father in fathers:
            self.put_father(father)

    def put_child(self, child):
        """
        :type child KnowledgeNode
        """
        # TODO: Following PEP484
        self._children.append(child)

    def put_children(self, children: list):
        for child in children:
            self.put_child(child)
