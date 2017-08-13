from six.moves import http_client

# Tests use this to make exception message format errors fatal
_FATAL_EXCEPTION_FORMAT_ERRORS = False


def _format_with_unicode_kwargs(msg_format, kwargs):
    return msg_format % kwargs


class Error(Exception):
    """Base error class.

    Child classes should define an HTTP status code, title, and a
    message_format.

    """

    code = None
    title = None
    message_format = None

    def __init__(self, message=None, **kwargs):
        try:
            message = self._build_message(message, **kwargs)
        except KeyError:
            # if you see this warning in your logs, please raise a bug report
            if _FATAL_EXCEPTION_FORMAT_ERRORS:
                raise
            else:
                message = self.message_format

        super(Error, self).__init__(message)

    def _build_message(self, message, **kwargs):
        """Build and returns an exception message.

        :raises KeyError: given insufficient kwargs

        """
        if message:
            return message
        return _format_with_unicode_kwargs(self.message_format, kwargs)


class NotFound(Error):
    message_format = "Could not find: %(target)s."
    code = int(http_client.NOT_FOUND)
    title = http_client.responses[http_client.NOT_FOUND]


class InternalError(Error):
    message_format = "Server internal error: %(target)s."
    code = int(http_client.INTERNAL_SERVER_ERROR)
    title = http_client.responses[http_client.INTERNAL_SERVER_ERROR]


class RequestError(Error):
    message_format = "Request error: %(target)s."
    code = int(http_client.BAD_REQUEST)
    title = http_client.responses[http_client.BAD_REQUEST]


class ClientError(Error):
    message_format = "Client error: %(target)s."
    code = int(http_client.OK)
    title = http_client.responses[http_client.OK]


class TokenNotFound(NotFound):
    message_format = "No token in the request."


class TokenNotValid(NotFound):
    message_format = "Token not valid."


class UserNotFound(NotFound):
    message_format = "User not found."


class ParameterNotValid(NotFound):
    message_format = "Wrong parameter in the request."


class CommitOJFailed(RequestError):
    message_format = "Commit OJ failed"
