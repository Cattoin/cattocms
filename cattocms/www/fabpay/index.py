import frappe
from frappe import _
def get_context(context):
    context.caseid = frappe._dict()
    context.no_cache = 1
    caseid = frappe.form_dict["caseid"]
    context.case_details = frappe.db.get_value(
        "Case",
	    caseid,
        ["name","main_title", "target_amount"],
        as_dict=1,
	)