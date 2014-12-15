from Template import Template
from tools import get_one_contact

class Delete(Template):

    def writeContent(self):
        wr = self.writeln
        cid = self.request().fields().get('cid')
        pick = get_one_contact(cid)
        name = '%s %s' % (pick.get('fn'), pick.get('sn'))
        wr('<h2>Delete %s?</h2>' % (name))
        wr('<div style="margin-top: 12px;">')
        wr('Are you sure you want to delete %s %s ' % (pick.get('fn'), pick.get('sn')))
        if pick.get('guest'):
            wr('and %s ' % (pick.get('guest')))
        wr('from the address book?')
        wr('</div>')
        wr('<div style="margin-top: 12px;">')
        wr('''<input type="button" value="Yes, Delete" onClick="javascript:window.location.href='DoDel?cid=%s'">''' % (cid))
        wr('<input type="button" value="Cancel" onClick="history.go(-1)">')
        wr('</div>')
