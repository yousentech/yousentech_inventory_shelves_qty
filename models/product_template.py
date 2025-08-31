from odoo import models, fields,api

class product_template(models.Model):
    _inherit = "product.template"

    ##########################################################################
    # shelf_ids = fields.Many2many("shelf", string="Shelf Name")

    # hide_shelf_field = fields.Boolean(default=lambda self: self._default_product_shelf_setting(),compute="_default_product_shelf_setting")

    # hide or show shelf fileds
    # def _default_product_shelf_setting(self):
    #     for rec in self: 
    #         enable_product_shelf = self.env["ir.config_parameter"].sudo().get_param("yousentech_inventory_shelves.deal_with_product_shelf")
    #         if enable_product_shelf:
    #             rec.hide_shelf_field = False
    #         else:
    #             rec.hide_shelf_field = True
    #######################################################           
    product_shelf_ids = fields.One2many("product.shelf", "product_tmpl_id", string="Shelves")
