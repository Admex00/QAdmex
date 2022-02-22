# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    buen_telar_report_footer_customer_invoice = fields.Text('Footer for customer invoice',
                                                readonly=False,
                                                related='company_id.buen_telar_report_footer_customer_invoice')