# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from odoo import models, fields, api,_
from odoo.exceptions import Warning



class Containers(models.Model):
    _name = 'containers.containers'
    _description = 'New Description'

    name = fields.Char(string='Name')
    containers_id_type = fields.Many2one('containers.type', string='Containers Type')
    




class ShipmentType(models.Model):
    _name = 'shipment.type'
    _description = 'New Description'
    
    name = fields.Char(string='Name')




class ContainersType(models.Model):
    _name = 'containers.type'
    _description = 'New Description'
    name = fields.Char(string='Name')
