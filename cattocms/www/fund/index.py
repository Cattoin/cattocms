import frappe

def get_context(context):
	context.no_cache = 1
	context.caselist = frappe.get_all(
		"Case",
        {"fundraising_status":"Ongoing"},
		["name", "main_title", "case_image", "fundraising_status", "target_amount", "sathi_name", "raising_for"],
		order_by="idx"
	)