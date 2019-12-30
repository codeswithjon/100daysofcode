import os

ip_list = ["10.51.0.1", "10.51.0.2", "10.51.0.16", "10.51.0.4"]

for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")