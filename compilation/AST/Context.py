class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Function:
    def __init__(self, func):
        self.name = func.idx
        self.params = func.params
        self.stat_list = func.stat_list


class Context:
    def __init__(self, parent=None):
        self.local_var = []
        self.local_func = []
        self.children_context = []
        self.parent = parent

    def create_child_context(self):
        children_context = Context(self)
        self.children_context.append(children_context)
        return children_context

    def def_var(self, name, value):
        var = Variable(name, value)
        self.local_var.append(var)

    def redef_var(self, name, value):
        for var in self.local_var:
            if var.name == name:
                var.value = value

    def def_function(self, func):
        function = Function(func)
        self.local_func.append(function)

    def check_var_defined(self, name):
        for var in self.local_var:
            if var.name == name:
                return 1
        return self.parent is not None and self.parent.is_var_defined(name)

    def check_func_defined(self, name, num_params):
        for func in self.local_func:
            if func.name == name and len(func.params) == num_params:
                return 1
        return self.parent is not None and self.parent.is_func_defined(name, num_params)

    def is_local_var(self, name):
        return self.get_local_variable_info(name) is not None

    def is_local_func(self, name, params):
        return self.get_local_function_info(name, params) is not None

    def get_local_variable_info(self, name):
        for var in self.local_var:
            if var.name == name:
                return var.value
        if self.parent is None:
            return None
        else:
            return self.parent.get_local_variable_info(name)

    def get_local_function_info(self, name, num_params):
        for func in self.local_func:
            if func.name == name and len(func.params) == num_params:
                return func
        if self.parent is None:
            return None
        else:
            return self.parent.get_local_function_info(name, num_params)

