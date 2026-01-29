def calculate_totals(items):
    total_qty = 0
    sub_total = 0
    total_gst = 0

    for item in items:
        amount = item.qty * item.rate
        gst_amount = amount * (item.igst / 100)

        item.amount = round(amount + gst_amount, 2)
        item.taxable = round(amount, 2)
        item.gst_amount = round(gst_amount, 2)

        total_qty += item.qty
        sub_total += amount
        total_gst += gst_amount

    grand_total = round(sub_total + total_gst, 2)

    return {
        "total_qty": total_qty,
        "sub_total": round(sub_total, 2),
        "total_gst": round(total_gst, 2),
        "grand_total": grand_total,
    }
