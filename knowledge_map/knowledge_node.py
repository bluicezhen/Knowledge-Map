class KnowledgeNode(object):
    _kid = None
    _name = None
    _describe = None

    def __init__(self, kid, name, describe):
        self._kid = kid
        self._name = name
        self._describe = describe
