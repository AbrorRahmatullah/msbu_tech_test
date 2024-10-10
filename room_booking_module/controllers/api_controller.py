from odoo import http
from odoo.http import request

class RoomBookingController(http.Controller):

    @http.route('/api/room_booking/<int:booking_id>', auth='public', methods=['GET'], csrf=False)
    def get_booking_status(self, booking_id):
        booking = request.env['room.booking'].sudo().browse(booking_id)
        if not booking.exists():
            return {'error': 'Booking not found'}
        return {
            'booking_number': booking.booking_number,
            'status': booking.status
        }
