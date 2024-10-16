import frappe
from frappe import _
from frappe.utils import get_site_name

def get_context(context):
    context.caseid = frappe._dict()
    context.no_cache = 1
    caseid = frappe.form_dict["caseid"]
    context.case_details = frappe.db.get_value(
        "Case",
	    caseid,
        ["name","main_title", "beneficiary_name", "case_image", "sathi_name", "target_amount", "case_details", "sathi_details", "raised_amount"],
        as_dict=1,
	)
    context.site_name = get_site_name(frappe.local.request.host)