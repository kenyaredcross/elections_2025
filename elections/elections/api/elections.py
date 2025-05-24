import frappe
from frappe import _
from elections.elections.api.utils import get_userScope

#Test Comment

@frappe.whitelist()
def get_eligible_candidates_filtered (election_level=None,election_sub_level=None,county=None,region=None,position=None):
    
    # userScope = get_userScope()

    # if county not in userScope["counties"] :
    #     frappe.throw ("You are not allowed to access candidates from this County.")
    #     frm.clear_table("Candidate_votes")
    # elif region not in userScope["regions"]:
    #     frappe.throw ("You are not allowed to access candidates from this Region")
    #     frm.clear_table("Candidate_votes")
    # else: 
        return frappe.get_all(
        "Election Candidate", 
        filters = {
            "election_level" : election_level,
            "election_sub_level" : election_sub_level,
            "county" : county,
            "region" : region,
            "position" : position,
            "shortlist_status" : "pass" 
        },
        fields = [
            "name", "full_name", "id_number", "county", "region", "election_level", "election_sub_level", "position"
        ],
        limit_page_length = 100 )
    


   

    # #Check if user is a returning officer with access

    # allowed_counties = frappe.get_all (
    #     "Returning Officer Assignment",
    #     filters={
    #         "user": user
    #     },
    #     pluck = "county"
    # )

    # if county not in allowed_counties:
    #     frappe.throw(_("you are not allowed to access candidates from this county"))

    #Get the Candidates 

    

    

    
