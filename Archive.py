from Template import Template
from tools import get_one_contact, archive_contact

class Archive (Template):

    def writeContent(self):
        wr = self.writeln
        cid = self.request().fields().get('cid')
        pick = get_one_contact(cid)
        name = '%s %s' % (pick.get('fn'), pick.get('sn'))


        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            archive_contact(cid)
            redir = 'Main'
            self.response().sendRedirect(redir)

        else:
            wr('<h2>Archive %s?</h2>' % (name))
            wr('<P>')
            wr('Are you sure you want to archive %s %s?' % (pick.get('fn'), pick.get('sn')))
            wr('</P>')
            wr('<P>')
            wr('<form method="POST" action="Archive">')
            wr('<input type="hidden" name="cid" value="%s">' % (cid))
            wr('<input type="submit" value="Yes, archive.">')
            wr('<input type="button" value="Cancel" onClick="history.go(-1)">')
            wr('</form>')
            wr('</P>')
