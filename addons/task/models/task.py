from odoo import models, fields

class Task(models.Model):
    _name = 'project.task'
    _description = 'Task'

    name = fields.Char(string="Task Name")

    project_id = fields.Many2one('project.project', string="Project")
    employee_id = fields.Many2one('hr.employee', string="Employee")