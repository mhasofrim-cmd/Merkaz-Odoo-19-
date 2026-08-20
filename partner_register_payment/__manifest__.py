{
    'name': 'Partner Register Payment',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Register a customer payment directly from the contact form',
    'depends': ['account'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_tests': [
            'partner_register_payment/static/tests/tours/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
