import cPickle, os.path, sha, time, glob, shutil

states = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',}
basedir = '/usr/local/wwrun/Addresses'
CDIR = os.path.join(basedir, 'contacts')
ARCH = os.path.join(basedir, 'archive')
XDIR = os.path.join(basedir, 'xmas')
AUTHFILE = os.path.join(basedir, 'users.auth')

def text(name, value='', size=25, max=40) :
    return '<input type="text" name="%s" value="%s" size="%s" maxlength="%s">' % (name, value, size, max)

def readPick(fullpath):
    try:
        file = open(fullpath, 'r')
        pick = cPickle.load(file)
        file.close()
        return pick
    except:
        return {}

def writePick(cid, dict):
    filename = os.path.join(CDIR, cid)
    file = open(filename, 'wb')
    cPickle.dump(dict, file)
    file.close()

def hashit(S):
    return sha.new(S).hexdigest()

def ismatch(name, pw):
    ud = readPick(AUTHFILE)
    upw = ud.get(name, '')
    return upw == hashit(pw)

def is_logged_in(sess):
    ok = False
    sd = sess.values()
    if sd.get('username') and sd.get('loggedin'):
        ok = True
    return ok

def get_mod(cid):
    fp = os.path.join(CDIR, cid)
    return time.strftime('%Y-%b-%d', time.localtime(os.path.getmtime(fp)))

def get_all_contacts(archived=False):
    recs = glob.glob(os.path.join(CDIR,'*'))
    if archived:
        recs = glob.glob(os.path.join(ARCH,'*'))
    contacts = {}
    for record in recs:
        pick = readPick(record)
        name = '%s, %s' % (pick.get('sn'), pick.get('fn'))
        contacts[name] = pick
    return contacts

def get_one_contact(cid, archived=False):
    fp = os.path.join(CDIR, cid)
    if archived:
        fp = os.path.join(ARCH, cid)
    return readPick(fp)

def archive_contact(cid):
    oldfile = os.path.join(CDIR, cid)
    newfile = os.path.join(ARCH, cid)
    shutil.move(oldfile, newfile)

######################################################
# Xmas List Stuff

def get_xmas_by_year (yr):
    yr = str(yr)
    yrfile = os.path.join(XDIR, yr)
    if os.path.exists(yrfile):
        return readPick(yrfile)
    else:
        return []

def toggle_card_recipient (yr, cid):
    year_list = get_xmas_by_year(yr)
    if cid in year_list:
        del year_list[year_list.index(cid)]
    else:
        year_list.append(cid)
    fn = os.path.join(XDIR, yr)
    file = open(fn, 'wb')
    cPickle.dump(year_list, file)
    file.close()



