from odoo import models, fields

class Website(models.Model):
    _name = 'custom.website'
    _description = 'Custom Website Model'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
