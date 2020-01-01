# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "user_profile"
app_title = "User Profile"
app_publisher = "NavdeepGhai"
app_description = "User Profile/Resume"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "navdeepghai1@gmail.com"
app_license = "MIT"


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/user_profile/css/user_profile.css"
# app_include_js = "/assets/user_profile/js/user_profile.js"

# include js, css files in header of web template
# web_include_css = "/assets/user_profile/css/user_profile.css"
# web_include_js = "/assets/user_profile/js/user_profile.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "user_profile.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "user_profile.install.before_install"
# after_install = "user_profile.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "user_profile.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"user_profile.tasks.all"
# 	],
# 	"daily": [
# 		"user_profile.tasks.daily"
# 	],
# 	"hourly": [
# 		"user_profile.tasks.hourly"
# 	],
# 	"weekly": [
# 		"user_profile.tasks.weekly"
# 	]
# 	"monthly": [
# 		"user_profile.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "user_profile.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "user_profile.event.get_events"
# }

