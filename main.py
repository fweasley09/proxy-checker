import socks
import socket
from concurrent.futures import ThreadPoolExecutor

# Function to check a single proxy
def check_proxy(proxy):
    try:
        # Extract host and port from the proxy string
        host, port = proxy.split(":")
        port = int(port)

        # Set up the SOCKS5 proxy
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, host, port)
        socket.socket = socks.socksocket

        # Test connection to a target website (e.g., Google)
        test_socket = socket.create_connection(("www.google.com", 80), timeout=5)
        test_socket.close()

        return proxy, True
    except Exception:
        return proxy, False

# Load proxies from a file
def load_proxies(file_path):
    with open(file_path, "r") as file:
        return [line.strip().replace("socks5://", "") for line in file if line.strip()]

# Save live proxies to a file
def save_live_proxies(file_path, live_proxies):
    with open(file_path, "w") as file:
        for proxy in live_proxies:
            file.write(f"socks5://{proxy}\n")

# Main function to check proxies
def main(input_file, output_file, max_threads=100):
    print("Loading proxies...")
    proxies = load_proxies(input_file)

    print(f"Checking {len(proxies)} proxies...")
    live_proxies = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = executor.map(check_proxy, proxies)
        for proxy, is_alive in results:
            if is_alive:
                live_proxies.append(proxy)

    print(f"Found {len(live_proxies)} live proxies.")
    save_live_proxies(output_file, live_proxies)
    print(f"Live proxies saved to {output_file}")

if __name__ == "__main__":
    # Specify input and output file paths
    input_file = "proxies.txt"  # Replace with your input file name
    output_file = "live_proxies.txt"     # Replace with your desired output file name

    # Run the proxy checker
    main(input_file, output_file)
