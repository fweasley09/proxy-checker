# proxy-checker
A Python script to check HTTP/HTTPS/SOCKS4/SOCKS5 proxies from a text file and save working/non-working proxies.


# Features
- Check proxies from a text file (one proxy per line)
- Save working and non-working proxies to separate sections in the output file
- Customizable timeout (default: 5 seconds)
- Easy-to-use interface


# Steps :
**1. Clone**
git clone https://github.com/fweasley09/proxy-checker.git
cd proxy-checker

**2. Install dependencies** 
pip install -r requirements.txt

**3. Run the script**
python3 main.py

## Script Overview

The script performs the following steps:

1. **Read Proxy List**: Reads the list of proxies from the specified file.
2. **Check Proxies**: Uses a multithreaded approach to test each proxy by attempting to connect to `www.google.com`.
3. **Save Results**: Writes the active proxies to a new file, `live_proxies.txt`.

## Example Output

Input file (`proxies.txt`):
```
socks5://190.95.183.242:2020
socks5://172.67.176.89:80
socks5://24.152.50.114:999
```

Output file (`live_proxies.txt`):
```
socks5://172.67.176.89:80
```

## Notes

- Ensure that the proxy list file is properly formatted.
- The script currently tests proxies against `www.google.com`. You can modify the target website in the script if needed.
- The timeout for each connection attempt is set to 5 seconds. You can adjust this value for stricter or more lenient testing.
- The script uses multithreading with a default of 100 threads for optimal performance. You can adjust the `max_threads` parameter in the `main` function for your system's capabilities.

## Troubleshooting

- If you encounter a `ModuleNotFoundError` for `socks`, ensure that you have installed the `PySocks` library:
  ```bash
  pip install pysocks
  ```

- If proxies are not being tested correctly, ensure that the proxies in the input file are valid and accessible.

## License
This script is provided "as is" without any warranties. Use it at your own risk.
