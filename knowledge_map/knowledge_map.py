from abc import ABCMeta, abstractmethod


class KnowledgeMap(object, metaclass=ABCMeta):
    _root_knowledge_node = None

    @abstractmethod
    def insert(self, knowledge_node, father_knowledge_node):
        pass

    @abstractmethod
    def delete(self, knowledge_node):
        pass

    @abstractmethod
    def update(self, knowledge_node):
        pass

    @abstractmethod
    def find_by_kid(self, knowledge_node_id):
        pass

    @abstractmethod
    def find_by_name(self, knowledge_node_name):
        pass
