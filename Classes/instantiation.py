class Instrument:

    def __init__(self, symbol: str, pip_position: int ):
        self.symbol = symbol
        self.pip_position = pip_position


    def inspect(self):
        return f"{self.symbol} - {self.pip_position}"


if __name__ == "__main__":
    value = Instrument("EUR/USD", 4).inspect()
    print(value)


