# -*- coding: utf-8 -*- 


from odoo import models,fields,api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    #MODEL FIELDS
    municipality_id = fields.Many2one("res.country.municipality",string="Municipality")

    @api.onchange('municipality_id')
    def on_change_municipality_id(self):
        if self.municipality_id:
            self.state_id = self.municipality_id.state_id and self.municipality_id.state_id.id or False
            self.zip = self.municipality_id.zip