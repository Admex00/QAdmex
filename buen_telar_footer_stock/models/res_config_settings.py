# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    buen_telar_report_footer_picking = fields.Text('Footer for Picking',
                                                readonly=False,
                                                related='company_id.buen_telar_report_footer_picking')