# from odoo import models, fields, api
# from odoo.exceptions import ValidationError


# class StockPicking(models.Model):
#     _inherit = "stock.picking"

#     def button_validate(self):
#         res = super().button_validate()
#         for picking in self:
#             if picking.picking_type_code == 'outgoing':
#                 picking._update_shelf_quantities_sales()
#             if picking.picking_type_code == 'incoming':
#                 picking._update_shelf_quantities_purchase()

#             # Handle returns/refunds
#             if picking.picking_type_code == 'incoming' and picking.return_id:
#                 picking._update_shelf_quantities_sale_refund()
#             if picking.picking_type_code == 'outgoing' and picking.return_id:
#                 picking._update_shelf_quantities_purchase_refund()

#         return res

#     def _update_shelf_quantities_sales(self):
#         for move in self.move_ids:
#             if move.sale_shelf_ids:
#                 available_qty = self._get_available_shelf_quantity(
#                     move.product_id.product_tmpl_id,
#                     move.sale_shelf_ids
#                 )
#                 if available_qty < move.quantity:
#                     raise ValidationError(
#                         f"Not enough quantity for product {move.product_id.product_tmpl_id.name} in selected shelves. "
#                         f"Available: {available_qty}, Required: {move.quantity}"
#                     )
#                 if self.picking_type_code == 'outgoing' and move.sale_shelf_ids and move.quantity > 0:
#                     move._update_shelf_quantities_sales()

#     def _update_shelf_quantities_purchase(self):
#         for move in self.move_ids:
#             if move.purchase_shelf_ids:
#                 if self.picking_type_code == 'incoming' and move.purchase_shelf_ids and move.quantity > 0:
#                     move._update_shelf_quantities_purchase()

#     def _update_shelf_quantities_sale_refund(self):
#         for move in self.move_ids:
#             if move.origin_returned_move_id and move.origin_returned_move_id.sale_shelf_ids:
#                 move._update_shelf_quantities_sale_refund()

#     def _update_shelf_quantities_purchase_refund(self):
#         for move in self.move_ids:
#             # available_qty = self._get_available_shelf_quantity(
#             #         move.product_id.product_tmpl_id,
#             #         move.origin_returned_move_id.purchase_shelf_ids
#             #     )
#             # if available_qty < move.quantity:
#             #         raise ValidationError(
#             #             f"Not enough quantity for product {move.product_id.product_tmpl_id.name} in selected shelves. "
#             #             f"Available: {available_qty}, Required: {move.quantity}"
#             #         )
#             if move.origin_returned_move_id and move.origin_returned_move_id.purchase_shelf_ids:
#                 move._update_shelf_quantities_purchase_refund()
                
#     def _get_available_shelf_quantity(self, product, shelves):
#         """Get total available quantity for product in selected shelves"""
#         shelf_records = self.env['product.shelf'].search([
#             ('product_tmpl_id', '=', product.id),
#             ('shelf_id', 'in', shelves.ids)
#         ])
#         return sum(shelf_records.mapped('quantity'))


