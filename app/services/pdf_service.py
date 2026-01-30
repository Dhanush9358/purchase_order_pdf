from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from io import BytesIO

from app.services.calculator import calculate_totals
from app.services.number_to_words import amount_to_words
from app.services.order_no import generate_order_no
from app.utils.date_utils import today_ddmmyyyy, parse_date


def generate_po_pdf(data):  # ✅ data exists ONLY here
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("purchase_order.html")

    order_no = generate_order_no()
    date_today = today_ddmmyyyy()
    delivery_date = parse_date(data.delivery_date)

    totals = calculate_totals(data.items)

    html_content = template.render(
        order_no=order_no,
        date=date_today,
        delivery_date=delivery_date,
        bill_from=data.bill_from,
        bill_to=data.bill_to,
        ship_to=data.ship_to,
        items=totals["items"],   # ✅ computed items
        totals=totals,
        total_words=amount_to_words(totals["grand_total"]),
        gst_words=amount_to_words(totals["total_gst"]),
    )

    pdf_io = BytesIO()
    HTML(string=html_content, base_url=".").write_pdf(pdf_io)
    pdf_io.seek(0)

    return pdf_io
