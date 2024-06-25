import frappe

def get_context(context):
    docs = frappe.get_list("FAQ", ["*"] , order_by="modified asc")
    items = frappe.get_list("Team", ["*"] , order_by="modified asc")
    context.update({
        "docs":docs,
        "items":items,
    })
    