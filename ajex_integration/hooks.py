app_name = "ajex_integration"
app_title = "AJEX Integration"
app_publisher = "Nasiruddin Ansari"
app_description = "Integration between ERPNext and AJEX API"
app_email = "you@example.com"
app_license = "MIT"

doctype_js = {"Delivery Note": "public/js/delivery_note.js"}

scheduler_events = {
    "cron": {
        "*/30 * * * *": ["ajex_integration.api.tracking.sync_status"]
    }
}
