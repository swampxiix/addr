from Template import Template
from tools import get_all_contacts

class Archived (Template):

    def writeContent(self):
        wr = self.writeln
        contacts = get_all_contacts(archived=True)
        sns = contacts.keys()
        sns.sort()
        wr('<table>')
        for surname in sns:
            pick, snl = contacts.get(surname), surname[0]
            cid = pick.get('cid')

            wr('<tr>')
            wr('<td><a href="View?cid=%s&archived=true">%s, %s</a></td>' % (cid, pick.get('sn'), pick.get('fn')))

            wr('</tr>')

        wr('</table>')



