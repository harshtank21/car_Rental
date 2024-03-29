{
    "name": "Car Rental",
    'version': '16.0.1.0.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
School Management 
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base', 'mail', 'sale', 'contacts', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir_sequence_data.xml',
        'data/ir_cron_data.xml',
        'data/ir_actions_server_data.xml',
        'data/mail_template_data.xml',
        'report/sale_order_report.xml',
        'report/car_rental_test_template.xml',
        'report/car_rental_order_report_template.xml',
        'report/car_rental_car_managment_template.xml',
        'report/car_rental_order_report.xml',
        'report/customer_report.xml',
        'views/menu_views.xml',
        'views/car_web_template.xml',
        'views/offline_transaction_views.xml',
        'views/online_transaction_views.xml',
        'views/all_order_views.xml',
        'views/avd_orders_views.xml',
        'views/running_order_views.xml',
        'views/contect_car_views.xml',
        'views/driver_salary_views.xml',
        'views/customers_customers_views.xml',
        'views/cars_management_views.xml',
        'views/customer_invoices_views.xml',
        'views/inherit_template_data.xml',
        'views/cleaning_maintenance_views.xml',
        # 'views/cleaning_ticket_create_views.xml',
        'views/car_bills_views.xml',
        'views/controllers_car_temp.xml',
        'views/web_template.xml',
        'views/finance_views.xml',
        'views/res_config_settings_views.xml',
        'wizard/customer_wizard_views.xml',
        'wizard/warning_wizard_views.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'car_Rental/static/src/scss/car_rental.scss', ]},
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
