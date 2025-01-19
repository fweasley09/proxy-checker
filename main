import requests

def check_proxy(proxy):
    try:
        response = requests.get('http://example.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def main():
    proxy_file = 'proxies.txt'  # input file
    output_file = 'checked_proxies.txt'  # output file

    working_proxies = []
    non_working_proxies = []

    with open(proxy_file, 'r') as f:
        proxies = [line.strip() for line in f.readlines()]

    for proxy in proxies:
        print(f"Checking {proxy}...")
        if check_proxy(proxy):
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
