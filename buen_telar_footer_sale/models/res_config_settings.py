# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    buen_telar_report_footer_sale = fields.Text('Footer for Sale Printing',
                                                readonly=False,
                                                related='company_id.buen_telar_report_footer_sale')