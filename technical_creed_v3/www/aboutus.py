import frappe

def get_context(context):
    docs = frappe.get_all("Pricing", ["*"] , order_by="modified asc")
    items = frappe.get_all("Team", ["*"] , order_by="modified asc")
    rows = frappe.get_all("Team", ["*"] , order_by="modified asc")

    context.update({
        "docs":docs,
        "items":items,
        "rows":rows,
        
    })