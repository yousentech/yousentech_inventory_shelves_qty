# from odoo import models, fields,_
# from odoo.exceptions import ValidationError

# class sale_order(models.Model):
#     _inherit = "sale.order"
    
#     hide_shelf_field = fields.Boolean(default=lambda self: self._default_product_shelf_setting())

#     # HIDE THE SHELF COLOUM  IN SALE OREDR LINE
#     def _default_product_shelf_setting(self):
#         enable_product_shelf = self.env["ir.config_parameter"].sudo().get_param("yousentech_inventory_shelves.deal_with_product_shelf")
#         if enable_product_shelf:
#             return False
#         else:
#             return True
        
  
#     def action_confirm(self):
#         res = super(sale_order, self).action_confirm()
#         pickings = self.picking_ids
#         if pickings:
#             for line in self.order_line:
#                 for move in self.picking_ids.move_ids.filtered(lambda x: x.sale_line_id.id == line.id):
#                     move.write({'sale_shelf_ids':line.shelf_ids.ids})
#         return res                     
                      


