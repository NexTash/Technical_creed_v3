import frappe

def get_context(context):
    codes = frappe.get_all("Services", {"feature": 1} ,["*"] , order_by="modified asc")
    context.update({
        "codes":codes,
    })
    