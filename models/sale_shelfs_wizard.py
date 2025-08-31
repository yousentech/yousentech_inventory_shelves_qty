# from odoo import models, fields, api, _
# from odoo.exceptions import ValidationError
# class sale_shelf_wizard_master(models.TransientModel):
#     _name = "sale.shelf.wizard.master"

#     product_id = fields.Many2one("product.template", string="Product Name")
#     sale_line_id = fields.Many2one("sale.order.line", string="Order Line")
#     shelf_line = fields.One2many("sale.shelf.wizard.detail", "master_id")

#     @api.onchange("product_id")
#     def add_shelf_lines(self):
#         for rec in self:
#             shelf_line_ids = []
#             for shelf in rec.product_id.product_shelf_ids:
#                 if shelf.quantity:
#                     vals = (
#                         0,
#                         0,
#                         {
#                             "shelf_id": shelf.shelf_id.id,
#                             "existing_quantity": shelf.quantity,
#                             "quantity": 0,
#                         },
#                     )
#                     shelf_line_ids.append(vals)
                    

#             self.shelf_line = shelf_line_ids
            
#     def confirm_shelf(self):
#         qty = 0
#         for rec in self.shelf_line:
#             qty += rec.quantity
#         if qty > self.sale_line_id.product_uom_qty:
#             # "الكميات المأخوذة من الأرفف أكبر من الكمية المحددة"
#             raise ValidationError(_("The quantity is greater than the available"))

#         if qty < self.sale_line_id.product_uom_qty:
#             # "الكميات المأخوذة من الأرفف أصغر من الكمية المحددة"
#             raise ValidationError(_("The quantities taken from the shelves are smaller than the specified quantity for the product"))

#         # update the quantity in the shelf
#         shelfs_in_product = self.env["product.shelf"].search([("product_tmpl_id", "=", self.product_id.id)])
#         for rec in self.shelf_line:
#             if rec.quantity:
#                 exit_shelf = shelfs_in_product.search([("shelf_id", "=", rec.shelf_id.id)])
#                 qty = rec.existing_quantity - rec.quantity
#                 exit_shelf.write({"quantity": qty})

# class sale_shelf_wizard_detail(models.TransientModel):
#     _name = "sale.shelf.wizard.detail"

#     shelf_id = fields.Many2one("shelf", string="Shelf Name")
#     existing_quantity = fields.Float(string="Available Quantity")
#     quantity = fields.Float(string="Quantity")
#     master_id = fields.Many2one("sale.shelf.wizard.master")

#     @api.onchange("quantity")
#     def add_shelf_lines(self):
#         # it should count the free quantity also but no files in sale for free quantity
#         if self.existing_quantity < self.quantity:
#             # "الكمية المطلوبة من الرف أكبر من الكمية الموجودة"
#             raise ValidationError(_("The quantity demanded from the shelf is greater than the quantity available"))
