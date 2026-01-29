ONES = (
    "", "One", "Two", "Three", "Four", "Five",
    "Six", "Seven", "Eight", "Nine", "Ten",
    "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
)

TENS = (
    "", "", "Twenty", "Thirty", "Forty",
    "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
)


def _convert(n: int) -> str:
    if n == 0:
        return ""

    if n < 20:
        return ONES[n]

    if n < 100:
        return TENS[n // 10] + (" " + ONES[n % 10] if n % 10 else "")

    if n < 1000:
        return ONES[n // 100] + " Hundred" + (
            " " + _convert(n % 100) if n % 100 else ""
        )

    if n < 100000:
        return _convert(n // 1000) + " Thousand" + (
            " " + _convert(n % 1000) if n % 1000 else ""
        )

    if n < 10000000:
        return _convert(n // 100000) + " Lakh" + (
            " " + _convert(n % 100000) if n % 100000 else ""
        )

    return _convert(n // 10000000) + " Crore" + (
        " " + _convert(n % 10000000) if n % 10000000 else ""
    )


def amount_to_words(amount: float) -> str:
    rupees = int(amount)
    paise = int(round((amount - rupees) * 100))

    words = ""

    if rupees:
        words += _convert(rupees) + " Rupees"

    if paise:
        words += " and " + _convert(paise) + " Paise"

    return words + " Only"
