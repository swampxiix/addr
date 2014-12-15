from Template import Template
from tools import get_mod, get_all_contacts
import time

class Main(Template):

    def writeContent(self):
        wr = self.writeln
        foundLetters = []
        currentLetter = ''
        contacts = get_all_contacts()
        sns = contacts.keys()
        sns.sort()
        wr('<table>')
        for surname in sns:
            pick, snl = contacts.get(surname), surname[0]
            if snl not in foundLetters:
                foundLetters.append(snl)
                currentLetter = snl
                self.writeln('<tr><td colspan="3" style="padding: 0px;"><a name="%s"></a><h2>%s</h2></td></tr>' % (snl, snl))
            moddate = get_mod(pick.get('cid'))
            modyr = int(moddate.split('-')[0])
            nowyr = time.localtime(time.time())[0]
            if modyr == nowyr:
                cls = 'green'
            elif (nowyr - modyr) < 2:
                cls = 'orange'
            elif (nowyr - modyr) > 7:
                cls = 'red'
            else:
                cls = 'gray'

            wr('<tr>')
            wr('<td><a href="View?cid=%s">%s, %s</a></td>' % (pick.get('cid'), pick.get('sn'), pick.get('fn')))
            wr('<td>')
            if pick.get('xmas') == 'yes':
                wr('<i class="gray fa fa-tree" title="Xmas"></i>')
            wr('</td>')
            wr('<td><i class="%s fa fa-clock-o" title="%s"></i></td>' % (cls, moddate))
            wr('<td><a href="./Form?edit=1&cid=%s"><i class="gray fa fa-pencil" title="Edit"></i></a></td>' % (pick.get('cid')))

            wr('</tr>')

        wr('</table>')



