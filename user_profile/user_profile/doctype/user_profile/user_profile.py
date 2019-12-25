# -*- coding: utf-8 -*-
# Copyright (c) 2019, NavdeepGhai and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint, cstr, getdate, flt, nowdate, month_diff

DATE_FORMAT = '%b/%Y'
class UserProfile(Document):

	def validate(self):
		self.profile_title = cstr(self.profile_title).upper()
		self.skill_title = cstr(self.skill_title).upper()
		self.employee_education_title =  cstr(self.employee_education_title).upper()
		self.validate_experiences()
		self.validate_employee_education()
		self.validate_skills()
		self.update_headline_for_experiences()

	# VALIDATE THE EXPERIENCE DATA
	def validate_experiences(self):
		if not self.experiences:
			frappe.throw(_("Please enter the Experience Item"))

		self.total_years_of_experience  = 0
		from_date = min([d.from_date for d in self.experiences])
		to_date = max([d.to_date for d in self.experiences])
		self.total_years_of_experience =  month_diff(to_date, from_date)/12.0

	# UPDATE AND HEADLING FROM EXPERIENCE FIELDS
	def update_headline_for_experiences(self):
		for exp in self.experiences:
			exp.headline = """{designation} at {company} from {from_date} to {to_date}
					""".format(
						designation=exp.designation,
						company=exp.company,
						from_date=getdate(exp.from_date).strftime(DATE_FORMAT),               
						to_date=getdate(exp.to_date).strftime(DATE_FORMAT))
	
	# VALIDATE EMPLOYEE EDUCATION
	def validate_employee_education(self):
		if not self.employee_education:
			return False
		for edu in self.employee_education:
			edu.qualification = cstr(edu.qualification).title()
			edu.school_univ = cstr(edu.school_univ).title()
	
	# VALIDATE THE SKILLS
	def validate_skills(self):
		if not self.skills:
			return False
		for skill in self.skills:
			skill.title = cstr(skill.title).title()	               
