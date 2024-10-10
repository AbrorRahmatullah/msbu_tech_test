from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PemesananRuangan(models.Model):
    _name = 'room.booking'
    _description = 'Pemesanan Ruangan'

    booking_number = fields.Char(string="Nomor Pemesanan", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    room_id = fields.Many2one('room.master', string="Ruangan", required=True)
    booking_name = fields.Char(string="Nama Pemesanan", required=True)
    booking_date = fields.Datetime(string="Tanggal Pemesanan", required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')], string="Status Pemesanan", default='draft')
    booking_notes = fields.Text(string="Catatan Pemesanan")

    @api.model
    def create(self, vals):
        if vals.get('booking_number', _('New')) == _('New'):
            vals['booking_number'] = self.env['ir.sequence'].next_by_code('room.booking') or _('New')
        return super(PemesananRuangan, self).create(vals)

    @api.constrains('room_id', 'booking_date')
    def _check_duplicate_booking(self):
        for rec in self:
            existing_booking = self.search([
                ('room_id', '=', rec.room_id.id),
                ('booking_date', '=', rec.booking_date),
                ('id', '!=', rec.id)
            ])
            if existing_booking:
                raise ValidationError("Ruangan ini sudah dipesan untuk tanggal tersebut.")

    _sql_constraints = [
        ('booking_name_unique', 'unique(booking_name)', 'Nama pemesanan sudah ada!'),
    ]
