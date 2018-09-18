

class Task:
    __name = ''
    __complete_by = None
    __cost_point = 0

    def __init__(self, name, complete_by=None, cost_point=0):
        self.__name = name
        self.__complete_by = complete_by
        self.__cost_point = cost_point

    def get_cost_point(self):
        return self.__cost_point

    def set_cost_point(self, new_cost_point:int):
        self.__cost_point = new_cost_point

    def __str__(self):
        return self.__name