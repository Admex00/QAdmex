# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    buen_telar_report_footer_mrp = fields.Text('Footer for MRP Order',
                                                readonly=False,
                                                related='company_id.buen_telar_report_footer_mrp')