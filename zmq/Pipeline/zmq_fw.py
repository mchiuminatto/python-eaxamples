import zmq
import time
import numpy.random
import sys
import random

# this class does not belong here
class Business:
    def __init__(self):
        pass
        
    def produce_items(self):
        _item_idx_list = range(101)
        _items = [{"id":i, "message":f" item {i}" } for i in _item_idx_list]
        # print(_items)
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

        self._endpoint = tgt_endpoint
        self.context = zmq.Context()
        self.zmq_socket = self.context.socket(zmq.PUSH)
        self.zmq_socket.bind(f"{tgt_endpoint.protocol}://{tgt_endpoint.ip}:{tgt_endpoint.port}")
        
        
    def __del__(self):
        _endpoint_address = f"{self._endpoint.protocol}://{self._endpoint.ip}:{self._endpoint.port}"
        print("Endpoint ", _endpoint_address)
        self.zmq_socket.close()
        
        
    
    def push_loop(self, business):
        print("Entering push loop")
        for _m in business.produce_items():
            print("sending ", _m)
            self.zmq_socket.send_json(_m)
            time.sleep(1)
        


class Worker:
    
    def __init__(self, src_endpoint, tgt_endpoint):
        self._consumer_id = random.randrange(1,10005)
        print(f"I am consumer {self._consumer_id}")
        _context = zmq.Context()
        # recieve work
        self._consumer_receiver = _context.socket(zmq.PULL)
        self._consumer_receiver.connect(f"{src_endpoint.protocol}://{src_endpoint.ip}:{src_endpoint.port}")
    
        # send work
        # self._consumer_sender = context.socket(zmq.PUSH)
        # self._consumer_sender.connect(f"{tgt_endpoint.protocol}://{tgt_endpoint.ip}:{tgt_endpoint.port}")
    
    
    def work_loop(self):
    
        while True:
            _work = self._consumer_receiver.recv_json()
            print(f"Worker {self._consumer_id}, processing messge {_work}")
            _data = _work
            _result = { 'consumer' : self._consumer_id, 'message' : _data}
 #           if data%2 == 0: 
 #               self.consumer_sender.send_json(result)
 
            time.sleep(1)
        
        
    
    
if __name__ == "__main__":
    _mode = sys.argv[1]

    print("starting " + _mode)
    
    if _mode == "producer":
        _protocol = sys.argv[2]
        _ip = sys.argv[3]
        _port = sys.argv[4]
    
        _edp = EndPoint(protocol=_protocol, ip =_ip, port=_port)
        
        _prd = Producer(_edp)
        _business = Business()
        _prd.push_loop(_business)
        
    elif _mode == "worker":
    
        _protocol = sys.argv[2]
        _ip_src = sys.argv[3]
        _port_src = sys.argv[4]
        
        _edp_src = EndPoint(protocol=_protocol, ip =_ip_src, port=_port_src)
        
        _ip_tgt = sys.argv[5]
        _port_tgt = sys.argv[6]
        
        _edp_tgt = EndPoint(protocol=_protocol, ip =_ip_tgt, port=_port_tgt)
    
        _prd = Worker(_edp_src, _edp_tgt)
        _prd.work_loop()
    
    
    
