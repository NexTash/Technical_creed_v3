import frappe

def get_context(context):
    blog = frappe.get_all("Blogs",["*"])

    context.update({
        "blog": blog or []
    })


    