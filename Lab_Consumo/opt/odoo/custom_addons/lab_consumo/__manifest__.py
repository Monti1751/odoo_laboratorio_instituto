{
    'name': 'Consumo de Reactivos de Laboratorio',
    'version': '1.0',
    'category': 'Inventory',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/consumo_reactivo_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
