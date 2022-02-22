# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Company(models.Model):
    _inherit = 'res.company'

    buen_telar_report_footer_sale = fields.Text('Footer for sale management')

    def get_models_custom_footer(self, doc=None):
        # print("si -----", doc)
        if self.env.user.company_id.buen_telar_report_footer_sale and doc._name == 'sale.order':
            print("Esto es en venta")
            return True
        return super(Company, self).get_models_custom_footer(doc=doc)