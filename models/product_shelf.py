from odoo import models, fields, api


class product_shelf(models.Model):
    _name = "product.shelf"
    _description = "Quantity of product in the shelf"

    product_id = fields.Many2one("product.product", string='Product')
    shelf_id = fields.Many2one("shelf", string='Shelf Name')
    quantity = fields.Float(string='Quantity')

    product_tmpl_id = fields.Many2one("product.template",)

    