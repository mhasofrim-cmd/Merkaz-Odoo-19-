from odoo.tests.common import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestResPartnerRegisterPayment(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env['res.partner'].create({
            'name': 'Register Payment Unit Test Customer',
        })

    def test_action_returns_prefilled_payment_action(self):
        action = self.partner.action_register_customer_payment()
        self.assertEqual(action['res_model'], 'account.payment')
        self.assertEqual(action['view_mode'], 'form')
        self.assertEqual(action['target'], 'new')
        self.assertEqual(action['context']['default_partner_id'], self.partner.id)
        self.assertEqual(action['context']['default_payment_type'], 'inbound')
        self.assertEqual(action['context']['default_partner_type'], 'customer')

    def test_action_context_prefills_a_valid_payment(self):
        action = self.partner.action_register_customer_payment()
        payment = self.env['account.payment'].with_context(action['context']).new()
        self.assertEqual(payment.partner_id, self.partner)
        self.assertEqual(payment.payment_type, 'inbound')
        self.assertEqual(payment.partner_type, 'customer')

    def test_action_requires_a_single_partner(self):
        other_partner = self.env['res.partner'].create({'name': 'Another Customer'})
        partners = self.partner + other_partner
        with self.assertRaises(ValueError):
            partners.action_register_customer_payment()
