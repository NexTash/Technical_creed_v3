import frappe

def get_context(context):
    docs = frappe.get_all("Team", ["*"])
    team = frappe.get_all("Team Des", ["*"])
    ptd = frappe.get_all("Project title des", ["*"])
    ptc=frappe.get_all("pro card content",["*"])
    community=frappe.get_all("Community",["*"])


    context.update({
        "docs": docs or [],
        "team": team or [],
        "ptd":ptd or [],
        "ptc":ptc or [],
        "community":community or []
    })

    