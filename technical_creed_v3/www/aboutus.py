import frappe

def get_context(context):
    docs = frappe.get_list("Pricing", ["*"] , order_by="modified asc")
    items = frappe.get_list("Team", ["*"] , order_by="modified asc")
    rows = frappe.get_list("Team", ["*"] , order_by="modified asc")

    context.update({
        "docs":docs,
        "items":items,
        "rows":rows,
        
    })