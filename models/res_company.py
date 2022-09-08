# -*- coding: utf-8 -*- 

from odoo import models,fields,api
from odoo.exceptions import UserError


class ResCompany(models.Model):
    _inherit = "res.company"

    #MODEL FIELDS
    municipality_id = fields.Many2one("res.country.municipality",string="Municipality")


    @api.onchange('municipality_id')
    def on_change_municipality_id(self):
        if self.municipality_id:
            self.state_id = self.municipality_id.state_id and self.municipality_id.state_id.id or False
            self.zip = self.municipality_id.zip

    @api.model
    def create(self,vals):
        rec = super(ResCompany, self).create(vals)
        rec.partner_id.write({
            'municipality_id':rec.municipality_id and rec.municipality_id.id or False,
            'state_id': rec.state_id and rec.state_id.id or False,
            'zip':rec.zip
        })
        return rec