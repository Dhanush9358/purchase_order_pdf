from pydantic import BaseModel
from typing import List


class Address(BaseModel):
    name: str
    address: str
    state: str
    gstin: str | None = None
    mobile: str | None = None


class Item(BaseModel):
    name: str
    hsn: str
    qty: int
    rate: float
    igst: float


class PurchaseOrderRequest(BaseModel):
    delivery_date: str
    bill_from: Address
    bill_to: Address
    ship_to: Address
    items: List[Item]
