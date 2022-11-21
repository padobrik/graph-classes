from typing import List

# Класс Graph работает с объектами, выступающими словарем:
# Ключ = вершина
# Значения = ребра

class Graph(object):

    def __init__(self, graph_dict=None):
        '''
        Инициализируем графовый объект, если словарь графа None,
        то работаем с пустым словарем
        '''

        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict
    
    def edges(self, vertice: List[str]) -> List[str]:
        '''
        Возвращает список всех ребер графа относительно вершин
        '''
        return self._graph_dict[vertice]
    
    def add_edge(self, edge):
        '''
        Предусматриваем, что ребро может быть подано в качестве
        параметра через типы list, set или tuple. При этом между
        вершинами может быть несколько ребер
        '''
        edge = set(edge)
        vertex_1, vertex_2 = tuple(edge)

        for x, y in [(vertex_1, vertex_2), (vertex_2, vertex_1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]
        
    def vertices(self) -> set:
        '''
        Возвращает список всех вершин графа
        '''
        return set(self._graph_dict.keys())

    def add_vertex(self, vertex: str):
        '''
        Если вершина vertex не в self._graph_dict, то добавляем
        ключ vertex с пустым списком в словарь
        '''    
        if vertex not in self._graph_dict.keys():
            self.graph_dict[vertex] = []    

    