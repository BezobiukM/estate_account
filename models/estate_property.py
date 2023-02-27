import logging

from odoo import models, fields
from odoo import Command

_logger = logging.getLogger(__name__)


class EstateProperty(models.Model):
    _inherit = 'estate.property'
    account_move_id = fields.Many2one('account.move', string="Invoice")

    def action_property_sold(self):
        account_move = self.env['account.move'].sudo()
        self.env['account.move'].check_access_rights('write')
        self.env['account.move'].check_access_rule('write')   
        print("reached ".center(100, '='))
        for record in self:
            # _logger.error("\n$$$$$action_property_sold$$$$$$$$$$$\n")
            # _logger.error(record.salesman.id)
            # _logger.info("reached ".center(100, '='))
            # _logger.error("\n$$$$$action_property_sold_end$$$$$$$$$$$\n")

            record.account_move_id = account_move.create({
                'partner_id': record.offer_ids.partner_id,
                'move_type': 'out_invoice',
                'invoice_origin': record.name,
                "invoice_line_ids": [
                    Command.create({
                        "name": record.name,
                        "quantity": 1,
                        "price_unit": record.selling_price,
                    }),
                    Command.create({
                        "name": "6% of Selling Price",
                        "quantity": 1,
                        "price_unit": record.selling_price*0.06,
                    }),
                    (0, 0, {
                        "name": "Administrative fee",
                        "quantity": 1,
                        "price_unit": 100.00,
                        "display_type": False,
                    })
                ]
            })

        return super(EstateProperty, self).action_property_sold()
    
    
     