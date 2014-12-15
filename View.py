from Template import Template
from tools import readPick, CDIR, get_mod
import os.path

class View(Template):

    def writeContent(self):
        wr = self.writeln
        cid = self.request().fields().get('cid')
        wr('<div style="float:right;font-size:9pt;color:#999;">Updated: ')
        wr(get_mod(cid))
        wr('</div>')
        pick = readPick(os.path.join(CDIR, cid))
        lastfirst = '%s %s' % (pick.get('fn'), pick.get('sn'))
        wr('<div style="margin-top: 12px;">')
        wr('%s' % (lastfirst))
        if pick.get('guest'):
            wr(' &amp; %s' % (pick.get('guest')))
        wr('<br />')
        wr('%s<br />' % (pick.get('addr')))
        wr('%s, %s %s' % (pick.get('city'), pick.get('state'), pick.get('zip')))
        if pick.get('phone'):
            wr('<br />%s' % (pick.get('phone')))
        wr('</div>')
        wr('<div style="margin-top: 12px;">')
        wr('<a href="mailto:%s">%s</a>' % (pick.get('email'), pick.get('email')))
        wr('</div>')
#        if pick.get('notes'):
#            wr('<div style="margin-top: 12px;">')
#            wr(pick.get('notes'))
#            wr('</div>')
        wr('<div class="botnav">')
        wr('<a href="Form?edit=1&cid=%s">edit</a> &middot; <a href="Delete?cid=%s">delete</a>' % (cid, cid))
        wr('</div>')

