import sys

cdef extern from "Python.h":
    ctypedef struct PyModuleDef:
        const char* m_name;

    void Py_INCREF(object)
    object PyModule_FromDefAndSpec(PyModuleDef *definition, object spec)
    int PyModule_ExecDef(object module, PyModuleDef* definition)

cdef extern from "dummy.h":
    object PyInit_b7f506f8b9903ccfc6daecc100c7adc3e47b15ec078b84f5723ccf63b6f66f95()

cdef object get_definition_by_name(str name):
    if name == "app.dummy":
        return PyInit_b7f506f8b9903ccfc6daecc100c7adc3e47b15ec078b84f5723ccf63b6f66f95()


cdef class CythonPackageLoader:
    cdef PyModuleDef* definition
    cdef object def_o
    cdef str name

    def __init__(self, name):
        self.def_o = get_definition_by_name(name)
        self.definition = <PyModuleDef*>self.def_o
        self.name = name
        Py_INCREF(self.def_o)

    def load_module(self, fullname):
        raise ImportError

    def create_module(self, spec):
        if spec.name != self.name:
            raise ImportError()
        return PyModule_FromDefAndSpec(self.definition, spec)

    def exec_module(self, module):
        PyModule_ExecDef(module, self.definition)


class CythonPackageMetaPathFinder:
    def __init__(self, modules_set):
        self.modules_set = modules_set

    def find_module(self, fullname, path):
        if fullname not in self.modules_set:
            return None
        return CythonPackageLoader(fullname)

    def invalidate_caches(self):
        pass

def bootstrap_cython_submodules():
    modules_set = {'app.dummy'}
    sys.meta_path.append(CythonPackageMetaPathFinder(modules_set))
