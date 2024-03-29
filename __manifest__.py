# -*- coding: utf-8 -*-
{
    'name': 'Point of Sale Managed Discounts',
    'version': '1.1',
    'author': 'Benlever Pvt Ltd',
    'company': 'Benelever Pvt Ltd',
    'website': 'https://www.benlever.com',
    'maintainer': 'Benlever Pvt Ltd',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Managed Discounts in the Point of Sale',
    'description': """

This module managed the discount % given to the customer. Super groups are allowed to go beyond the set discount limit

""",
    'depends': ['point_of_sale', 'pos_discount'],
    'data': [
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_managed_discount/static/src/js/**/*'
        ],
    },
    'license': 'LGPL-3',
}
