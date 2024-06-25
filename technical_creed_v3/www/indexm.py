import frappe

def get_context(context):
  customers = frappe.get_all("Customer" , ['*'] )
  pricing = frappe.db.get_all("Pricing", ["*"] )
  links = frappe.db.get_all("Team", ["*"])
  codes = frappe.get_all("Services", {"feature": 1} ,["*"] , order_by="modified asc")
        
  context.update({
    "pricing" : pricing,
    "customers" : customers,
    "links" : links,
    "codes":codes,

  })
