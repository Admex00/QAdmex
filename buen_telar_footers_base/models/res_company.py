# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Company(models.Model):
    _inherit = 'res.company'

    def get_models_custom_footer(self, doc=None):
        # print("si -----", doc)
        return False