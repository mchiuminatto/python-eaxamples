# Iterable class

class CafeQueue:

    def __init__(self) -> None:
        self._queue = []
        self._orders = {}
        self._togo = {}

    def __iter__(self):
        return CafeQueueIterator(self)
    
    def add_customer(self, customer, *orders, togo=True):
        self._queue.append(customer)
        self._orders[customer] = orders
        self._togo[customer] = togo

    def __len__(self):
        return len(self._queue)
    

    def __contains__(self, customer):
        return (customer in self._queue)
    

class CafeQueueIterator:

    def __init__(self, cafe_queue):
        self._cafe = cafe_queue
        self._position = 0

    
    def __next__(self):
        try:
            customer = self._cafe._queue[self._position]
        except IndexError:
            raise StopIteration
        
        orders = self._cafe._orders[customer]
        togo = self._cafe._togo[customer]
        self._position += 1
        return (customer, orders, togo)
    
    def __iter__(self):
        return self
    

def brew(order):
    print(f"Making {order} ...")
    return order

if __name__ == "__main__":
    queue = CafeQueue()
    queue.add_customer('Newman', 'tea', 'tea', 'tea', 'tea', togo=False)
    queue.add_customer('James', 'medium roast drip, milk, 2 sugarsubstitutes')
    queue.add_customer('Glen', 'americano, no sugar, heavy cream')
    queue.add_customer('Jason', 'pumpkin spice latte', togo=False)

    print("Customers", len(queue))
    print("Glen" in queue)
    print("Marcello" in queue)

    for customer, orders, togo in queue:
        for order in orders:
            brew(order)
        if togo:
            print(f"Order for {customer}!")
        else:
            print(f"Takes order to {customer}")




    

