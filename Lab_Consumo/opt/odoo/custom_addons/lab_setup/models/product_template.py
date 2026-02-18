# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # ─── Campos para Reactivos Químicos ───────────────────────────────────────

    x_formula_quimica = fields.Char(
        string='Fórmula química',
        help='Fórmula molecular del reactivo (ej: H₂SO₄)',
    )

    x_CAS = fields.Char(
        string='CAS',
        help='Número de registro CAS del reactivo',
    )

    x_pureza = fields.Char(
        string='Pureza',
        help='Nivel de pureza del reactivo (ej: 99%, 95%)',
    )

    x_estado_de_agregacion = fields.Selection(
        selection=[
            ('solido', 'Sólido'),
            ('liquido', 'Líquido'),
            ('gaseoso', 'Gaseoso'),
        ],
        string='Estado de agregación',
    )

    x_densidad = fields.Float(
        string='Densidad (g/cm³)',
        digits=(10, 4),
    )

    x_punto_de_fusion = fields.Float(
        string='Punto de fusión (°C)',
        digits=(10, 2),
    )

    x_punto_de_ebullicion = fields.Float(
        string='Punto de ebullición (°C)',
        digits=(10, 2),
    )

    x_pictograma_de_peligrosidad = fields.Char(
        string='Pictogramas de peligrosidad',
        help='Símbolos de seguridad (ej: GHS01, GHS06)',
    )

    x_fecha_de_caducidad = fields.Date(
        string='Fecha de caducidad',
    )

    x_fecha_de_apertura = fields.Date(
        string='Fecha de apertura',
    )

    x_advertencia_seguridad = fields.Text(
        string='Advertencia de seguridad',
        help='Advertencias de uso para el reactivo',
    )

    # ─── Campos para Equipos de Laboratorio ──────────────────────────────────

    x_codigo_equipo = fields.Char(
        string='Código del equipo',
        help='Identificador único del equipo',
    )

    x_funcion = fields.Text(
        string='Función',
        help='Descripción del uso del equipo',
    )

    x_proximo_mantenimiento = fields.Date(
        string='Próximo mantenimiento',
    )

    x_observaciones = fields.Text(
        string='Observaciones',
        help='Notas generales sobre el equipo',
    )

    equipment_usage_ids = fields.One2many(
        'lab.equipment.usage',
        'product_id',
        string='Historial de uso',
    )

    # ─── Campos computados para visibilidad de pestañas ──────────────────────
    # Odoo 17: invisible= evalúa expresiones Python simples en el cliente.
    # No se pueden usar ref() en esas expresiones, por eso usamos booleanos
    # computados que el cliente puede evaluar directamente.

    is_reactivo = fields.Boolean(
        string='Es reactivo',
        compute='_compute_lab_type',
        store=False,
    )

    is_equipo = fields.Boolean(
        string='Es equipo',
        compute='_compute_lab_type',
        store=False,
    )

    @api.depends('categ_id')
    def _compute_lab_type(self):
        categ_reactivos = self.env.ref(
            'lab_setup.categ_reactivos', raise_if_not_found=False
        )
        categ_equipos = self.env.ref(
            'lab_setup.categ_equipos', raise_if_not_found=False
        )
        for record in self:
            record.is_reactivo = (
                categ_reactivos and record.categ_id == categ_reactivos
            )
            record.is_equipo = (
                categ_equipos and record.categ_id == categ_equipos
            )
