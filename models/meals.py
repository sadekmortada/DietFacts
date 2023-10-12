from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Dietfacts_res_users_meal(models.Model):
    _name = 'meal.template'
    _description = "model description"
    name = fields.Char("Meal Name")
    user_id = fields.Many2one('res.users', "Meal User")
    item_ids = fields.One2many('mealitem.template',  'meal_id')
    notes = fields.Text("Meal Notes")
    totalcalories = fields.Integer(string="Total Calories", store=True, compute="_sumcalories")
    meal_date = fields.Datetime("Meal Date")
    largemeal = fields.Boolean("Large Meal",readonly=True)
    
    @api.onchange('totalcalories')
    def _checklarge(self):
        if self.totalcalories>500:
            self.largemeal = True
        else:
            self.largemeal = False

    @api.depends('item_ids', 'item_ids.servings')
    def _sumcalories(self):
        current = 0
        for mealitem in self.item_ids:
            current += mealitem.servings*mealitem.calories
        self.totalcalories = current

    @api.constrains('meal_date')
    def _validate_date(self):
        # for meal in self:
        if self.meal_date < fields.Datetime.today():
            raise ValidationError("The meal date can't be set in the past!")
        
        
        
        
        
        
        
        