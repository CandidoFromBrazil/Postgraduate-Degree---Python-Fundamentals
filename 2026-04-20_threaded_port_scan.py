import socket
import threading
from queue import Queue

# Configuration
target = "127.0.0.1"  # Change this to your target IP
queue = Queue()
open_ports = []

def port_scan(port):
    """
    Attempts to connect to a specific port on the target IP.
    """
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Short timeout for speed
        
        # Attempt to connect
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

def fill_queue(port_list):
    """
    Puts the ports we want to scan into a queue.
    """
    for port in port_list:
        queue.put(port)

def worker():
    """
    The thread worker that pulls ports from the queue and scans them.
    """
    while not queue.empty():
        port = queue.get()
        port_scan(port)
        queue.task_done()

def run_scanner(threads, port_range):
    fill_queue(port_range)
    
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    print(f"Scanning complete. Open ports on {target}: {sorted(open_ports)}")

# Example: Scan ports 1 through 1024 using 100 threads
if __name__ == "__main__":
    run_scanner(100, range(1, 1025))