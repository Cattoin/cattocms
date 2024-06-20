import frappe

def get_context(context):
	context.no_cache = 1
	context.caselist = frappe.get_all(
		"Case",
        {"enable_funding":1},
		["name", "main_title", "case_image", "enable_funding", "target_amount", "sathi_name", "raising_for"],
		order_by="idx"
	)
