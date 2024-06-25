import frappe

@frappe.whitelist()
def contacts(firstname,email,subject,message):
    doc = frappe.new_doc("Contact")
    doc.first_name = firstname
    doc.custom_subject = subject
    doc.custom_message = message
   
    doc.append("email_ids", {
            'email_id' : email
        })
    doc.insert()

    return "Created"