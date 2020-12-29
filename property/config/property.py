# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
    return [{
		"label": _("Document"),
				"items":[
                    {
                        "type":"doctype",
                        "name":"Bill Run",
                        "description":_("Bill Run")
                      },
                    {
                        "type":"doctype",
                        "name":"Other Charges",
                        "description":_("Other Charges")
                      },
                    {
                      "type":"doctype",
                      "name":"Meter Reading",
                      "description":_("Meter Reading")
                    },
                    {
                      "type":"doctype",
                      "name":"Unit",
                      "description":_("Unit")
                    },
                    {
                      "type":"doctype",
                      "name":"Unit Type",
                      "description":_("Unit Type")
                    },
                    {
                      "type":"doctype",
                      "name":"Charge",
                      "description":_("Charge")
                    },
                    {
                      "type":"doctype",
                      "name":"Bill Run Type",
                      "description":_("Bill Run Type")
                    },
                    {
                      "type":"doctype",
                      "name":"Bill Period",
                      "description":_("Bill Period")
                    },
                    {
                      "type":"doctype",
                      "name":"Main Meter",
                      "description":_("Main Meter")
                    }
                ]
    }
    ]