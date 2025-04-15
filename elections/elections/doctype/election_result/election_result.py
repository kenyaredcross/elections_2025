# Copyright (c) 2025, Kelvin Njenga and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ElectionResult(Document):
    def before_save(self):
        if self.county and self.position:
            self.title = f"{self.county.title()} - {self.position}"