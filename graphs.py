from typing import List, Union, Iterator

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
        Возвращает список всех ребер графа относительно вершины
        '''
        return self._graph_dict[vertice]
    
    def add_edge(self, edge: Union[set, list, tuple]):
        '''
        Предусматриваем, что ребро может быть подано в качестве
        параметра через типы list, set или tuple. При этом между
        вершинами может быть несколько ребер

        Если хотим использовать направленный граф, то нужно
        работать со списками ребер, ибо множество является
        неупорядоченным типом данных 
        '''
        edge = set(edge)
        vertex_1, vertex_2 = tuple(edge)

        for x, y in [(vertex_1, vertex_2), (vertex_2, vertex_1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]
    
    def all_edges(self) -> List[set]:
        '''
        Возвращает все ребра графа
        '''
        return self.__generate_edges()
    
    def __generate_edges(self) -> List[set]:
        '''
        Статический метод генерации ребер графа
        '''
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
        
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

    # Некоторые статические методы для полного описания класса:
    def __str__(self) -> str:
        '''
        Метолд для описания объекта класса в виде строки
        '''
        res = 'Vertices: '
        for k in self._graph_dict:
            res += str(k) + ' '
        res += '\nEdges: '
        for edge in self.__generate_edges():
            res += str(edge) + ' '
        return res

    def __iter__(self) -> Iterator:
        '''
        Возвращает итерируемый объект
        '''
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self) -> Iterator:
        '''
        Для прохождения по вершинам графа
        '''
