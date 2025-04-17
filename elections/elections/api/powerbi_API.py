# apps/your_app/your_app/doctype/election_result/api.py

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)  # Optional: allow_guest for Power BI access without login
def get_all_election_results():
    results = []

    parent_docs = frappe.get_all("Election Result", fields=["*"])

    for doc in parent_docs:
        child_votes = frappe.get_all(
            "Candidate Votes",
            filters={"parent": doc.name},
            fields=["*"]
        )

        doc["candidate_votes"] = child_votes
        results.append(doc)

    return results
