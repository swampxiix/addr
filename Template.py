from WebKit.Page import Page
from tools import is_logged_in

class Template (Page):

    def writeStyleSheet (self):
        self.writeln('<link rel="stylesheet" href="./default.css" type="text/css">')

    def title (self):
        return 'Address Book'

    def writeBodyParts(self):
        if is_logged_in(self.session()):
            self.writeln('''
                <table align="center" width="800" border="0" cellspacing="0" cellpadding="0">
                <tr><td class="header">
                <span class="button"><a href="Main">%s</a></span>
                <span class="button"><a href="Form">Add New Contact</a></span>
                <span class="button"><a href="Logout">Log out</a></span>
                </td></tr>
                <tr valign="top"><td class="content">''' % (self.title()))
            self.writeContent()
        else:
            self.response().sendRedirect('Login')

    def writeFooter(self):
        self.writeln('''
            </td></tr></table>
            ''')
        self.writeln('</html>')
