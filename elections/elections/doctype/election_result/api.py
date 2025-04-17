# apps/elections/elections/elections/doctype/election_result/api.py

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_all_election_results():
    results = []

    # Get all Election Result records
    parent_docs = frappe.get_all("Election Result", fields=["*"])

    for doc in parent_docs:
        # Fetch child table records for each parent
        child_votes = frappe.get_all(
            "Candidate Votes",
            filters={"parent": doc.name},
            fields=["*"]
        )
        # Add child records under a new field
        doc["candidate_votes"] = child_votes

        # Append the combined data
        results.append(doc)

    return results
