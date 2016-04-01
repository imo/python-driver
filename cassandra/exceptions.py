class ConnectionException(Exception):
    """
    An unrecoverable error was hit when attempting to use a connection,
    or the connection was already closed or defunct.
    """

    def __init__(self, message, host=None):
        Exception.__init__(self, message)
        self.host = host


class ConnectionShutdown(ConnectionException):
    """
    Raised when a connection has been marked as defunct or has been closed.
    """
    pass


class ProtocolVersionUnsupported(ConnectionException):
    """
    Server rejected startup message due to unsupported protocol version
    """
    def __init__(self, host, startup_version):
        super(ProtocolVersionUnsupported, self).__init__("Unsupported protocol version on %s: %d",
                                                         (host, startup_version))
        self.startup_version = startup_version


class ConnectionBusy(Exception):
    """
    An attempt was made to send a message through a :class:`.Connection` that
    was already at the max number of in-flight operations.
    """
    pass


class ProtocolError(Exception):
    """
    Communication did not match the protocol that this driver expects.
    """
    pass

