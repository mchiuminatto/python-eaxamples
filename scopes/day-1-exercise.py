
"""Day 1 exercise: a toy LEGB resolver."""
import builtins

BUILTINS = vars(builtins)


def resolve(name, local, enclosing, global_ns, builtin_ns=BUILTINS):
    """Resolve `name` the way Python resolves a bare name."""

    chain = [("L", local)]
    chain += [("E", ns) for ns in enclosing]       # innermost first
    chain += [("G", global_ns), ("B", builtin_ns)]
    for scope, ns in chain:
        if name in ns:                             # membership, not truthiness
            return scope, ns[name]
    raise NameError(f"name {name!r} is not defined")

        
    
def shadowed_builtins(namespace):
    """Sorted list of non-dunder names in `namespace` that hide a builtin."""
    return sorted(
        n for n in namespace
        if n in BUILTINS and not (n.startswith("__") and n.endswith("__"))
    )



# ---------------------------------------------------------------- graders
G = {"PIP": 0.0001, "max": "shadow!"}
E = [{"digits": 5}, {"digits": 2, "venue": "LMAX"}]
L = {"price": 1.08}

assert resolve("price", L, E, G) == ("L", 1.08)
assert resolve("digits", L, E, G) == ("E", 5), "innermost enclosing scope wins"
assert resolve("venue", L, E, G) == ("E", "LMAX")
assert resolve("PIP", L, E, G) == ("G", 0.0001)
assert resolve("max", L, E, G) == ("G", "shadow!"), "a global hides a builtin"
assert resolve("len", L, E, G) == ("B", len)
assert resolve("price", {}, [{"price": None}], G) == ("E", None), "None is a value"
assert resolve("flag", {"flag": False}, [], {"flag": True}) == ("L", False)
try:
    resolve("spread", L, E, G)
except NameError as e:
    assert str(e) == "name 'spread' is not defined", str(e)
else:
    raise AssertionError("expected NameError")

assert shadowed_builtins({"max": 1, "list": [], "PIP": 0.1, "id": 7}) == ["id", "list", "max"]
assert shadowed_builtins({"__name__": "m", "sum": 0}) == ["sum"], "ignore dunders"
assert shadowed_builtins({}) == []

# cross-check with the real interpreter
def real_fmt():
    price = 1.08
    return price
assert resolve("price", {"price": 1.08}, [], {}) == ("L", real_fmt())
print("All checks passed")