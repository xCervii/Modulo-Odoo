# -*- coding: utf-8 -*-
{
    'name': "clubpadel",

    'summary': """
        Un módulo que te ayuda a ver los clubes, marcas en colaboración y sus respectivas palas.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Adrian29",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
