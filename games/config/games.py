from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
            {
                "label": _("Games"),
                "icon": "octicon octicon-briefcase",                
                "items": [
                    {
                        "type": "doctype",
                        "name": "Game",
                        "label": "Game"
                    } 
                    ]
                }
            ]
