# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class LabConsumoReactivo(models.Model):
    _name = 'lab.consumo.reactivo'
    _description = 'Consumo de Reactivos de Laboratorio'

    producto_id = fields.Many2one(
        'product.product',  
        string='Reactivo',  
        required=True
    )
     
    cantidad_usada = fields.Float(
        string='Cantidad usada',
        required=True
    )

    alumno_id = fields.Many2one(
        'res.partner',
        string='Alumno'
    )

    fecha = fields.Datetime(
        string='Fecha',
        default=fields.Datetime.now
    )

    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('done', 'Consumido')
        ],
        default='draft',
        string='Estado'
    )

    def action_consumir(self):
        for record in self:
            if record.state == 'done':
                continue

            if record.cantidad_usada <= 0:
                raise UserError("La cantidad debe ser mayor que cero")

            if record.producto_id.qty_available < record.cantidad_usada:
                raise UserError(f"No hay stock suficiente. Disponible: {record.producto_id.qty_available}")

            # Buscamos las ubicaciones
            ubicacion_stock = self.env.ref('stock.stock_location_stock')
            ubicacion_consumo = self.env.ref('stock.stock_location_customers')

            # 1. Crear el movimiento
            movimiento = self.env['stock.move'].create({
                'name': f'Consumo de {record.producto_id.name}',
                'product_id': record.producto_id.id,
                'product_uom_qty': record.cantidad_usada,
                'product_uom': record.producto_id.uom_id.id,
                'location_id': ubicacion_stock.id,
                'location_dest_id': ubicacion_consumo.id,
            })

            # 2. Confirmar y asignar (Todo esto debe estar alineado aquí dentro)
            movimiento._action_confirm()
            movimiento._action_assign()

            # 3. Registrar la cantidad realizada
            for line in movimiento.move_line_ids:
                line.qty_done = record.cantidad_usada

            # 4. Validar y finalizar
            movimiento._action_done()
            record.state = 'done'
