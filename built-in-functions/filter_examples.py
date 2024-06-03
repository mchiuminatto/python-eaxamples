# list filter
print("List")
instruments = ["EUR/USD", "USD/JPY", "AUD/USD", "EUR/GBP", "USD/CAD"]
for instrument in filter(lambda x: "/USD" in x, instruments):
    print("Instrument", instrument)


instruments_metadata = {
                        "EUR/USD":{"pip-position": 4}, 
                        "USD/JPY":{"pip-position": 2}, 
                        "AUD/USD":{"pip-position": 4}, 
                        "EUR/GBP":{"pip-position": 4}, 
                        "USD/CAD":{"pip-position": 4},
                        "AUD/JPY":{"pip-position": 2}
                        }
# dictionary filter
print("Metadata")
for instrument in filter(lambda x: "JPY" in x.split("/"), instruments_metadata):
    print("insruments", instrument, instruments_metadata[instrument])