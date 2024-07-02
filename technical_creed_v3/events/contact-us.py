import frappe

@frappe.whitelist()
def contacts(firstname,email,subject,message):
    doc = frappe.new_doc("Contact us")
    doc.name1 = firstname
    doc.email = email
    doc.subject = subject
    doc.message = message
   
    # doc.append("email_ids", {
    #         'email_id' : email
    #     })
    doc.insert()

    return "Created"