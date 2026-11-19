d = {}
d["EURUSD"] = 1.1300
print(d)
print(d.get("EURUSD"))

try:
    print(d["EURGBP"])
except KeyError as exc:
    print("Key Error:", exc)


print("1.1300 in d", 1.1300 in d)
print("EURUSD in d", "EURUSD" in d)


print("list(d)", list(d))

d.update({"USDJPY":115.2})

print("After update", d)

quote = d.pop("USDJPY")

print("afetr pop", d, quote)
d.update({"USDJPY":115.2})
print(d.items())