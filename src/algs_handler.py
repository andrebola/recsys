import pkgutil
import recommendalgs
import imp
import inspect

def get_module_source(modulename):
    """ Given a module dotted path (string), see how it can be
    imported (.py or .pyc)
    returns imp.PY_SOURCE, imp.PY_COMPILED, or imp.C_EXTENSION"""
    pkgname, modname = modulename.rsplit(".", 1)
    # easiest way to get the path of the module
    package = __import__(pkgname, fromlist="dummy")
    #print "package path", package.__path__
    moddata = imp.find_module(modname, package.__path__)
    desc = moddata[2]
    return desc[2]

def get_recommend_algs():
    ret = {}
    errors = []
    for importer, modname, ispkg in \
            pkgutil.walk_packages(recommendalgs.__path__, "src.recommendalgs."):
        if not ispkg:
            stype = get_module_source(modname)
            if stype == imp.PY_SOURCE:
                try:
                    module = __import__(modname, fromlist="dummy")
                    for name, ftype in inspect.getmembers(module, inspect.isclass):
                        if issubclass(ftype,
                        recommendalgs.base_algorithm.AbstractRecommendAlgorithm):
                            inst = ftype()
                            if inst._slug:
                                ret[inst._slug] = inst
                except ImportError, e:
                    print e
                    errors.append(modname)
    return ret, errors
