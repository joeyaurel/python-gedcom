# -*- coding: utf-8 -*-

#  Copyright (C) 2020
#
#  This file is part of the Python GEDCOM Parser.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#  For more, have a look at the GitHub repository at:
#  https://github.com/nickreynke/python-gedcom
#
#  This file is part of the Python GEDCOM Parser.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#  For more, have a look at the GitHub repository at:
#  https://github.com/nickreynke/python-gedcom

"""
Substructure parser for a `ADDRESS_STRUCTURE` embedded record.

This is referenced as part of a larger structure so there is no anchor tag.
The `gedcom.tags.GEDCOM_TAG_ADDRESS` tag is at the same level as some of
the other parts of this structure.
"""

import gedcom.tags as tags
from gedcom.elements.element import Element

ADDRESS_TAGS = {
    tags.GEDCOM_PROGRAM_DEFINED_TAG_ADDRESSE: 'addresse',
    tags.GEDCOM_TAG_ADDRESS1: 'address1',
    tags.GEDCOM_TAG_ADDRESS2: 'address2',
    tags.GEDCOM_TAG_ADDRESS3: 'address3',
    tags.GEDCOM_TAG_CITY: 'city',
    tags.GEDCOM_TAG_STATE: 'state',
    tags.GEDCOM_TAG_POSTAL_CODE: 'postal_code',
    tags.GEDCOM_TAG_COUNTRY: 'country'
}

CONTACT_TAGS = {
    tags.GEDCOM_TAG_PHONE: 'phone',
    tags.GEDCOM_TAG_EMAIL: 'email',
    tags.GEDCOM_TAG_FAX: 'fax',
    tags.GEDCOM_TAG_WWW: 'www'
}


def parse_address_structure(element: Element) -> dict:
    """Parses and extracts a `ADDRESS_STRUCTURE` structure.

    The `element` should be the parent that contains it.
    """
    record = {
        'address': '',
        'addresse': '',
        'address1': '',
        'address2': '',
        'address3': '',
        'city': '',
        'state': '',
        'postal_code': '',
        'country': '',
        'phone': [],
        'email': [],
        'fax': [],
        'www': []
    }
    for child in element.get_child_elements():
        if child.get_tag() == tags.GEDCOM_TAG_ADDRESS:
            record['address'] = child.get_multi_line_value()
            for gchild in child.get_child_elements():
                if gchild.get_tag() in ADDRESS_TAGS:
                    record[ADDRESS_TAGS[gchild.get_tag()]] = gchild.get_value()
            continue

        if child.get_tag() in CONTACT_TAGS:
            record[CONTACT_TAGS[child.get_tag()]].append(child.get_value())

    return record
