import copy

config = {"db": {"host": "localhost"}, "debug": False}
shallow = config.copy()
deep = copy.deepcopy(config)

shallow["db"]["host"] = "prod"
shallow["debug"] = True

print(config["db"]["host"], config["debug"], deep["db"]["host"])