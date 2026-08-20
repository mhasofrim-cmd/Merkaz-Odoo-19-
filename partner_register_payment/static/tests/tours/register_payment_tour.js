import { registry } from "@web/core/registry";
import { stepUtils } from "@web_tour/tour_utils";

registry.category("web_tour.tours").add("partner_register_payment_tour", {
    steps: () => [
        {
            trigger: 'input.o_searchview_input',
            run: "edit Register Payment Tour Customer",
        },
        {
            trigger: '.o_searchview_autocomplete .o-dropdown-item.focus',
            run: "click",
        },
        {
            trigger: '.o_data_row:first td[name="display_name"]',
            run: "click",
        },
        stepUtils.autoExpandMoreButtons(),
        {
            trigger: 'button[name="action_register_customer_payment"]',
            run: "click",
        },
        {
            trigger: '.o_dialog .modal-title:contains("Register Payment")',
        },
        {
            trigger: '.o_dialog .o_field_widget[name="partner_id"] input',
        },
        {
            trigger: '.o_dialog .btn-close',
            run: "click",
        },
        {
            trigger: '.o_breadcrumb',
        },
    ],
});
