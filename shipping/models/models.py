# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from odoo import models, fields, api,_
from odoo.exceptions import Warning
# class shipping(models.Model):
#     _name = 'shipping.shipping'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

# STATE = [('draft','Draft'),
#          ('weating','Weating'),
#          ('approve','Approve'),
#          ('done','Done'),
#          ('rejuct','Rejuct')
#          ]

# class ShippingProcess(models.Model):
#     _name = 'shipping.process'
#     _description = "Shipping Process"
#     name = fields.Char(string="Title", required=True)
#     pro_num = fields.Char(string='NO Shipping Process',readonly=True)
#     cutomer_shipping = fields.Many2one('res.partner', string='Partner', required=True)
#     state = fields.Selection(STATE, "Status", readonly=True, default="draft")   
#     @api.model
#     def create(self,vals):
#         seq = self.env['ir.sequence'].next_by_code('shipping.process') or '/'
#         vals['pro_num'] = seq
#         return super(Regute, self).create(vals) 

# class ResPartnerPatient(models.Model):
#     _inherit = 'res.partner'

#     is_patient = fields.Boolean(string='Is Patient')
#     is_physician = fields.Boolean(string='Is Physician')
#     speciality = fields.Many2one('physician.speciality', string='Speciality')
#     hospital = fields.Many2one('res.partner', string='Hospital')



class  SaleOrder(models.Model):
    _inherit = 'sale.order'
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Waiting'),
        ('sale', 'Shipping'),
        ('unloading', 'Unloading'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True,default='draft')
    name_100 = fields.Char(string='Name')

    @api.multi
    def unloading(self):
        self.state = 'unloading'

    @api.multi
    def done(self):
        self.state = 'done'


    @api.multi
    def _document_count(self):
        for each in self:
            document_ids = self.env['shipping.document'].sudo().search([('so_ref', '=', each.id)])
            each.document_count = len(document_ids)

    @api.multi
    def document_view(self):
        self.ensure_one()
        domain = [
            ('so_ref', '=', self.id)]
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'shipping.document',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click to Create for New Documents
                        </p>'''),
            'limit': 80,
            'context': "{'default_so_ref': '%s'}" % self.id
        }

    document_count = fields.Integer(compute='_document_count', string='# Documents')
    





    @api.multi
    def _moving_count(self):
        for each in self:
            moving_ids = self.env['moving.moving'].sudo().search([('moving_ref', '=', each.id)])
            each.moving_count = len(moving_ids)

    @api.multi
    def moving_view(self):
        self.ensure_one()
        domain = [
            ('moving_ref', '=', self.id)]
        return {
            'name': _('Moves'),
            'domain': domain,
            'res_model': 'moving.moving',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click to Create for New Moving
                        </p>'''),
            'limit': 80,
            'context': "{'default_moving_ref': '%s'}" % self.id
        }
    
    moving_count = fields.Integer(compute='_moving_count', string='# Containers')

    # adding  field
    shippers_name = fields.Many2one('res.partner', string='Shippers Name')
    recipients_name = fields.Many2one('res.partner', string='Recipients Name')
    typeofshipment = fields.Many2one('shipment.type', string='Type Of Shipment')
    moveport = fields.Many2one('port.name', string='Move Port')
    accessport = fields.Many2one('port.name', string='Access Port')
    typeofcontainers = fields.Many2one('containers.type', string='Type Of Containers')
    os_containers_rel = fields.Many2many('containers.containers', 'os_containers_id', 'os_id3', 'container_id',
                                      string="Containers")
    numberofcontainers = fields.Char(string='Number of Containers')
    the_total_weight = fields.Char(string='The Total Weight')
    number_of_packages = fields.Char(string='Number Of Packages')

    os_vehicle_rel = fields.Many2many('fleet.vehicle', 'os_vehicle_id', 'os_idv', 'vehicle_id',
                                      string="Vehicles")
    class PortName(models.Model):
        _name = 'port.name'
        _description = 'New Description'
        name = fields.Char(string='Name Port')


    
    
    
    
    


    
    
    
    
    
    