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

from gedcom.elements.element import Element
from gedcom.elements.object import ObjectElement
import gedcom.tags


def test_initialization():
    object_element = ObjectElement(level=-1, pointer="", tag=gedcom.tags.GEDCOM_TAG_OBJECT, value="")
    assert isinstance(object_element, Element)
    assert isinstance(object_element, ObjectElement)
