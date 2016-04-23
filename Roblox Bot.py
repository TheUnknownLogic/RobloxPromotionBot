#Time to beam you up, scotty.
import json
import urllib
import urllib2
import cgi

arguments = cgi.FieldStorage()

def get(link):
    return json.loads(urllib2.urlopen(link).read())

def post(link, data):
    values = urllib.urlencode(data)
    request = urllib2.Request(link, values)
    return urllib2.urlopen(request).read()

def PromotePlayer(group, player, role): #Use IDs for group and player, not role
    post('http://api.roblox.com/login/v1', {username: 'Promotions_Bot', password: 'blue1224'})
    roles = get('http://www.roblox.com/api/groups/'+group+'/RoleSets')
    for role in roles:
        if role['Name'] == strRole:
            post('http://www.roblox.com/groups/api/change-member-rank?groupId='+group+'&newRoleSetId='+role['ID']+'&targetUserId='+player)
            
PromotePlayer(2664056, arguments[1], arguments[2])
