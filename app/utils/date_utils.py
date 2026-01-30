from datetime import datetime


def today_ddmmyyyy() -> str:
    """Returns today's date in DD/MM/YYYY format"""
    return datetime.now().strftime("%d/%m/%Y")


def financial_year(date: datetime | None = None) -> str:
    """Returns Indian financial year like 25-26"""
    date = date or datetime.now()
    year = date.year

    if date.month < 4:
        return f"{year-1}-{str(year)[-2:]}"
    return f"{year}-{str(year+1)[-2:]}"


def parse_date(date_str: str | None):
    if not date_str:
        return datetime.now().strftime("%d/%m/%Y")

    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        return datetime.now().strftime("%d/%m/%Y")
