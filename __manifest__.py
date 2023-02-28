{
    'name': 'Real Estate Invoicing',
    'version': '1.0',
    'depends': [
        'base',
        'estate',
        'account'
        ],
    'author': 'Maria Bezobiuk',
    'category': 'Real Estate/Brokerage',
    'description': """
    The Real Estate Advertisement Invoicing module
    Odoo provides an Invoicing module, once a property is set to ‘Sold’ in Real Estate application, an invoice is created in the Invoicing application.
    """,
    'data': [
        'report/estate_property_templates.xml',
        'views/estate_property_view.xml'
        ]
    ,
    'installable': True,
    'application': True,
    'auto_install': False
}