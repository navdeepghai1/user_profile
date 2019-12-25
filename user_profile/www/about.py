# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
import urllib.parse as urlparse
from urllib.parse import parse_qs

no_cache=True

def get_context(context):
        flag = False
        context.doc = frappe.get_doc("About Us Settings", "About Us Settings")
        parsed = parse_qs(urlparse.urlparse(frappe.local.request.url).query)
        if (parsed.get("user") and isinstance(parsed.get("user"), list)
                                    and len(parsed.get("user")) > 0):
                user = parsed.get("user")[0]
                if frappe.db.exists("User Profile", user):
                        context.user_profile = frappe.get_doc("User Profile", user)
                        flag = True
        if not flag:
                frappe.local.flags.redirect_location = "/login"
                raise frappe.Redirect 
        return context
