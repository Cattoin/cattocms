import frappe

def get_context(context):
	context.no_cache = 1
	context.ongoing_caselist = frappe.get_all(
		"Case",
		{"fundraising_status":"Ongoing"},
		["name", "main_title", "case_image", "fundraising_status", "target_amount", "sathi_name", "raising_for"],
		order_by="idx"
	)

	context.completed_caselist = frappe.get_all(
		"Case",
		{"fundraising_status":"Completed"},
		["name", "main_title", "case_image", "fundraising_status", "target_amount", "sathi_name", "raising_for"],
		order_by="idx"
	)