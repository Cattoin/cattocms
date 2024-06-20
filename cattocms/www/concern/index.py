import frappe
from frappe import _
from frappe.utils import get_site_name

def get_context(context):
    context.site_name = get_site_name(frappe.local.request.host)