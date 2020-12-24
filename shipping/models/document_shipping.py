# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from odoo import models, fields, api
from odoo.exceptions import Warning

class ShippingDocument(models.Model):
    _name = 'shipping.document'
    _description = 'Shipping Documents'

    # def mail_reminder(self):
    #     """Sending document expiry notification to employees."""

    #     now = datetime.now() + timedelta(days=1)
    #     date_now = now.date()
    #     match = self.search([])
    #     for i in match:
    #         if i.expiry_date:
    #             exp_date = fields.Date.from_string(i.expiry_date) - timedelta(days=7)
    #             if date_now >= exp_date:
    #                 mail_content = "  Hello  " + i.employee_ref.name + ",<br>Your Document " + i.name + "is going to expire on " + \
    #                                str(i.expiry_date) + ". Please renew it before expiry date"
    #                 main_content = {
    #                     'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
    #                     'author_id': self.env.user.partner_id.id,
    #                     'body_html': mail_content,
    #                     'email_to': i.employee_ref.work_email,
    #                 }
    #                 self.env['mail.mail'].create(main_content).send()

    # @api.onchange('expiry_date','issue_date')
    # def check_date(self):
    #     exp_date = fields.Date.from_string(self.expiry_date)
    #     iss_date = fields.Date.from_string(self.issue_date)
    #     if iss_date and exp_date:
    #         if iss_date > exp_date:
    #             raise Warning('Issue date must be less than expiry date')

    # @api.constrains('expiry_date')
    # def check_expr_date(self):
    #     for each in self:
    #         if each.expiry_date:
    #             exp_date = fields.Date.from_string(each.expiry_date)
    #             if exp_date < date.today():
    #                 raise Warning('Your Document Is Expired.')

    name = fields.Char(string='Document Name', required=True, copy=False, help='You can give your')
    # document1_name = fields.Many2one('employee.checklist', string='Document', required=True)                                                                             'Document name.')
    doc_number = fields.Char(string='Document code')
    
    description = fields.Text(string='Description', copy=False)
    expiry_date = fields.Date(string='Expiry Date', copy=False)
    so_ref = fields.Many2one('sale.order', invisible=1, copy=False)
    doc_attachment_id = fields.Many2many('ir.attachment', 'doc_attach_rel', 'doc_id', 'attach_id3', string="Attachment",
                                         help='You can attach the copy of your document', copy=False)
    issue_date = fields.Date(string='Issue Date', default=fields.datetime.now(), copy=False)


class SoAttachment(models.Model):
    _inherit = 'ir.attachment'
    doc_attach_rel = fields.Many2many('shipping.document', 'doc_attachment_id', 'attach_id3', 'doc_id',
                                      string="Attachment", invisible=1)




