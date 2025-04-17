# Copyright (c) 2025, Kelvin Njenga and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ElectionResult(Document):
    def before_save(self):
        if self.county and self.position:
            self.title = f"{self.county.title()} - {self.position}"





'''
Description Here

'''

from elections.elections.api.utils import get_userScope

def get_permission_query_conditions(user):
    if not user or user == "Administrator":
        return ""

    scope = get_userScope(user)
    counties = scope.get("counties", [])

    if not counties:
        return "1=0"

    counties_escaped = ', '.join([f"'{c}'" for c in counties])
    return f"`tabElection Result`.`county` IN ({counties_escaped})"
