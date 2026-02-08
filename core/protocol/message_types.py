# core/protocol/message_types.py

from enum import Enum

class MessageType(str, Enum):
    EXECUTE_REQUEST = "execute_request"
    EXECUTE_RESPONSE = "execute_response"
    STREAM_OUTPUT = "stream_output"
    ERROR = "error"
    STATUS = "status"
    INTERRUPT = "interrupt"
    RESTART = "restart"
