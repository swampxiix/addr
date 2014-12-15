from Template import Template
from tools import get_mod, get_one_contact

class View(Template):

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        cid = qs.get('cid')
        from_archive = qs.get('archived')

        if from_archive:
            pick = get_one_contact(cid, archived=True)
        else:
            pick = get_one_contact(cid)
        

        lastfirst = '%s %s' % (pick.get('fn'), pick.get('sn'))

        wr('<P><b>')
        wr('%s' % (lastfirst))
        if pick.get('guest'):
            wr(' &amp; %s' % (pick.get('guest')))
        wr('</b>')
        wr('&nbsp;&nbsp;<a href="./Form?edit=1&cid=%s"><i class="gray fa fa-pencil" title="Edit"></i></a>' % (cid))
        wr('&nbsp;&nbsp;<a href="./Archive?cid=%s"><i class="gray fa fa-archive" title="Archive"></i></a>' % (cid))
        wr('&nbsp;&nbsp;<a href="./Delete?cid=%s"><i class="gray fa fa-remove" title="Delete"></i></a>' % (cid))

        wr('<br />')
        wr('%s<br />' % (pick.get('addr')))
        wr('%s, %s %s' % (pick.get('city'), pick.get('state'), pick.get('zip')))
        if pick.get('phone'):
            wr('<br />%s' % (pick.get('phone')))
        wr('</P>')

        if pick.get('xmas') == 'yes':
            wr('<P><i class="gray fa fa-tree"></i> Supposed to get Xmas card.</P>')


        wr('<P>')
        wr('Email: <a href="mailto:%s">%s</a>' % (pick.get('email'), pick.get('email')))
        wr('</P>')

        if pick.get('notes'):
            wr('<P>')
            wr(pick.get('notes'))
            wr('</P>')

        if not from_archive:
            wr('<P>Updated: %s</P>' % (get_mod(cid)))
