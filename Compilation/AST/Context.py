class Variable:
    def __int__(self, name):
        self.name = name


class Function:
    def __init__(self, name, params):
        self.name = name
        self.params = params


class Context:
    def __int__(self):
        self.local_var = []
        self.local_func = []
        self.children_context = []

    def create_child_context(self):
        children_context = Context()
        self.children_context.append(children_context)
        return children_context

    def define_var(self, name, value):
        a = Variable("hil", "8")
        


    @staticmethod
    def define_function(self, name, params):
        pass



