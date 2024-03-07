import zmq
import time
import numpy.random
import sys

# this class does not belong here
class Business:
    def __init__(self):
        pass
        
    def produce_items(self):
        _item_idx_list = range(101)
        _items = [{"id":i, "message":f" item {i}" } for i in _item_idx_list]
        print(_items)
        return _items
    

class EndPoint:
    """
    Implements a network endpoint abstraction
    
    """
    def __init__(self, protocol="tcp", ip="127.0.0.1", port="5557"):
        self._protocol = protocol
        self._ip = ip
        self._port = port
        
    @property
    def protocol(self):
        return self._protocol
        
    @protocol.setter
    def protocol(self, protocol):
        self._protocol = protocol
        
    @property
    def ip(self):
        return self._ip
        
    @ip.setter
    def ip(self, ip):
        self._ip = ip
        
    @property
    def port(self):
        return self._port
        
    @port.setter
    def port(self, port):
        self._port = port


class Producer:
    def __init__(self, tgt_endpoint: EndPoint):

        self.context = zmq.Context()
        self.zmq_socket = self.context.socket(zmq.PUSH)
        self.zmq_socket.bind(f"{tgt_endpoint.protocol}://{tgt_endpoint.ip}:{tgt_endpoint.port}")
        
        
    
    def push_loop(self, business):
        
        for _m in business.produce_items():
            self.zmq_socket.send_json(_m)
            print("sending ", _m)
            time.sleep(1)
        


class Worker:
    
    def __init__(self, src_endpoint, tgt_endpoint):
        self._consumer_id = random.randrange(1,10005)
        print("I am consumer {consumer_id}")
        _context = zmq.Context()
        # recieve work
        self._consumer_receiver = _context.socket(zmq.PULL)
        self._consumer_receiver.connect(f"{src_endpoint.protocol}://{src_endpoint.ip}:{src_endpoint.port}")
    
        # send work
        self._consumer_sender = context.socket(zmq.PUSH)
        self._consumer_sender.connect(f"{tgt_endpoint.protocol}://{tgt_endpoint.ip}:{tgt_endpoint.port}")
    
    
    def work_loop(self):
    
        while True:
            _work = self._consumer_receiver.recv_json()
            print(f"Worker {self._consumer_id}, processing messge {_work}")
            _data = _work['id']
            _result = { 'consumer' : self._consumer_id, 'num' : data}
            if data%2 == 0: 
                self.consumer_sender.send_json(result)
        
        
    
    
if __name__ == "__main__" :
    _mode = sys.argv[1]
    print("starting " + _mode)
    _protocol = sys.argv[2]
    _ip = sys.argv[3]
    _port = sys.argv[4]

    _edp = EndPoint(protoco=_protocol, i =_ip, port=_port)


    if _mode == "producer":
        _prd = Producer(_edp)

    
    
    
