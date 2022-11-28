# -*- coding: utf-8 -*-
{
    'name': 'SW - Manual Currency Exchange Rate',
    'license':  "Other proprietary",
    'summary': """Manually set currency exchange rate on records.""",
    'description': """Grants users ability to manually set exchange rate on the following records.
                    Purchase Orders
                    Sale Orders
                    Invoices
                    Payments
                    """,
    'author': "Smart Way Business Solutions","Oloyede Femi",
    'website': "https://www.smartway.co",
    'category': 'Accounting',
    'version': '16.0.1.1',
    "depends" : ['base','account','purchase', 'sale', 'sale_management','stock', 'purchase_stock', 'sale_stock'],
    'data': [
            #"views/customer_invoice.xml",
            #"views/account_payment_view.xml",
            "views/purchase_view.xml",
            "views/sale_view.xml",
             ],
    'images':  ["static/description/image.png"],
}
