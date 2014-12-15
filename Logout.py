from Template import Template

class Logout (Template):
    def title(self):
        return 'Logging Out...'

    def writeContent(self):
        self.session().invalidate()
        self.response().sendRedirect('Login')