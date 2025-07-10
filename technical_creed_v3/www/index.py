import frappe

def get_context(context):
  # customers = frappe.get_all("Customer" , ['*'] )
  pricing = frappe.db.get_all("Pricing", ["*"] )
  links = frappe.db.get_all("Team", ["*"])
  codes = frappe.get_all("Services", {"feature": 1} ,["*"] , order_by="modified asc")
  team = frappe.get_all("Team Des", ["*"])
  ptd = frappe.get_all("Project title des", ["*"])
  ptc=frappe.get_all("pro card content",["*"])
  y = frappe.get_all("Why Choose Us", ["*"] , order_by="modified asc")
  community=frappe.get_all("Community",["*"])
  agency_card=frappe.get_all("services agency facts", ["*"] , order_by="modified asc")

  context.update({
    "pricing" : pricing,
    # "customers" : customers,
    "links" : links,
    "codes":codes,
     "team": team or [], 
    "ptd":ptd,
    "ptc":ptc,
    "y":y,
    "community":community,
    "agency_card":agency_card

  })
