from odoo import models,fields

class Dietfacts_res_users_mealitem(models.Model):
    _name = 'mealitem.template'
    _description = "model description"
    meal_id = fields.Many2one('meal.template', "Meal")
    item_id = fields.Many2one('product.template', "Item")
    servings = fields.Integer("Servings")
    calories = fields.Integer(related="item_id.calories", string="Calories per Serving", store=True, readonly=True)
    notes = fields.Text("Meal item notes")