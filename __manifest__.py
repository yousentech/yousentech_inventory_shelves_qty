{
    "name": "yousentech_inventory_shelves_qty",
    'version': '17.0.0.1',
    "category": "Inventory",
    "summary": """Enhancing inventory management by improving the handling of item shelve.""",
    "description": """This update focuses on optimizing the management of item shelves within the inventory system. 
                    It introduces features that facilitate better organization, tracking, and accessibility of items stored 
                    on shelves.""",
    'author': 'yousen tech Techno Solutions, Odoo SA',
    'website': "https://www.qimamhd.com",
    'company': 'yousen Techno Solutions',
    'maintainer': 'yousen Techno Solutions',
    'depends': ['base','purchase','sale','stock','yousentech_inventory_shelves'],
    'data': [   
        
          'security/ir.model.access.csv',
          # 'views/purchase_order.xml',
          # 'views/sale_order.xml',
          # 'views/res_config_settings.xml',
          # 'views/shelf.xml',
          'views/shelfs_wizard.xml',
          # 'views/sale_shelf_wizard.xml',
          'views/product_template.xml',
          'views/stock_move.xml'
          
         ],
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    'sequence':'-100',
    'installable': True,
    'auto_install': False,
    'application': True,
}
