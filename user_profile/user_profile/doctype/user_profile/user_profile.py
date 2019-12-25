# -*- coding: utf-8 -*-
# Copyright (c) 2019, NavdeepGhai and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint, getdate, flt, nowdate, month_diff
class UserProfile(Document):
	
        def validate(self):
                self.validate_experiences()

        def validate_experiences(self):
                if not self.experiences:
                        frappe.throw(_("Please enter the Experience Item"))

                self.total_years_of_experience  = 0
                from_date = min([d.from_date for d in self.experiences])
                to_date = max([d.to_date for d in self.experiences])
                self.total_years_of_experience =  month_diff(to_date, from_date)/12.0

                
