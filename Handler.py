from Template import Template
import random, string
from tools import writePick

class Handler(Template):

    def getID(self, fn, sn):
        r = random.randint(0, 999)
        rn = string.zfill(r, 3)
        id = fn[0] + sn + rn
        return id

    def writeContent(self):
        wr = self.writeln
        form = self.request().fields()
        failed = 0

        # Check Required
        reqd = {'fn': 'First Name', 'sn': 'Last Name'}
        for a in reqd.keys():
            if not form.get(a, None):
                failed = a

        if failed:
            wr('<div id="title">ERROR</div>')
            wr('<div>%s is required. <a href="javascript:history.go(-1)">Go back and try again</a>.</div>' % (reqd.get(failed)))
        else:
            if not form.get('cid'):
                action = 'Added'
                cid = self.getID(form.get('fn').lower(), form.get('sn').lower())
            else:
                action = 'Updated'
                cid = form.get('cid')
            form['cid'] = cid
            writePick(cid, form)
            fn, sn = form.get('fn'), form.get('sn')
            wr('<div id="title">%s %s %s\'s Record</div>' % (action, fn, sn))
            wr('<div>')
            wr('Here\'s the info:<br />')
            x = form.keys()
            x.sort()
            for key in x:
                wr('<b>%s</b>: %s<br />' % (key, form.get(key)))
            wr('</div>')
            redir = 'View?cid=%s' % (cid)
            self.response().sendRedirect(redir)



