#!/usr/bin/env python

# Service class
class Service:
    def serve(self):
        return "Service is running!"


# Client class dependent on Service
class Client:
    def __init__(self, service: Service):
        self.service = service

    def run(self):
        return self.service.serve()


# Injecting dependency via constructor
service = Service()
client = Client(service)

print(client.run())
