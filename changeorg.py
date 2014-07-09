import requests


class Client():
    def __init__(self,api_key=None, api_secret=None,api="http://api.change.org/v1/"):
        self.api_key=api_key
        self.api_secret=api_secret
        self.api=api


    def getRequest(self,resource,params=[]):
        """ issue a simple get request.
            getRequest('/petitions/get_id',[('url','http://...')])
            """

        params += [('api_key',self.api_key)]
        params="&".join(map(lambda x: "%s=%s"%x, params))
        print params
        r = requests.get("%s/%s?%s"%(self.api,resource,params))
        if r.status_code == 200:
            return r.json()
        else:
            # proper error handling needed
            return r.json()

    def get_petition_id(self,url=None):
        """ gets the id for a petition from the change.org url """
        r = self.getRequest('petitions/get_id',[('petition_url',url)])
        if r['result'] == 'success':
            return r['petition_id']
        else:
            return r['messages']

    def get_petition(self,id=None):
        """ gets petition data for a petition with id"""
        return self.getRequest('petitions/%s'%id)

    def get_petitions(self,ids=[]):
        "gets petition data for petitions with the ids"""
        ids = ",".join(ids)
        return self.getRequest('petitions/',[('petition_ids',ids)])
