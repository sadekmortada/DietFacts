# Dietfacts Application
from odoo import models, fields, api


# Extend product template model with calories, etc..
class Dietfacts_products_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    calories = fields.Integer("Calories")
    servingsize = fields.Float("Serving Size")
    nutrition_ids = fields.One2many('nutritionfact.template', 'product_id')
    nutritionscore = fields.Float(string="Nutrition Score", store=True, compute='_sumnutritionscore')

    @api.depends('nutrition_ids', 'nutrition_ids.value')
    def _sumnutritionscore(self):
        current = 0
        for nutrition in self.nutrition_ids:
            if nutrition.nutrient_id.name == 'Sodium':
                current += nutrition.value * 5
            else:
                current += nutrition.value
        self.nutritionscore = current
