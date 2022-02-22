# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Company(models.Model):
    _inherit = 'res.company'

    buen_telar_report_footer_customer_invoice = fields.Text('Footer for customer invoice')

    def get_models_custom_footer(self, doc=None):
        if self.env.user.company_id.buen_telar_report_footer_customer_invoice and doc._name == 'account.move':
            if doc.move_type in ['out_invoice', 'out_refund']:
                print("Esto es en Factura")
                return True
        return super(Company, self).get_models_custom_footer(doc=doc)