{
    'name': 'Room Booking Module',
    'version': '1.0',
    'category': 'Management',
    'summary': 'Module for managing room bookings',
    'description': """
        This module allows users to manage room bookings, including room details and reservations.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/master_ruangan_views.xml',
        'views/pemesanan_ruangan_views.xml',
    ],
    'installable': True,
    'application': True,
}
