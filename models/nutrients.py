from odoo import fields, models


class Dietfacts_product_nutrient(models.Model):
    _name = 'nutrient.template'
    _description = "model description"
    name = fields.Char("Nutrient Name")
    uom_id = fields.Many2one("uom.uom", "Unit of Measure")
    description = fields.Text("Description")
