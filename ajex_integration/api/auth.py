import requests, frappe

def get_token():
    settings = frappe.get_single("AJEX Settings")
    url = f"{settings.base_url}/authentication-service/api/auth/login"
    payload = {"username": settings.username, "password": settings.password}
    res = requests.post(url, json=payload)
    data = res.json()
    if "accessToken" in data:
        settings.token = data["accessToken"]
        settings.save()
        frappe.db.commit()
        return data["accessToken"]
    else:
        frappe.throw(f"AJEX Authentication Failed: {res.text}")
