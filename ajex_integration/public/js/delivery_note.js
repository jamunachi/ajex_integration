frappe.ui.form.on("Delivery Note", {
    refresh: function(frm) {
        if (!frm.doc.ajex_waybill) {
            frm.add_custom_button("Create AJEX Booking", function() {
                frappe.call({
                    method: "ajex_integration.api.booking.create_booking",
                    args: { delivery_note: frm.doc.name },
                    callback: function(r) { frm.reload_doc(); }
                });
            });
        } else {
            frm.add_custom_button("Fetch AJEX POD", function() {
                frappe.call({
                    method: "ajex_integration.api.documents.fetch_pod",
                    args: { waybill: frm.doc.ajex_waybill, doctype: "Delivery Note", docname: frm.doc.name },
                    callback: function(r) {
                        frappe.msgprint("POD Attached: " + r.message);
                    }
                });
            });
        }
    }
});