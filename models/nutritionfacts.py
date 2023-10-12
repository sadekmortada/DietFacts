from odoo import fields, models

class Dietfacts_product_nutritionfacts(models.Model):
    _name = "nutritionfact.template"
    _description = "model description"
    nutrient_id = fields.Many2one('nutrient.template', "Product Nutrient")
    product_id = fields.Many2one('product.template')
    value = fields.Float('Nutrient Value')
    dailypercent = fields.Float("Daily Recommended Value")
    uom = fields.Char(related="nutrient_id.uom_id.name",string="Unit of Measure",readonly=True)