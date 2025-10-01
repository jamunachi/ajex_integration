import requests, frappe
from ajex_integration.api.auth import get_token

def sync_status():
    dn_list = frappe.get_all("Delivery Note", filters={"ajex_waybill": ["!=", ""]}, fields=["name","ajex_waybill"])
    token = frappe.get_single("AJEX Settings").token or get_token()
    headers = {"Authorization": f"Bearer {token}"}
    base_url = frappe.get_single("AJEX Settings").base_url

    for dn in dn_list:
        url = f"{base_url}/tms-adapter-service/api/v1/ext-booking/getstatus/{dn.ajex_waybill}"
        res = requests.get(url, headers=headers)
        if res.ok:
            status = res.json().get("status")
            frappe.db.set_value("Delivery Note", dn.name, "ajex_status", status)
