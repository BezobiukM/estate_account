{
    'name': 'Real Estate Invoicing',
    'version': '1.0',
    'depends': [
        'base',
        'estate',
        'account'
        ],
    'author': 'Bezobiuk M',
    'category': 'Real Estate/Brokerage',
    'description': """
    Description text
    Real estate account link module app 
    :)
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