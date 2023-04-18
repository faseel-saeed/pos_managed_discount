# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from uuid import uuid4
import pytz

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError


class PosConfig(models.Model):
    _inherit = 'pos.config'

    group_discount_admin_id = fields.Many2one('res.groups', string='Point of Sale Discount Admin Group',
        help='This group has the ability to grant discounts more than the default limit')

