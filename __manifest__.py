# -*- coding: utf-8 -*- 


{
    'name': 'Algeria territorial administrative subdivision',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.1',
    'category': 'Base',
    'demo': [],
    'depends': ['contacts'],
    'data': ['data/l10n_dz_region_data.xml',
             'security/ir.model.access.csv',
             'views/res_country_municipality_view.xml',
             'views/res_partner_view.xml',
             'views/res_company_view.xml',
             'views/l10n_dz_region_action.xml',
             'views/l10n_dz_region_menuitem.xml'
             ],
    'license': 'LGPL-3',
}
