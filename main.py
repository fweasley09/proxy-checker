import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import socks

def check_proxy(proxy, proxy_type):
    try:
        if proxy_type == 'socks5':
            parts = proxy.split(":")
            address = parts[1].strip()
            port = int(parts[2].strip())  # Convert port to integer safely
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, address, port)
            socket = socks.socksocket()
            socket.settimeout(5)

        response = requests.get('http://example.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
    except ValueError:
        print(f"Invalid proxy format: {proxy}")
        return False

def main():
    proxy_file = 'proxies.txt'
    output_file = 'checked_proxies.txt'

    working_proxies = []
    non_working_proxies = []

    with open(proxy_file, 'r') as f:
        proxies = [line.strip() for line in f.readlines()]

    for proxy in proxies:
        proxy_type = 'http' if proxy.startswith('http') else 'socks5'
        print(f"Checking {proxy}...")
        if check_proxy(proxy, proxy_type):
            working_proxies.append(proxy)
            print(f"{proxy} - WORKING")
        else:
            non_working_proxies.append(proxy)
            print(f"{proxy} - NOT WORKING")

    with open(output_file, 'w') as f:
        f.write("# Working Proxies\n")
        for proxy in working_proxies:
            f.write(proxy + "\n")
        f.write("\n# Non-Working Proxies\n")
        for proxy in non_working_proxies:
            f.write(proxy + "\n")

    print("Proxy checking complete!")
    print(f"Working: {len(working_proxies)} | Non-Working: {len(non_working_proxies)}")

if __name__ == "__main__":
    main()
