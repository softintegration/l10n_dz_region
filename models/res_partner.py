# -*- coding: utf-8 -*- 


from odoo import models,fields,api
from odoo.exceptions import UserError

ADDRESS_FIELDS = ('street', 'street2', 'zip', 'municipality_id', 'state_id', 'country_id')
class ResPartner(models.Model):
    _inherit = "res.partner"

    #MODEL FIELDS
    municipality_id = fields.Many2one("res.country.municipality",string="Municipality")

    @api.onchange('municipality_id')
    def on_change_municipality_id(self):
        if self.municipality_id:
            self.state_id = self.municipality_id.state_id and self.municipality_id.state_id.id or False
            self.zip = self.municipality_id.zip


    @api.model
    def _address_fields(self):
        """Returns the list of address fields that are synced from the parent."""
        return list(ADDRESS_FIELDS)

    def _prepare_display_address(self, without_company=False):
        address_format, args = super(ResPartner,self)._prepare_display_address(without_company=without_company)
        address_format = address_format.replace("(city)s","(municipality_name)s %(state_name)s")
        municipality = args.get('municipality_id',False)
        if municipality:
            args.update({'municipality_name':municipality.name})
        return address_format,args
