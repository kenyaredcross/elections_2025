import frappe

@frappe.whitelist()
def get_userScope(user=None):
    user = user or frappe.session.user
    
    #Get Assigned areas for the user
    
    assigned_area = frappe.get_all(
        "Returning Officer Assignment",
        filters = {
            "returning_officer" : user,
            "active": 1
        },
        pluck = "name"
    )
    
    rows = frappe.get_all(
        "Returning Officer Area",
        filters = {
            "parent" : ["in", assigned_area]
        },
        fields = ["region","county"]
    )
    
    regions = list({r.region for r in rows if r.region})
    counties = list({r.county for r in rows if r.county})
    
    return {
        "regions": regions,
        "counties" : counties
    }




# def get_userScope (user=None) :
#     user = user or frappe.session.user

#     rows = frappe.get_all (
#         "Returning Officer Assignment",
#         filters = { "parent": assignment_name, "active": 1},
#         fields = ["region", "county"]
#     )

#     regions = list({r.region for r in rows if r.region})
#     counties = list({r.county for r in rows if r.county})

#     return {"regions": regions, "counties":counties}