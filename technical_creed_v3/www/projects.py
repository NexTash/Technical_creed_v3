import frappe

def get_context(context):
    docs = frappe.get_list("Team", ["*"])
    context["docs"]=docs