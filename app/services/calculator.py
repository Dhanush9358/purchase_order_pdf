def calculate_totals(items):
    computed_items = []
    sub_total = 0
    total_gst = 0
    total_qty = 0

    for item in items:
        taxable = item.qty * item.rate
        gst_amount = taxable * item.igst / 100
        amount = taxable + gst_amount

        computed_items.append({
            "name": item.name,
            "hsn": item.hsn,
            "qty": item.qty,
            "rate": item.rate,
            "igst": item.igst,
            "amount": round(amount, 2),
        })

        sub_total += taxable
        total_gst += gst_amount
        total_qty += item.qty

    return {
        "items": computed_items,
        "sub_total": round(sub_total, 2),
        "total_gst": round(total_gst, 2),
        "grand_total": round(sub_total + total_gst, 2),
        "total_qty": total_qty,
    }
