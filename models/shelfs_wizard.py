from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class shelf_wizard_master(models.TransientModel):
    _name = "shelf.wizard.master"

    product_tmpl_id = fields.Many2one("product.template", string="Product")
    move_id = fields.Many2one("stock.move", string="Stock move")
    shelf_lines = fields.One2many("shelf.wizard.detail", "master_id")
    existing_quantity = fields.Float(string="Existing Quantity")

    @api.onchange("product_tmpl_id")
    def add_shelf_lines(self):
        for rec in self:
            uom_factor = rec.move_id.get_uom_factor(rec.move_id.product_uom)
            rec.existing_quantity = rec.move_id.quantity * uom_factor
            # add wizard lines
            shelf_line_ids = []
            for shelf in rec.move_id.shelf_ids:
                vals = (0, 0,
                        {
                            "shelf_id": shelf.id,
                            "quantity": 0,
                        })
                shelf_line_ids.append(vals)

            rec.shelf_lines = shelf_line_ids

    def confirm_shelf(self):
        uom_factor = self.move_id.get_uom_factor(
            self.move_id.purchase_line_id.product_uom if self.move_id.purchase_line_id 
            else (self.move_id.sale_line_id.product_uom if self.move_id.sale_line_id 
                else self.move_id.product_uom))
        
        qty = sum(rec.quantity for rec in self.shelf_lines) * uom_factor
        if qty  > self.existing_quantity :
            # "الكميات المأخوذة من الأرفف أكبر من الكمية المحددة"
            raise ValidationError( _("The quantity is greater than the available"))

        if qty  < self.existing_quantity :
            # "الكميات المأخوذة من الأرفف أصغر من الكمية المحددة"
            raise ValidationError(_("The quantities taken from the shelves are smaller than the specified quantity for the product"))
   
        for rec in self.shelf_lines:
            if self.move_id.picking_id.picking_type_code == 'outgoing' and self.shelf_lines or self.move_id.picking_id.picking_type_code == 'outgoing' and self.move_id.picking_id.return_id:
                   
                available_qty = self.move_id._get_available_shelf_quantity(
                    self.move_id.product_id.product_tmpl_id,rec.shelf_id)
                if available_qty < rec.quantity:
                    raise ValidationError(
                        f"Not enough quantity for product {self.move_id.product_id.product_tmpl_id.name} in selected shelves. "
                        f"Available: {available_qty}, Required: {rec.quantity}")
                # self.move_id._update_shelf_quantities_sales(rec.quantity)
                shelfs_in_product = self.env["product.shelf"].search([("product_tmpl_id", "=", self.product_tmpl_id.id)])
                if rec.quantity :
                        exit_shelf = shelfs_in_product.search([("shelf_id", "=", rec.shelf_id.id)])
                        if exit_shelf.quantity >= rec.quantity:
                            exit_shelf.quantity -= rec.quantity * uom_factor


            if self.move_id.picking_id.picking_type_code == 'incoming' and self.shelf_lines or self.move_id.picking_id.picking_type_code == 'incoming' and self.move_id.picking_id.return_id:
                # self.move_id._update_shelf_quantities_purchase(rec.quantity)
                shelfs_in_product = self.env["product.shelf"].search(
                    [("product_tmpl_id", "=", self.product_tmpl_id.id)])
                if rec.shelf_id.id in shelfs_in_product.shelf_id.ids:
                    exit_shelf = shelfs_in_product.search([("shelf_id", "=", rec.shelf_id.id)])
                    exit_shelf.write({"quantity": exit_shelf.quantity + rec.quantity * uom_factor})
                else:
                    self.env["product.shelf"].create(
                        {
                            "product_tmpl_id": self.product_tmpl_id.id,
                            "quantity": rec.quantity * uom_factor,
                            "shelf_id": rec.shelf_id.id,
                        })


class shelf_wizard_detail(models.TransientModel):
    _name = "shelf.wizard.detail"

    shelf_id = fields.Many2one("shelf", string="Shelf Name")
    quantity = fields.Float(string="Quantity")
    master_id = fields.Many2one("shelf.wizard.master")
