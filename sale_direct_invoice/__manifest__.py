# -*- coding: utf-8 -*-
{
    'name': "sale_direct_invoice",

    'summary': """
        sale_direct_invoice""",

    'description': """
      Confirm quotations, assign products and validate deliveries, then invoice the order
    """,

    'author': "Difference informatique",
    'website': "http://www.pole-erp-pgi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale_direct_invoice',
    'version': '14',

    # any module necessary for this one to work correctly
      'depends': [   
        'base',
        'account',
        'sale',
        'delivery',
        'popup' ,
        #FRPA 220413 'sale_direct_delivery'                                                     
        ],

    # always loaded
    'data': [  
        'security/ir.model.access.csv',
        "views/di_wiz_direct_invoice_view.xml",                                                                      
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
    'installable': True,    
}