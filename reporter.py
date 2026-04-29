def banner():
    print("""
╔════════════════════════════╗
║          p0khrl           ║
╚════════════════════════════╝
""")


def guess_service(port):
    services = {
        21: "ftp",
        22: "ssh",
        23: "telnet",
        25: "smtp",
        53: "dns",
        80: "http",
        110: "pop3",
        139: "netbios",
        443: "https",
        445: "smb"
    }
    return services.get(port, "unknown")


def print_host(host, ports):
    print(f"\n[ HOST ] {host}")
    print("-" * 35)
    print(f"{'PORT':<8}{'STATE':<10}{'SERVICE'}")
    print("-" * 35)

    if not ports:
        print(f"{'none':<8}{'closed':<10}-")
    else:
        for p in ports:
            print(f"{p:<8}{'open':<10}{guess_service(p)}")

    print("-" * 35)


def progress(i, total):
    bar_len = 18
    filled = int(bar_len * i / total)
    bar = "█" * filled + "-" * (bar_len - filled)
    print(f"\r[SCAN] [{bar}] {i}/{total}", end="")