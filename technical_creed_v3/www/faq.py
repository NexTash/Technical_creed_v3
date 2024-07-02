import frappe

def get_context(context):
    docs = frappe.get_all("FAQ", ["*"] , order_by="modified asc")
    items = frappe.get_all("Team", ["*"] , order_by="modified asc")
    context.update({
        "docs":docs,
        "items":items,
    })
    