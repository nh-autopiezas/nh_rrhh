# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
import datetime
from datetime import timedelta

class hr_holidays(osv.osv):
	_inherit = "hr.holidays"

	def _get_duration_hours(self, cr, uid, ids, field_name, arg, context):
		res = {}
		for i in ids:
			holiday = self.browse(cr,uid,i)
			date_from = datetime.datetime.strptime(holiday.date_from, '%Y-%m-%d %H:%M:%S')
			date_to = datetime.datetime.strptime(holiday.date_to, '%Y-%m-%d %H:%M:%S')
			res[i] = (date_to - date_from).total_seconds() / 3600
		        # res[i] = False
			# date_to - date_from
		return res
	

	_columns = {
		'holiday_duration_hours': fields.function(_get_duration_hours,string='Horas Ausencia', 
                            help="Horas de ausencia"),
	}

hr_holidays()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
