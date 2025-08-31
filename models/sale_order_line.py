# from odoo import api, models, fields
# class sale_order_line(models.Model):
#     _inherit = "sale.order.line"

#     shelf_ids = fields.Many2many("shelf", string="Shelf")
    
#     shelf_ids_domain = fields.Char("shelf_ids_domain", compute="_get_shelf_domain")
   
#     @api.depends('product_template_id')
#     def _get_shelf_domain(self):
#         for record in self:
#             if record.product_template_id and record.product_template_id.product_shelf_ids:
#                 shelf_ids = record.product_template_id.product_shelf_ids.shelf_id.ids
#                 record.shelf_ids_domain = [('id', 'in', shelf_ids)]
#             else:
#                 record.shelf_ids_domain = [('id', '=', False)]

#     ACTION IF CLICK THE SHELF BUTTON ON SALE OREDER LINE
#     def get_shelfs(self):
#         return {
#             "type": "ir.actions.act_window",
#             "name": "shelves",
#             "view_mode": "form",
#             "view_type": "form",
#             "res_model": "sale.shelf.wizard.master",
#             "target": "new",
#             "domain": "",
#             "context": {
#                 "default_product_id": self.product_template_id.id,
#                 "default_sale_line_id": self.id,
#             },
#         }
