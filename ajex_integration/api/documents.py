import requests, frappe, base64
from ajex_integration.api.auth import get_token

@frappe.whitelist()
def fetch_pod(waybill, doctype, docname):
    token = frappe.get_single("AJEX Settings").token or get_token()
    url = f"{frappe.get_single('AJEX Settings').base_url}/tms-common-service/api/v1/pod-details/extwaybill/{waybill}"
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    if res.ok:
        data = res.json()
        pdf_data = base64.b64decode(data["file"])
        file = frappe.get_doc({
            "doctype": "File",
            "file_name": f"{waybill}_POD.pdf",
            "is_private": 1,
            "content": pdf_data,
            "attached_to_doctype": doctype,
            "attached_to_name": docname
        })
        file.insert()
        return file.file_url
    else:
        frappe.throw(f"Failed to fetch POD: {res.text}")
