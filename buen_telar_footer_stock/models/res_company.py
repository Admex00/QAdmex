# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Company(models.Model):
    _inherit = 'res.company'

    buen_telar_report_footer_picking = fields.Text('Footer for Picking')

    def get_models_custom_footer(self, doc=None):
        if self.env.user.company_id.buen_telar_report_footer_picking and doc._name == 'stock.picking':
            return True
        return super(Company, self).get_models_custom_footer(doc=doc)