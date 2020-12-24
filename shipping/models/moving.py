# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from odoo import models, fields, api,_
from odoo.exceptions import Warning

class Moving(models.Model):
    _name = 'moving.moving'
    _description = 'Moving Module'

    name = fields.Char(string='Name')
    moving_ref = fields.Many2one('sale.order', invisible=1, copy=False)
    moving_number =fields.Char("Moving Number",readonly=True)
    os_containers_rel_moving = fields.Many2many('containers.containers', 'os_containers_moving_id', 'os_moving_id3', 'container_moving_id', string="Containers")
    os_vehicle_rel_moving = fields.Many2many('fleet.vehicle', 'os_vehicle_moving_id', 'os_moving_idv', 'vehicle_moving_id', string="Vehicles")
    starting_point = fields.Char(string='Starting Point')
    end_point = fields.Char(string='End Point')
    note_moving = fields.Html(string='Note')
    
    


    
    
    

    @api.model
    def create(self,vals):
        seq = self.env['ir.sequence'].next_by_code('moving.moving') or '/'
        vals['moving_number'] = seq
        return super(Moving, self).create(vals)


    