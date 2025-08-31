# from odoo import api, models, fields,_
# from odoo.exceptions import ValidationError

# class purchase_order(models.Model):
#     _inherit = "purchase.order"

#     hide_shelf_field = fields.Boolean(default=lambda self: self._default_product_shelf_setting())

#     # hide shelf field in purchase order line
#     def _default_product_shelf_setting(self):
#         enable_product_shelf = self.env["ir.config_parameter"].sudo().get_param("yousentech_inventory_shelves.deal_with_product_shelf")
#         if enable_product_shelf:
#             return False
#         else:
#             return True

#     ADD SHELFS TO PRODUCT CARD IF NOT ALREADY EXISTS
#     @api.constrains("order_line")
#     def get_product_shelf(self):
#         for rec in self:
#             for line in rec.order_line:
#                 for shelf_id in line.shelf_ids:
#                     if not shelf_id.id in line.product_id.shelf_ids.ids:
#                         line.product_id.write({"shelf_ids": [(4, shelf_id.id)]})
    
    
#     def button_confirm(self):
#         res = super(purchase_order, self).button_confirm()        
#         pickings = self.picking_ids
#         if pickings:
#             for line in self.order_line:
#                 for move in self.picking_ids.move_ids.filtered(lambda x: x.purchase_line_id.id == line.id):
#                     move.write({'purchase_shelf_ids':line.shelf_ids.ids})
#         return res     
                           

                                
