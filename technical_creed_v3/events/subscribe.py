import frappe

@frappe.whitelist(allow_guest=True)
def subscribe(email):
    # yahan aap ek custom doctype bana ke usme email save kar sakte hain
    doc = frappe.new_doc("Subscribe")
    doc.email = email
    doc.insert()

    return "Subscribed Successfully!"