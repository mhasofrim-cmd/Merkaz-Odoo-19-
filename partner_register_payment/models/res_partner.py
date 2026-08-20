from odoo import models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_register_customer_payment(self):
        self.ensure_one()
        return {
            'name': _('Register Payment'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_id': self.id,
                'default_payment_type': 'inbound',
                'default_partner_type': 'customer',
            },
        }
