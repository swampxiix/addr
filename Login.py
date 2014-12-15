from Template import Template
from tools import *
import glob, os
from tools import is_logged_in, ismatch

class Login (Template):

    def writeBodyParts(self):
        self.writeContent()

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            if ismatch(form.get('username'), form.get('password')):
                self.session().setValue('username', form.get('username'))
                self.session().setValue('loggedin', True)
                self.session().setTimeout(3600)
                self.response().sendRedirect('Main')
            else:
                wr('<h2>Nope.</h2>')
        else:
            if is_logged_in(self.session()):
                self.response().sendRedirect('Main')
            else:
                wr('<h2>Log In</h2>')
                wr('<form method="POST" action="Login">')
                wr('<P>')
                wr('Username:<br />')
                wr('<input type="text" name="username" value="">')
                wr('<P>')
                wr('Password:<br />')
                wr('<input type="password" name="password" value="">')
                wr('<P>')
                wr('<input type="submit" value="Log In">')
                wr('</form>')