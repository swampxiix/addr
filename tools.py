import cPickle, os.path, sha, time

states = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',}
basedir = '/usr/local/wwrun/Addresses'
CDIR = os.path.join(basedir, 'contacts')
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
