#https://wiki.selfhtml.org/wiki/HTTP/Anfragemethoden
import requests
import json
from pathlib        import Path
from config         import Config


def network() -> dict:
    """Declares where API is hosted"""
    return {'host': Config().server.host , 'port': Config().server.port, 'api' : Config().server.api}

def base_url(network: dict) -> str:
    """Returns base URL of API"""
    return f'http://{network["host"]}:{network["port"]}/{network["api"]}'


class Client_Exception(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__('Client API: ' + message)


    
class RestClient: 
    def __init__(self):
        self.base_url: str = base_url(network())
    def Members(self) -> None:
        try:
            res = requests.get(self.base_url + '/records/members/')  #GET
        except:
            raise Client_Exception('Members Network Fail')
        js = json.loads(res.text)
        json_formatted_str = json.dumps(js, indent=4)
        print(js)
        print(json_formatted_str)

    def CreateMember(self, Name : str, Vorname : str):
        adict =  {'nachname': Name, 'vorname': Vorname}
        print(adict)
        try:
            res = requests.post(self.base_url + '/records/members', json=adict)  #POST
        except:
            raise Client_Exception('CreateMember Network Fail')
        assert res.status_code == 200
    def DeleteMember(self, ident : int):
        try:
            res = requests.delete(self.base_url + '/records/members/' + str(ident))  #POST
        except:
            Client_Exception('DeleteMember Network Fail')
        assert res.status_code == 200

if __name__ == '__main__':
    p : Path = Path('./data') #p : Path = Path('./data')
    if not p.is_dir():
        print(f'{p.absolute()} is not a directory')
        sys.exit()
    # get config
    Config().mount_at_directory(p.absolute())

        
    client = RestClient()
    #client.CreateMember('Max', 'Mustermann')
    #client.DeleteMember(3)
            
    client.Members()


