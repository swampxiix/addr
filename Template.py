from WebKit.Page import Page
from tools import is_logged_in, get_all_contacts
import string

class Template (Page):

    def writeStyleSheet (self):
        self.writeln('<link rel="stylesheet" href="./default.css" type="text/css">')
        self.writeln('<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">')

    def title (self):
        return 'Address Book'

    def navLets(self, snls):
        l = ''
        for char in string.ascii_uppercase:
            if char in snls:
                l = l + '<span class="let"><a href="./Main#%s">%s</a></span>' % (char, char)
            else:
                l = l + '<span class="let gray">%s</span>' % (char)
        return l

    def writeBodyParts(self):
        wr = self.writeln
        if is_logged_in(self.session()):
            wr('<div id="header">')
            wr('<span class="button"><a href="Main" title="Address Book"><i class="fa fa-home"></i></a></span>')
            wr('<span class="button"><a href="Form" title="Add New Contact"><i class="fa fa-plus"></i><i class="fa fa-user"></i></a></span>')
            wr('<span class="button"><a href="Xmas" title="Xmas Lists"><i class="fa fa-tree"></i></a></span>')

            contacts = get_all_contacts()
            sns = contacts.keys()
            sns.sort()
            snls = []
            for surname in sns:
                snl = surname[0]
                if snl not in snls:
                    snls.append(snl)
            activelets = self.navLets(snls)
            wr(activelets)

            wr('<span class="button"><a href="Archived" title="Archived"><i class="fa fa-archive"></i></a></span>')


            wr('<div class="flr"><span class="button"><a href="Logout" title="Log out"><i class="fa fa-sign-out"></i></a></span></div>')

            wr('</div>')

            wr('<div id="content">')
            self.writeContent()
            wr('</div>')
        else:
            self.response().sendRedirect('Login')

    def writeFooter(self):
        self.writeln('''
            </td></tr></table>
            ''')
        self.writeln('</html>')
