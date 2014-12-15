from Template import Template
from tools import toggle_card_recipient

class ToggleXmas (Template):

    def writeContent(self):
        form = self.request().fields()
        cid = form.get('cid')
        yr = form.get('yr')
        toggle_card_recipient(yr, cid)
        redir = 'Main#%s' % (form.get('bookmark'))
        self.response().sendRedirect(redir)
