import frappe

def get_context(context):
    docs = frappe.get_all("Team", ["*"])
    context["docs"]=docs