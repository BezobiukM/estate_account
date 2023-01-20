import logging

from odoo import models, fields
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_property_sold(self):
        for record in self:
            _logger.error("$$$$$action_property_sold$$$$$$$$$$$\n")
            _logger.error(record.state)
            _logger.error("$$$$$action_property_sold_end$$$$$$$$$$$")
        return super(EstateProperty, self).action_property_sold()
 
    
    