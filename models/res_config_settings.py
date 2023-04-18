# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_group_discount_admin_id = fields.Many2one('res.groups', compute='_compute_discount_admin_group', store=True, readonly=False)

    @api.depends('pos_config_id')
    def _compute_discount_admin_group(self):
        for res_config in self:
            res_config.pos_group_discount_admin_id = res_config.pos_config_id.group_discount_admin_id
