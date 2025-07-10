import frappe

def get_context(context):
    content = frappe.get_all("Blogs Content",["*"],order_by="modified asc")
    crd = frappe.get_all("Other Projects Side",["*"],order_by="modified asc")
    frappe.msgprint(f"{content}")
    context.update({
        "content": content,
        "crd": crd
    })
