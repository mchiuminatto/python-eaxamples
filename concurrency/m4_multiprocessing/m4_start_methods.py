import multiprocessing as mp

def child(tag):
    print(f"[{tag}] child sees name = {__name__}")


if  __name__ == "__main__":
    for method in ("fork", "spawn", "forkserver"):
        ctx = mp.get_context(method)
        p = ctx.Process(target=child, args=(method, ))
        p.start()
        p.join()

