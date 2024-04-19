from queue import PriorityQueue
from datetime import datetime

class ServerQueue:
    def __init__(self):
        self.request_queue = PriorityQueue()
        self.request_statistics = []

    def add_request(self, client_name, priority):
        timestamp = datetime.now()
        self.request_queue.put((priority, timestamp, client_name))
        self.request_statistics.append((client_name, timestamp))

    def process_request(self):
        if not self.request_queue.empty():
            priority, timestamp, client_name = self.request_queue.get()
            print(f"Request from {client_name} with priority {priority} at {timestamp}")
        else:
            print("No requests to process")

    def show_statistics(self):
        print("\nRequest Statistics:")
        for client_name, timestamp in self.request_statistics:
            print(f"Client: {client_name}, Timestamp: {timestamp}")

def show_menu():
    print("1. Add a request to the server queue")
    print("2. Process a request from the server queue")
    print("3. Show request statistics")
    print("0. Exit")

    choice = input("Enter your choice: ")
    return choice

server = ServerQueue()

while True:
    choice = show_menu()

    if choice == '1':
        client_name = input("Enter client name: ")
        priority = int(input("Enter priority (1 - high, 2 - medium, 3 - low): "))
        server.add_request(client_name, priority)
        print("Request added to the server queue.")
    elif choice == '2':
        server.process_request()
    elif choice == '3':
        server.show_statistics()
    elif choice == '0':
        print("end")
        break
    else:
        print("Error!!!")