# Namespace:
# A mapping from names to objects
# Are implemented as python dictionaries
# Examples:
#           built-in names (created when python interpreter loads)
#           module's global names (created when a module file is loaded)
#           function invocations names (created when a function is invoked)
#
# Attribute of a module is any thing referenced after the module name followed
# by a dot. for instance module.name, module.calculate, both are referenced as
# attributes. It turns out that the references of a module attributes match
# with the module namespace.

# attributes can be only readable and writable. In this latter case, attributes
# can also be deleted.
#
# Scope:
# It is a textual region where a namespace is directly accessible, which means
# that a reference to a name it will be solved within the namespace.
#
# there are three nested scopes whose namespaces are directly accessible:
#   * innermost namespace, containing local names
#   * the scope of any enclosing function, searched from the nearest enclosing
#   scope containing not-local but also non-global names
#   * the next-to-last scope. containing current module's global names
#   * the outermost scope (searched last) is the namespace containing built-in names

# IMPORTANT
#   if a variable is declared global, all references and assignments will go to the
#   module's global namespace
#
#   you can read global scope variables in the innermost scope. But if they are
#   assigned with a value a new local copy is created with the same name than
#   the global's
#
#   to rebind a global variable to innermost scope use the nonlocal statement
#
# global statement: indicates that a variable lives on the module's namespace
#
# nonlocal: rebinds a variable of the enclosing scope to the local's

# examples


def scope_test():
    def do_local():
        spam = "local spam"
        # local variable spam, not
        # externally binding

    def do_nonlocal():
        nonlocal spam
        spam = "non local spam"
        # enclosing function spam variable is binded to
        # the global one

    def do_global():
        global spam
        spam = "global spam"
        # a global binding is done (at module's level)
        # so the value in the enclosing function (scope_test)
        # scope where the value is printed, it is not affected

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)  # "test spam"
    do_nonlocal()
    print("After nonlocal assignment", spam)  # "non local spam"
    do_global()
    print("After global assignment", spam)  # "non local spam"

scope_test()
print("In global scope:", spam)  # this value was modified on do_global

