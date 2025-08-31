# from odoo import models, fields, _

# class purchase_orderLine(models.Model):
#     _inherit = "purchase.order.line"

#     shelf_ids = fields.Many2many("shelf", string="Shelf")
 
#     on click shelfs button
#     def get_shelfs(self):
#         return {
#             "type": "ir.actions.act_window",
#             "name": "shelves",
#             "view_mode": "form",
#             "view_type": "form",
#             "res_model": "shelf.wizard.master",
#             "target": "new",
#             "domain": "",
#             "context": {
#                 "default_product_id": self.product_id.product_tmpl_id.id,
#                 "default_po_line_id": self.id,
#             },
#         }




    