from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
        {
                "label": _("stpl_1"),
                "icon": "octicon octicon-briefcase",
                "items": [
                {
                        "type": "doctype",
                        "name": "First Doctype",
                        "label": _("First Doctype"),
                }
                {       "type": "doctype",
                        "name": "Retail Sales Order",
                        "label": _("Retail Sales Order"),
                },
                ]
        }
]

