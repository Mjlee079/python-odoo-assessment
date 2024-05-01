from odoo import http
from odoo.http import request

class WebsiteController(http.Controller):
    @http.route('/custom_website/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('custom_website.index', {})
