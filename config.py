"""
config.py
"""

import json
from os                  import makedirs
from pathlib             import Path
from singleton_decorator import singleton


class NetworkObject:
    """Interface for network objects"""

    def __init__(self, *, host: str, port: int, api: str) -> None:
        self.host : str = host
        self.port : int = port
        self.api  : str = api

    def to_dict(self) -> dict:
        """Returns dict representation of network object"""
        return self.__dict__

class ServicePaths:
    """Interface for all file/dir paths that the service uses"""

    def __init__(self, *, mount: str, log_dir: str,
                 conf_file: str
                 ) -> None:
        self.mount      : Path = Path(mount)
        self.log_dir    : Path = Path(log_dir)
        self.conf_file  : Path = Path(conf_file)


    def to_dict(self) -> dict:
        """Returns dict representation of paths config"""
        d : dict = {}
        for k in self.__dict__:
            d[k] = str(self.__getattribute__(k))
        return d
        
@singleton
class Config:
    """Service config singleton"""

    FILENAME : str = 'config.json'

    def __init__(self) -> None:
        self.initialized : bool = False

    def to_dict(self) -> dict:
        """Returns dict representation of config"""
        return {
            'server': self.server.to_dict(),
            'paths': self.paths.to_dict()
        }

    def save(self) -> None:
        """Serializes to json and saves to configured path"""
        with open(self.paths.conf_file, 'w+') as file:
            file.write(json.dumps(self.to_dict(), indent=4, sort_keys=True))

    def mount_at_directory(self, mount: str) -> None:
        """Init instance on given data directory, reading given data from it or initiating it if no config file is found"""
        d : dict
        p : Path = Path(mount).joinpath(self.FILENAME)
        try:
            with open(p, 'r') as file:
                d = json.loads(file.read())
        except Exception as error:
            print(f'Could not initialize from {p} for the following reason: {error}')
            d = self._defaults(r'./data')
        # create from given dict and create necessary directories, then save conf
        self._init_from_dict(d)
        self._create_dirs()
        self.save()
        self.initialized = True

    def _create_dirs(self) -> None:
        """Creates all directories that don't exist"""
        if not self.paths.mount.is_dir(): makedirs(self.paths.mount.absolute())
        for k in self.paths.__dict__:
            v : Path = self.paths.__getattribute__(k)
            if not v.is_dir() and not v.suffix:
                makedirs(v.absolute())

    def _init_from_dict(self, conf: dict) -> None:
        """Set instance fields from given dict"""
        self.server : NetworkObject = NetworkObject(**conf['server'])
        self.paths = ServicePaths(**conf['paths'])

    def _defaults(self, mount: str) -> dict:
        """Default values if no config was found"""
        return {
            'server': {
                'host': '0.0.0.0',
                'port': 80,
                'api' : 'api.php'
            },
            'paths': {
                'mount': mount,
                'log_dir': mount + '/log/',
                'conf_file': mount + '/' + self.FILENAME,
            }
        }
