#!/usr/bin/env python

# Service class
class Service:
    def serve(self):
        return "Service is running!"


# Client class dependent on Service
class Client:
    def __init__(self):
        self.service = None

    def set_service(self, service: Service):
        self.service = service

    def run(self):
        return self.service.serve()


# Injecting dependency via setter method
service = Service()
client = Client()
client.set_service(service)

print(client.run())
