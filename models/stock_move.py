from odoo import models, fields, _,api

class stock_move(models.Model):
    _inherit = "stock.move"
    ##########################################################################################
    # sale_shelf_ids = fields.Many2many(
    #     "shelf", 
    #     "stock_move_sale_shelf_rel",  # Unique relation table name
    #     "move_id",                    # Column for stock.move id
    #     "shelf_id",                   # Column for shelf id
    #     string="Shelves"
    # )
    
    # purchase_shelf_ids = fields.Many2many(
    #     "shelf", 
    #     "stock_move_purchase_shelf_rel",  # Unique relation table name
    #     "move_id",                        # Column for stock.move id
    #     "shelf_id",                       # Column for shelf id
    #     string="Shelves",   
    # )

    # def _update_shelf_quantities_sales(self,quantity):
    #     for line in self:
    #         if line.shelf_ids and line.product_id:
    #             uom_factor = self.get_uom_factor(line.product_uom)
    #             for shelf in line.shelf_ids:
    #                 shelf_record = self.env['product.shelf'].search([
    #                     ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id),
    #                     ('shelf_id', '=', shelf.id)
    #                 ], limit=1)
    #                 if shelf_record and shelf_record.quantity >= quantity:
    #                     shelf_record.quantity -= quantity * uom_factor
                        

    # def _update_shelf_quantities_purchase(self,quantity):
    #     for line in self:
    #         if line.shelf_ids and line.product_id:
    #             uom_factor = self.get_uom_factor(line.product_uom)
               
    #             for shelf in line.shelf_ids:
                    
    #                 shelf_record = self.env['product.shelf'].search([
    #                     ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id),
    #                     ('shelf_id', '=', shelf.id)
    #                 ], limit=1)

    #                 if shelf_record:
    #                     shelf_record.quantity += quantity * uom_factor

    #                 else:
    #                     self.env['product.shelf'].create({
    #                         'product_tmpl_id': line.product_id.product_tmpl_id.id,
    #                         'shelf_id': shelf.id,
    #                         'quantity': quantity * uom_factor
    #                     })


    # is_from_sale_purchase = fields.Boolean(
    #     compute='_compute_readonly_feilds',
    #     store=False)
    
    # def _compute_readonly_feilds(self):
    #     """Method to determine if fields should be readonly"""
    #     for record in self:
    #         if record.sale_line_id:
    #             record.is_from_sale_purchase = True
    #         elif record.purchase_line_id:
    #             record.is_from_sale_purchase = True
    #         elif record.picking_id.return_id:
    #              record.is_from_sale_purchase = True
    #         else:
    #             record.is_from_sale_purchase = False
                
    # shelf_ids_domain = fields.Char("shelf_ids_domain", compute="_get_shelf_domain")

    # @api.depends('product_id')
    # def _get_shelf_domain(self):
    #     for record in self:
    #         if record.product_id and record.product_id.product_tmpl_id.product_shelf_ids:
    #             shelf_ids = record.product_id.product_tmpl_id.product_shelf_ids.shelf_id.ids
    #             record.shelf_ids_domain = [('id', 'in', shelf_ids)]
    #         else:
    #             record.shelf_ids_domain = [('id', '=', False)]

    
    # def _update_shelf_quantities_sale_refund(self):
    #     for move in self:
    #         origin_move = move.origin_returned_move_id
    #         if origin_move and origin_move.sale_shelf_ids:
    #             product_tmpl = move.product_id.product_tmpl_id
    #             uom_factor = self.get_uom_factor(move.product_uom)

    #             for shelf in origin_move.sale_shelf_ids:
    #                 shelf_record = self.env['product.shelf'].search([
    #                     ('product_tmpl_id', '=', product_tmpl.id),
    #                     ('shelf_id', '=', shelf.id)
    #                 ], limit=1)
                    
    #                 if shelf_record:
    #                     shelf_record.quantity += move.quantity * uom_factor
    #                 else:
    #                     self.env['product.shelf'].create({
    #                         'product_tmpl_id': move.product_tmpl_id.id,
    #                         'shelf_id': shelf.id,
    #                         'quantity': move.quantity * uom_factor
    #                     })
                        

    # def _update_shelf_quantities_purchase_refund(self):
    #     for move in self:
    #         origin_move = move.origin_returned_move_id
    #         if origin_move and origin_move.purchase_shelf_ids:
    #             product_tmpl = move.product_id.product_tmpl_id
    #             uom_factor = self.get_uom_factor(move.product_uom)

    #             for shelf in origin_move.purchase_shelf_ids:
    #                 shelf_record = self.env['product.shelf'].search([
    #                     ('product_tmpl_id', '=', product_tmpl.id),
    #                     ('shelf_id', '=', shelf.id)
    #                 ], limit=1)
                    
    #                 if shelf_record and shelf_record.quantity >= move.quantity:
    #                     shelf_record.quantity -= move.quantity * uom_factor
                        
    #############################################################################                    

    def get_uom_factor(self,product_uom):
        uom_factor = 0
        if product_uom.uom_type == "bigger":
            uom_factor = product_uom.factor_inv
        elif product_uom.uom_type == "smaller":
            uom_factor = 1 / product_uom.factor
        elif product_uom.uom_type == "reference":
            uom_factor = product_uom.factor
        
        return uom_factor
                    
                                       
    def get_shelves(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Shelves",
            "view_mode": "form",
            "view_type": "form",
            "res_model": "shelf.wizard.master",
            "target": "new",
            "domain": "",
            "context": {
                "default_product_tmpl_id": self.product_id.product_tmpl_id.id,
                "default_move_id": self.id,
            },
        }
        
        
    def _get_available_shelf_quantity(self, product, shelves):
            """Get total available quantity for product in selected shelves"""
            shelf_records = self.env['product.shelf'].search([
                ('product_tmpl_id', '=', product.id),
                ('shelf_id', 'in', shelves.ids)
            ])
            return sum(shelf_records.mapped('quantity'))
            
    
    

# class StockPicking(models.Model):
#     _inherit = "stock.picking"

#     def button_validate(self):
#         res = super().button_validate()
#         for picking in self.move_ids:
#             return picking.get_shelves()
            
#         return res
