import logging

from odoo import models, fields
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_property_sold(self):
        accountMove = self.env['account.move'].sudo()
        for record in self:
            _logger.error("$$$$$action_property_sold$$$$$$$$$$$\n")
            _logger.error(record.state)
            _logger.error("$$$$$action_property_sold_end$$$$$$$$$$$")

            accountMove.create({
                'partner_id': record.salesman,
                'move_type': 'out_invoice',
                'invoice_origin': record.name,
            })
        return super(EstateProperty, self).action_property_sold()
