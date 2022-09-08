# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError


class ResCountryMunicipality(models.Model):
    _name = "res.country.municipality"
    _description = 'Municipality'

    #MODEL FIELDS
    name = fields.Char(string="Name",required=True)
    code = fields.Char(string="Code")
    state_id = fields.Many2one("res.country.state",string="State",required=True)
    zip = fields.Char(string="Zip")
    company_id = fields.Many2one("res.company",string="Company",required=True,default=lambda self: self.env.company)

