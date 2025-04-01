import frappe
import requests

@frappe.whitelist()
def sync_candidates_from_espocrm():
    settings = frappe.get_single("EspoCRM Settings")
    headers = {
        "Accept": "application/json",
        "X-Api-Key": settings.api_key
    }

    response = requests.get(f"{settings.base_url}/api/v1/CElectionNomination", headers=headers)
    if response.status_code != 200:
        frappe.throw(f"Failed to fetch data: {response.status_code} - {response.text}")

    candidates = response.json().get("list", [])
    synced = 0

    for item in candidates:
        external_id = item.get("id")
        if not external_id:
            continue

        existing = frappe.get_all("Election Candidate", filters={"external_id": external_id}, limit=1)

        if existing:
            doc = frappe.get_doc("Election Candidate", existing[0]["name"])
        else:
            doc = frappe.new_doc("Election Candidate")
            doc.external_id = external_id

        # Map fields from EspoCRM to your Doctype
        doc.full_name = item.get("yourFullNameAsAppearedOnYourID")
        doc.position = item.get("krcsPositions")
        doc.email = item.get("emailAddress")
        doc.phone = item.get("phone")
        doc.county = item.get("county")
        doc.region = item.get("region")
        doc.gender = item.get("gender")
        doc.instance_id = item.get("instanceID")
        doc.id_number = item.get("nationalID")
        doc.shortlist_status = item.get("shortlistStatus")
        # doc.status = item.get("status")
        doc.election_level = item.get("kRCSElectionLevel")
        
        
        
        doc.save(ignore_permissions=True)
        synced += 1

    return f"✅ {synced} candidates synced from EspoCRM."
