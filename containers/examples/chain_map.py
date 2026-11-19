from collections import ChainMap

# ---- layered config ----

defaults = {"pair": "EURUSD", "tf": "H1"}
env = {"tf": "M15"} 
cli = {}

cfg = ChainMap(cli, env, defaults)

print(cfg["tf"], cfg["pair"])   # M15 EURUSD
cfg["pair"] = "GBPUSD"          # writes go to first map

print(cli, defaults["pair"])