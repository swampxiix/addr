from Template import Template
from tools import text, get_one_contact

class Form (Template):

    def writeContent(self):
        wr = self.writeln
        editMode = 0
        qs = self.request().fields()
        ######################################################
        # 'edit' in query string *must* also have 'cid'.
        if qs.get('edit', None) and qs.get('cid', None):
            editMode = 1
            cid = qs.get('cid')
            pick = get_one_contact(cid)

        a = 'Add'
        if editMode: a = 'Edit'
        wr('<h2>%s Contact</h2>' % (a))

        wr('<div>')
        wr('<form method="post" action="Handler">')
        wr('<table border="0">')
        if editMode:
            wr('<input type="hidden" name="cid" value="%s">' % (cid))

        ######################################################
        # Primary contact, first name, surname
        wr('<tr>')
        wr('<td>First Name:</td><td>')
        if editMode:
            wr(text('fn', pick.get('fn')))
        else:
            wr(text('fn'))
        wr('</td>')
        wr('</tr>')
        wr('<tr>')
        wr('<td>Last Name:</td><td>')
        if editMode:
            wr(text('sn', pick.get('sn')))
        else:
            wr(text('sn'))
        wr('</td>')
        wr('</tr>')

        ######################################################
        # Postal Address
        wr('<tr>')
        wr('<td>Street Addr.:</td><td>')
        if editMode:
            wr(text('addr', pick.get('addr'), '', 40))
        else:
            wr(text('addr', '', 40))
        wr('</td>')
        wr('</tr>')

        wr('<tr>')
        wr('<td>City, State, ZIP:</td><td>')
        if editMode:
            wr(text('city', pick.get('city'), '', 18))
        else:
            wr(text('city', '', 18))
        wr('&nbsp;')
        if editMode:
            wr(text('state', pick.get('state'), 2, 2))
        else:
            wr(text('state', '', 2, 2))
        wr('&nbsp;')
        if editMode:
            wr(text('zip', pick.get('zip'), 5, 5))
        else:
            wr(text('zip', '', 5, 5))
        wr('</td>')
        wr('</tr>')

        ######################################################
        # Phone & Email
        wr('<tr><td>Phone:</td><td>')
        if editMode:
            wr(text('phone', pick.get('phone', ''), 12))
        else:
            wr(text('phone'))
        wr('</td>')
        wr('</tr>')

        wr('<tr><td>Email:</td><td>')
        if editMode:
            wr(text('email', pick.get('email')))
        else:
            wr(text('email'))
        wr('</td>')
        wr('</tr>')

        ######################################################
        # Guest?
        wr('<tr><td>Husband/Wife:</td><td>')
        if editMode:
            wr(text('guest', pick.get('guest')))
        else:
            wr(text('guest'))
        wr('<small>(leave blank if none)</small>')
        wr('</td>')
        wr('</tr>')

        ######################################################
        # Xmas
        xmas = False
        if editMode:
            if pick.get('xmas') == 'yes':
                xmas = True
        wr('<tr><td>Send Xmas Card?</td><td>')
        wr('<label for="xy"><input type="radio" name="xmas" value="yes" id="xy"')
        if xmas:
            wr(' CHECKED')
        wr('> Yes</label>')
        wr('<label for="xn"><input type="radio" name="xmas" value="no" id="xn"')
        if not xmas:
            wr(' CHECKED')
        wr('> No</label>')

        ######################################################
        # Notes
        wr('<tr><td>Notes:</td><td>')
        wr('<textarea name="notes" cols="40" rows="5">')
        if editMode:
            wr(pick.get('notes'))
        wr('</textarea>')
        wr('</td>')
        wr('</tr>')

        ######################################################
        wr('<tr><td>&nbsp;</td><td>')
        wr('<input type="submit" value="Submit">')
        wr('<input type="button" value="Cancel" onClick="javascript:history.go(-1)">')
        wr('</td></tr>')
        wr('</table>')
        wr('</form>')
        wr('</div>')
