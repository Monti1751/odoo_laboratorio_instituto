# -*- coding: utf-8 -*-
{
    'name': 'Configuración de Laboratorio',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Configura automáticamente categorías, ubicaciones, campos y vistas para la gestión de laboratorio.',
    'description': """
        Módulo de configuración automática para laboratorios educativos.
        Al instalarse crea:
        - Categorías de producto: Reactivos Químicos y Equipos de Laboratorio
        - Jerarquía de ubicaciones del laboratorio
        - Campos personalizados en product.template
        - Modelo de historial de uso de equipos
        - Vistas heredadas con pestañas condicionales por categoría
    """,
    'author': 'Monti1751',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/product_category_data.xml',
        'data/stock_location_data.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
