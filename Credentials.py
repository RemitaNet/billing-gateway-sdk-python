class Credentials:

    public_key: str
    secret_key: str
    environment: str
    read_timeout: int
    connection_timeout: int

    def __init__(self, public_key: str, secret_key: str, environment: str, read_timeout: int, connection_timeout: int) -> None:
        self.public_key = public_key
        self.secret_key = secret_key
        self.environment = environment
        self.read_timeout = read_timeout
        self.connection_timeout = connection_timeout

    # @property
    # def public_key(self):
    #     return self.__public_key
    #
    # @public_key.setter
    # def public_key(self, value):
    #     self.__public_key = value
    #
    # @property
    # def secret_key(self):
    #     return self.__secret_key
    #
    # @secret_key.setter
    # def secret_key(self, value):
    #     self.__secret_key = value
    #
    # @property
    # def environment(self):
    #     return self.__environment
    #
    # @environment.setter
    # def environment(self, value):
    #     self.__environment = value
    #
    # @property
    # def read_timeout(self):
    #     return self.__read_timeout
    #
    # @read_timeout.setter
    # def read_timeout(self, value):
    #     self.__read_timeout = value
    #
    # @property
    # def connection_timeout(self):
    #     return self.__connection_timeout
    #
    # @connection_timeout.setter
    # def connection_timeout(self, value):
    #     self.__connection_timeout = value
