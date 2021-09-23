from __future__ import unicode_literals
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and
from frappe import throw, msgprint, _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
import requests , json

def ConnectToRepzo(self,method):
    doc = {
    "name": self.customer_name
    }
    url = "https://sv.api.repzo.me/client"
    headers = {
    "api-key": "62yjvw0y5TTtT8oDAeRxNKlHmqRT7J88eufk4rogGB0"
    }
    response = requests.request("POST", url, headers=headers, data=doc)
    # frappe.msgprint(response.text)
