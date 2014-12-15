from Template import Template
from tools import CDIR, readPick, get_mod
import glob, string, os.path

class Main(Template):

    def navLets(self, snls):
        l = ''
        for char in string.ascii_uppercase:
            if char in snls:
                l = l + '<span class="let"><a href="#%s">%s</a></span>' % (char, char)
            else:
                l = l + '<span class="let">%s</span>' % (char)
        return l

    def writeContent(self):
        wr = self.writeln
        recs = glob.glob(os.path.join(CDIR,'*'))
        foundLetters = []
        currentLetter = ''
        contacts = {}
        for record in recs:
            pick = readPick(record)
            name = '%s, %s' % (pick.get('sn'), pick.get('fn'))
            contacts[name] = pick
        sns = contacts.keys()
        sns.sort()

        snls = []
        for surname in sns:
            snl = surname[0]
            if snl not in snls:
                snls.append(snl)
        activelets = self.navLets(snls)

        for surname in sns:
            pick, snl = contacts.get(surname), surname[0]
            if snl != currentLetter:
                wr('<div class="lets" colspan="2">%s</div>' % (activelets))
            if snl not in foundLetters:
                foundLetters.append(snl)
                currentLetter = snl
                self.writeln('<a name="%s"></a><h2>%s</h2>' % (snl, snl))
            wr('<div style="float:right;font-size:9pt;color:#999;">Updated: ')
            wr(get_mod(pick.get('cid')))
            wr('</div>')
            wr('<div style="margin-bottom: 0.75em;"><a href="View?cid=%s">%s, %s</a></div>' % (pick.get('cid'), pick.get('sn'), pick.get('fn')))


