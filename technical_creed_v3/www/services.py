import frappe

def get_context(context):
    codes = frappe.get_all("Services", {"feature": 1} ,["*"] , order_by="modified asc")
    work_card=frappe.get_all("services work card", ["*"] , order_by="modified asc")
    agency_card=frappe.get_all("services agency facts", ["*"] , order_by="modified asc")
    context.update({
        "codes":codes,
        "work_card":work_card,
        "agency_card":agency_card
    })
    