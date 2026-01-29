from datetime import datetime

_counter = 272  # simple in-memory counter (safe for now)


def generate_order_no() -> str:
    global _counter
    _counter += 1

    year = datetime.now().year
    fy = f"{str(year)[-2:]}-{str(year + 1)[-2:]}"
    return f"OMC-PO-{_counter}/{fy}"
