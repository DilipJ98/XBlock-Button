"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from random import random
import math

class ButtonXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf-8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context = None):
        html = self.resource_string("static/html/firstbutton.html")
        frag = Fragment(html.format(self = self))
        frag.add_css(self.resource_string("static/css/firstbutton.css"))
        frag.add_javascript(self.resource_string("static/js/src/firstbutton.js"))
        frag.initialize_js('ButtonXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def random_generator(self, data, suffix = ''):
        random_number = random() * 100
        final_num  = math.floor(random_number)
        return {"count" : final_num }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ButtonXBlock",
             """<firstbutton/>
             """),
            ("Multiple ButtonXBlock",
             """<vertical_demo>
                <firstbutton/>
                <firstbutton/>
                <firstbutton/>
                </vertical_demo>
             """),
        ]
