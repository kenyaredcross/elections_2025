frappe.ready(function() {
	// bind events here
})

frappe.web_form.validate = () => {
    
	if (frappe.web_form.get_value([id_number]) != "xxx") {
		frappe.msgprint("not succesful");

		return false;
	}

}


