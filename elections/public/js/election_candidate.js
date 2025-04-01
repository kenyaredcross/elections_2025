frappe.listview_settings['Election Candidate'] = {
    onload(listview) {
        listview.page.add_button('Sync from EspoCRM', () => {
            frappe.call({
                method: 'elections.elections.api.espocrm_sync.sync_candidates_from_espocrm',
                callback: function(r) {
                    frappe.msgprint(r.message);
                    listview.refresh();
                }
            });
        });
    }
};
