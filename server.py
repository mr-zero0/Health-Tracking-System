import socket
import threading
from setup_logging import logger
 
class EmbeddedServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.is_running = threading.Event()
        self.is_running.set()
 
    def is_anomalous(self, bp, heartrate):
        # Check for abnormal blood pressure and heart rate
        return (bp < 90 or bp > 140) or (heartrate < 60 or heartrate > 100)
 
    def handle_client(self, conn, addr):
        try:
            logger.info(f"Connection established with {addr}")
            data = conn.recv(1024).decode()
            logger.info(f"Received alert message: {data}")
            conn.send("Alert received".encode())
        except Exception as e:
            logger.error(f"Error while handling client {addr}: {e}")
        finally:
            conn.close()
 
    def run(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logger.info(f"Server started at {self.host}:{self.port}")
 
            while self.is_running.is_set():
                try:
                    self.server_socket.settimeout(1.0)  # Short timeout for graceful shutdown
                    conn, addr = self.server_socket.accept()
                    client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                    client_thread.start()
                except socket.timeout:
                    continue
                except OSError as e:
                    if not self.is_running.is_set():
                        break
                    logger.error(f"Socket error: {e}")
        except Exception as e:
            logger.error(f"Server encountered an error: {e}")
        finally:
            self.server_socket.close()
            logger.info("Server socket closed")
 
    def stop(self):
        self.is_running.clear()
        self.server_socket.close()
        logger.info("Server stopping...")
 
# Example usage
if __name__ == "__main__":
    server = EmbeddedServer()
    server_thread = threading.Thread(target=server.run)
    server_thread.start()
 
    try:
        input("Press Enter to stop the server...\n")
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received.")
 
    server.stop()
    server_thread.join()
    logger.info("Server has been stopped.")
 