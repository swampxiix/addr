from Template import Template
from tools import get_mod, get_all_contacts, get_xmas_by_year
import time

class Main (Template):

    def writeContent(self):

        nowyr = time.localtime(time.time())[0]
        got_cards = get_xmas_by_year(nowyr) # list

        wr = self.writeln
        foundLetters = []
        currentLetter = ''
        contacts = get_all_contacts()
        sns = contacts.keys()
        sns.sort()
        wr('<table>')
        for surname in sns:
            pick, snl = contacts.get(surname), surname[0]
            cid = pick.get('cid')
            if snl not in foundLetters:
                foundLetters.append(snl)
                currentLetter = snl
                self.writeln('<tr><td colspan="3" style="padding: 0px;"><a name="%s"></a><h2>%s</h2></td></tr>' % (snl, snl))
            moddate = get_mod(cid)
            modyr = int(moddate.split('-')[0])
            if modyr == nowyr: # updated this year
                cls = 'green'
            elif (nowyr - modyr) < 2: # less than 2 years old
                cls = 'gray'
            elif (nowyr - modyr) > 6: # more than 6 years old
                cls = 'red'
            else:
                cls = 'orange' # between 2-6 years old

            wr('<tr>')
            wr('<td><a href="View?cid=%s">%s, %s</a></td>' % (cid, pick.get('sn'), pick.get('fn')))
            wr('<td>')

            if pick.get('xmas') == 'yes':
                if cid in got_cards:
                    wr('<a href="ToggleXmas?cid=%s&yr=%s&bookmark=%s" title="Card Sent. Click to change."><i class="green fa fa-tree"></i></a>' % (cid, nowyr, currentLetter))
                else:
                    wr('<a href="ToggleXmas?cid=%s&yr=%s&bookmark=%s" title="Not Sent. Click to change."><i class="red fa fa-tree"></i></a>' % (cid, nowyr, currentLetter))

            wr('</td>')
            wr('<td><i class="%s fa fa-clock-o" title="%s"></i></td>' % (cls, moddate))
            wr('<td><a href="./Form?edit=1&cid=%s"><i class="gray fa fa-pencil" title="Edit"></i></a></td>' % (cid))

            wr('</tr>')

        wr('</table>')



