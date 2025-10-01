import requests, frappe
from ajex_integration.api.auth import get_token

@frappe.whitelist()
def create_booking(delivery_note):
    dn = frappe.get_doc("Delivery Note", delivery_note)
    token = frappe.get_single("AJEX Settings").token or get_token()
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{frappe.get_single('AJEX Settings').base_url}/tms-adapter-service/api/v1/ext-booking"

    payload = {
        "customerName": dn.customer_name,
        "productName": "DOM",
        "subProductName": "EXS",
        "temperatureName": "Ambient",
        "pieceCount": sum([i.qty for i in dn.items]),
        "pickupDatetimeMs": frappe.utils.now_datetime().timestamp() * 1000,
        "commodityId": 1,
        "shipper": {"companyName": dn.company},
        "consignee": {"name": dn.customer_name},
        "podList": []
    }

    res = requests.post(url, json=payload, headers=headers)
    if res.ok:
        data = res.json()
        dn.db_set("ajex_waybill", data.get("waybillNo"))
        dn.db_set("ajex_status", "Booked")
        return data
    else:
        frappe.throw(f"AJEX Booking Failed: {res.text}")
