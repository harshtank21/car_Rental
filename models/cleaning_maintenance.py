from odoo import models, fields, api


class CarBills(models.Model):
    _name = "cleaning.maintenance"
    _description = "Car Rental"

    washing = fields.Char(string="Name")
    phone = fields.Char(string="phone")
    type = fields.Selection([("car dry cleaning", "CAR DRY CLEANING"), ("CAR VACUUM cLEANING", "CAR VACUUM CLEANING"),
                             ("CAR wASHING", "CAR WASHING")], string="type")
    driver_name = fields.Char(string="driver_name")
    date = fields.Date(string="date")
    cost = fields.Integer(string="cost")
    name = fields.Selection(
        [("gajanan_motors", "Gajanan Motors"), ("auto_club_car_dettling_studio", "Auto Club Car Dettling Studio"),
         ("steer_well_auto", "Steer Well Auto")],
        string="washing")
    theday = fields.Integer(string="Date", compute="_compute_date", store=True)




    @api.depends("date")
    def _compute_date(self):
        for rec in self:
            if rec.date:
                rec.theday = rec.date.month