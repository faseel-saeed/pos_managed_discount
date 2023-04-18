# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from datetime import timedelta
from itertools import groupby

from odoo import api, fields, models, _, Command
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
from odoo.osv.expression import AND, OR
from odoo.service.common import exp_version


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_users(self):
        return {
            'search_params': {
                'domain': [('id', '=', self.env.user.id)],
                'fields': ['name', 'groups_id'],
            },
        }

    def _get_pos_ui_res_users(self, params):
        user = self.env['res.users'].search_read(**params['search_params'])[0]
        user['role'] = 'manager' if any(id == self.config_id.group_pos_manager_id.id for id in user['groups_id']) else 'cashier'

        user['discount_admin'] = True if any(
            id == self.config_id.group_discount_admin_id.id for id in user['groups_id']) else False

        del user['groups_id']
        return user

