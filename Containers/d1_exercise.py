"""

Your risk service caches results keyed by the current position book, a nested structure of dicts, lists and sets. 

You need two helpers: 
- freeze turns the book into a hashable snapshot that later mutations cannot touch, and 
- find_aliases reports where the same mutable object is reachable from two paths, which is usually a bug from a shallow copy.

"""

from collections.abc import Hashable

MUTABLE = (list, dict, set)


def freeze(position) -> frozenset:
    """
    Returns a hashable, deeply immutable copy of obj.

    dict -> tuple of (key, frozen value) pairs sorted by key
    list/tuple -> tuple of frozen items
    anything else -> returned unchaged if hashable else TypeError
    """
    # TODO: Dipatch one typoe and recurse

    print("evaluating=", position, "type=", type(position).__name__)

    if isinstance(position, dict):
        print("Procesing dict")
        return tuple(sorted((k, freeze(v)) for k, v in position.items()))
    
    if isinstance(position, (list, tuple)): 
        print("Processing list or tuple")
        return tuple(freeze(v) for v in position)

    if isinstance(position, (set, frozenset)):
        print("Processing set, frozenset")
        return frozenset(freeze(v) for v in position)

    if isinstance(position, Hashable):
        print("Procesing hashable")
        hash(position)  # a tuple is Hashable by type but may hold a list
        return position

    raise TypeError(f"cannot freeze {type(position).__name__}")



def find_aliases(obj, path="root", _seen=None):
    seen = {} if _seen is None else _seen     # id -> first path
    found = []
    if isinstance(obj, MUTABLE):
        if id(obj) in seen:
            return [path]                     # already visited: an alias
        seen[id(obj)] = path
    if isinstance(obj, dict):
        children = ((f"{path}[{k!r}]", v) for k, v in obj.items())
    elif isinstance(obj, (list, tuple)):
        children = ((f"{path}[{i}]", v) for i, v in enumerate(obj))
    else:
        children = ()
    for child_path, child in children:
        found += find_aliases(child, child_path, seen)
    return found


    

# ---- acceptance checks ----
fills = [100_000, -40_000]
book = {"acct1": {"EURUSD": fills, "tags": {"hedge", "fx"}},
        "acct2": {"EURUSD": fills}}

frozen = freeze(book)
print(hash(frozen) == hash(freeze(book)))          # stable and hashable
fills.append(5)
print(frozen == freeze(book))                      # snapshot unaffected -> False
print(find_aliases(book))
print(find_aliases({"x": [1], "y": [1]}))          # equal but distinct: no alias
try:
    freeze({"bad": (1, bytearray(b"x"))})
except TypeError as exc:
    print("TypeError:", exc)