{
'name' : "DietFacts",
'version' : "1.0",
'author' : "SMM",
'depends' : ['sale'],
'installable' : True,
'data' : ['security/ir.model.access.csv',
    'views/dietfacts_view.xml',
    'views/meals_view.xml',
    'views/nutrients_view.xml',
    'views/nutritionfacts_view.xml',
    'views/mealitems_view.xml',
          ],
'description' : "Adds nutrition information to products",
'license': 'LGPL-3'
}
