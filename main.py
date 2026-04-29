import asyncio
import time

from utils import parse_ports, expand_targets
from scanner import scan_host
from reporter import banner, print_host, progress


async def run(target, ports):
    hosts = expand_targets(target)
    results = {}

    banner()

    print(f"target : {target}")
    print(f"ports  : {ports}\n")

    start = time.time()

    for i, host in enumerate(hosts, 1):
        print(f"\n[+] scanning {host}")

        try:
            open_ports = await scan_host(host, ports)
        except Exception:
            open_ports = []

        results[host] = open_ports

        print_host(host, open_ports)
        progress(i, len(hosts))

    end = time.time()

    print("\n\n[+] scan complete")
    print(f"[+] time: {round(end - start, 2)}s")


def main():
    print("\n(p0khrl scanner v10+)\n")

    target = input("target (default 127.0.0.1): ").strip() or "127.0.0.1"
    ports = input("ports (default 1-100): ").strip() or "1-100"

    port_list = parse_ports(ports)

    asyncio.run(run(target, port_list))


if __name__ == "__main__":
    main()