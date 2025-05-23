# import frappe

# @frappe.whitelist()
# def get_candidates_by_position(region, election_level, election_sub_level):
#     candidates = frappe.get_all("Election Candidate", 
#         filters={
#             "region": region,
#             "election_level": election_level,
#             "election_sub_level": election_sub_level,
#             "status": "Approved" 
#         },
#         fields=["name", "full_name", "id_number", "position"]
#     )

#     grouped = {}
#     for cand in candidates:
#         position_key = cand.position.lower().replace(" ", "_")
#         grouped.setdefault(position_key, []).append(cand)

#     return grouped


import frappe

@frappe.whitelist()
def get_candidates_by_position(region, election_level, election_sub_level):
    """
    Fetches candidates from the 'Election Candidates' Doctype based on
    region, election level, and sub level, filtering only 'Pass' candidates.
    """
    candidates = frappe.get_all("Election Candidate",
        filters={
            "region": region,
            "election_level": election_level,
            "election_sub_level": election_sub_level,
            "candidacy_status": "Pass"  # Ensure only valid/approved candidates
        },
        fields=["name", "full_name", "position"]
    )

    grouped = {}
    for cand in candidates:
        key = cand.position.strip().lower().replace(" ", "_")
        grouped.setdefault(key, []).append({
            "name": cand.name,
            "full_name": cand.full_name
        })

    return grouped
