from Template import Template
from tools import get_all_contacts, get_xmas_by_year
import time

class Xmas (Template):

    def writeContent(self):
        wr = self.writeln
        showaddr = self.request().fields().get('showaddr', '')

        nowyr = time.localtime(time.time())[0]
        got_cards = get_xmas_by_year(nowyr) # list

        contacts = get_all_contacts()
        sns = contacts.keys()
        sns.sort()

        nolist, yeslist = [], []

        for surname in sns:
            pick = contacts.get(surname)
            if pick.get('xmas') == 'yes':
                cid = pick.get('cid')
                if cid in got_cards:
                    yeslist.append(surname)
                else:
                    nolist.append(surname)

        wr('<h1>Xmas Cards %s = %s Total</h1>' % ( nowyr, len(nolist)+len(yeslist) ))

        wr('<h2>%s Unsent: ' % (len(nolist)) )
        if showaddr:
            wr('<a href="Xmas">Hide Addresses</a>')
        else:
            wr('<a href="Xmas?showaddr=true">Show Addresses</a>')
        wr('</h2>')
        for surname in nolist:
            pick = contacts.get(surname)
            cid = pick.get('cid')
            wr('')
            if pick.get('xmas') == 'yes':
                if showaddr:
                    wr('<P>')
                    wr('%s' % (surname))
                    wr('<br>')
                    wr(pick.get('addr'))
                    wr('<br>')
                    wr('%s, %s %s' % (pick.get('city'), pick.get('state'), pick.get('zip')))
                    wr('</P><hr>')
                else:
                    wr('<P>')
                    wr('<a href="View?cid=%s">%s</a>' % (cid, surname))
                    wr('</P>')

        if not showaddr:
            wr('<h2>%s Sent</h2>' % (len(yeslist)) )

            for surname in yeslist:
                pick = contacts.get(surname)
                cid = pick.get('cid')
                wr('<P>')
                if pick.get('xmas') == 'yes':
                    wr(surname)

