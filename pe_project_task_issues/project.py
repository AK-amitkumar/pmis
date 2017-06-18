# -*- encoding: utf-8 -*-

from openerp import models, fields, api


class Task(models.Model):
    _inherit = 'project.task'

    issue_ids = fields.One2many(
        'project.issue', 'task_id', string="Issues")
    issue_id = fields.Many2one(
        'project.issue',
        string='Source Issue',
        compute='get_issue',
        store=True,
    )

    @api.one
    @api.depends('issue_ids')
    def get_issue(self):
        self.issue_id = self.issue_ids and self.issue_ids[0] or False
