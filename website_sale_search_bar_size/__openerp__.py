# -*- encoding: utf-8 -*-
# #############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Website Sale Search Bar Size',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Website',
    'summary': 'Resize the search bar',
    'description': """
Website Sale Search Bar Size
============================
This module resize the search bar of the shop page in the front office,
to a human usable size.

Disclaimer
----------
The size of the bar is hard coded in the view and should not fit
for responsive design.
It is mainly a temporary fix in meantime Odoo offers its answer.

Contributors
------------
* Jordi RIERA (jordi.riera@savoirfairelinux.com)
* William BEVERLY (william.beverly@savoirfairelinux.com)
* Bruno JOLIVEAU (bruno.joliveau@savoirfairelinux.com)

More informations
--------------------
* Module developed and tested with Odoo version 8.0
* For questions, please contact our support services \
(support@savoirfairelinux.com)
""",
    'depends': [
        'website_sale'
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'website_sale_templates.xml',
    ],
    'installable': True,
}
