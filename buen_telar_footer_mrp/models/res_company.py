# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Company(models.Model):
    _inherit = 'res.company'

    buen_telar_report_footer_mrp = fields.Text('Footer for MRP Order')

    def get_models_custom_footer(self, doc=None):
        if self.env.user.company_id.buen_telar_report_footer_mrp and doc._name == 'mrp.production':
            return True
        return super(Company, self).get_models_custom_footer(doc=doc)