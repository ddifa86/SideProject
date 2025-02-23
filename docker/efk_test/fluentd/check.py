import socket

def check_fluentd_connection(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print("Connected to Fluentd.")
        except Exception as e:
            print(f"Failed to connect to Fluentd: {e}")

check_fluentd_connection('localhost', 24224)