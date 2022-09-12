from odoo import api, models,fields, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    ref = fields.Char(string='Ref')
    name = fields.Char(string='Name')
    dob = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    image = fields.Image(string='Image')
    father_name = fields.Char(string='Father name')
    partner_name = fields.Char(string='Partner name')
    marital_status = fields.Selection([('single', 'Single'), ('married', 'Married')], string='Marital Status')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    active = fields.Boolean(string='Active', default=True)



