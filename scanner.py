import asyncio

TIMEOUT = 0.4


async def scan_port(ip, port):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=TIMEOUT)
        writer.close()
        await writer.wait_closed()
        return port
    except:
        return None


async def scan_host(ip, ports):
    tasks = [scan_port(ip, p) for p in ports]
    results = await asyncio.gather(*tasks)

    return [p for p in results if p]