from Template import Template
from tools import CDIR
import os

class DoDel(Template):

    def writeContent(self):
        cid = self.request().fields().get('cid')
        os.unlink(os.path.join(CDIR, cid))
        redir = 'Main'
        self.response().sendRedirect(redir)
