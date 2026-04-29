import ipaddress


def parse_ports(port_str="1-100"):
    ports = set()

    for part in port_str.split(","):
        part = part.strip()

        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))

    return sorted(ports)


def expand_targets(target):
    try:
        net = ipaddress.ip_network(target, strict=False)
        return [str(ip) for ip in net.hosts()]
    except ValueError:
        return [target]