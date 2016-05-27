from .knowledge_node import KnowledgeNode
from .model import Model


class KnowledgeMap(object):
    _root_knowledge_node = None

    def __init__(self, model: Model):
        self._model = model

    def insert(self, knowledge_node: KnowledgeNode):
        self._model.insert(knowledge_node)

    def delete(self, knowledge_node):
        pass

    def update(self, knowledge_node):
        pass

    def find_by_kid(self, knowledge_node_id):
        pass

    def find_by_name(self, knowledge_node_name):
        pass
