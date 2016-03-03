import urllib

class Contribute:
    def GET(self):
        github = 'https://api.github.com/orgs/TetrahedronSolutions/members'
        return urllib.urlopen(github)
