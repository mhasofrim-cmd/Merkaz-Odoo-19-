from odoo.tests.common import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestRegisterPaymentTour(HttpCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env['res.partner'].create({
            'name': 'Register Payment Tour Customer',
        })
        admin = cls.env.ref('base.user_admin')
        admin.group_ids = [(4, cls.env.ref('account.group_account_invoice').id)]

    def test_register_payment_tour(self):
        self.start_tour(
            "/odoo/contacts",
            "partner_register_payment_tour",
            login="admin",
        )
