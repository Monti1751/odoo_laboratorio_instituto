# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date, datetime


class LabEquipmentUsage(models.Model):
    _name = 'lab.equipment.usage'
    _description = 'Historial de Uso de Equipos de Laboratorio'
    _order = 'fecha_uso desc, hora_uso desc'

    product_id = fields.Many2one(
        'product.template',
        string='Equipo',
        required=True,
        ondelete='cascade',
    )

    usuario_id = fields.Many2one(
        'res.users',
        string='Usuario',
        default=lambda self: self.env.user,
        readonly=True,
    )

    fecha_uso = fields.Date(
        string='Fecha de uso',
        default=fields.Date.today,
        readonly=True,
    )

    hora_uso = fields.Char(
        string='Hora',
        readonly=True,
    )

    observaciones = fields.Text(
        string='Observaciones',
    )

    @api.model_create_multi
    def create(self, vals_list):
        now = datetime.now().strftime('%H:%M')
        for vals in vals_list:
            if not vals.get('hora_uso'):
                vals['hora_uso'] = now
            if not vals.get('fecha_uso'):
                vals['fecha_uso'] = date.today()
            if not vals.get('usuario_id'):
                vals['usuario_id'] = self.env.user.id
        return super().create(vals_list)
