import frappe
import json

@frappe.whitelist()
def string_to_object(json_string):
    if json_string:
        try:
            json_object = json.loads(json_string)
            return json_object
        except ValueError as e:
            return {}
