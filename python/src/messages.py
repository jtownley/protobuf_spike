from messages_pb2 import PrinterStatus, DripRecorded, SetDripCount, MoveToDripCount, SetCurrentHeight


class ProtoBuffableMessage(object):
    TYPE_ID = 0

    def get_bytes(self):
        raise NotImplementedError()

    @classmethod
    def from_bytes(cls, proto_bytes):
        raise NotImplementedError()


class PrinterStatusMessage(ProtoBuffableMessage):
    TYPE_ID = 51

    def __init__(self, targetHeightMicrometer, currentHeightMicrometer, waitingForNextLayerHeight, status):
        self._target_height_micrometer = targetHeightMicrometer
        self._current_height_micrometer = currentHeightMicrometer
        self._waiting_for_next_layer_height = waitingForNextLayerHeight
        self._status = status

    @property
    def target_height_micrometer():
        return self._target_height_micrometer

    @property
    def current_height_micrometer():
        return self._current_height_micrometer

    @property
    def waiting_for_next_layer_height():
        return self._waiting_for_next_layer_height

    @property
    def status():
        return self._status


    def get_bytes(self):
        encoded = PrinterStatus()
        encoded.targetHeightMicrometer = self._target_height_micrometer
        encoded.currentHeightMicrometer = self._current_height_micrometer
        encoded.waitingForNextLayerHeight = self._waiting_for_next_layer_height
        encoded.status = self._status

        if encoded.IsInitialized():
            return encoded.SerializeToString()
        else:
            raise Exception("Protobuf Message encoding incomplete")

    @classmethod
    def from_bytes(cls, proto_bytes):
        decoded = PrinterStatus()
        decoded.ParseFromString(proto_bytes)
        return cls(
            decoded.targetHeightMicrometer,
            decoded.currentHeightMicrometer,
            decoded.waitingForNextLayerHeight,
            decoded.status,
            )

    def __eq__(self, other):
        if (self.__class__ == other.__class__ and
                self._target_height_micrometer == other._target_height_micrometer and
                self._current_height_micrometer == other._current_height_micrometer and
                self._waiting_for_next_layer_height == other._waiting_for_next_layer_height and
                self._status == other._status
                ):
            return True
        else:
            return False

    def __repr__(self):
        return ("Target Height            : {}\n"
               "Current Height           : {}\n"
               "Waiting for next height  : {}\n"
               "Status                   : {}").format(
                self._target_height_micrometer,
                self._current_height_micrometer,
                self._waiting_for_next_layer_height,
                self._status)


class SetCurrentHeightMessage(ProtoBuffableMessage):
    TYPE_ID = 52

    def __init__(self, heightMicrometers):
        self._height_micrometers = heightMicrometers

    @property
    def drips(self):
        return self._height_micrometers

    def get_bytes(self):
        encoded = SetCurrentHeight()
        encoded.heightMicrometers = self._height_micrometers
        if encoded.IsInitialized():
            return encoded.SerializeToString()
        else:
            raise Exception("Protobuf Message encoding incomplete")

    @classmethod
    def from_bytes(cls, proto_bytes):
        decoded = SetCurrentHeight()
        decoded.ParseFromString(proto_bytes)
        return cls(decoded.heightMicrometers)

    def __eq__(self, other):
        if (self.__class__ == other.__class__ and
                self._height_micrometers == other._height_micrometers):
            return True
        else:
            return False

    def __repr__(self):
        return "HeightMicrometers={}".format(self._height_micrometers)

class DripRecordedMessage(ProtoBuffableMessage):
    TYPE_ID = 3

    def __init__(self, drips):
        self._drips = drips

    @property
    def drips(self):
        return self._drips

    def get_bytes(self):
        encoded = DripRecorded()
        encoded.drips = self._drips
        if encoded.IsInitialized():
            return encoded.SerializeToString()
        else:
            logger.error("Protobuf Message encoding incomplete. Did the spec change? Have you compiled your proto files?")
            raise Exception("Protobuf Message encoding incomplete")

    @classmethod
    def from_bytes(cls, proto_bytes):
        decoded = DripRecorded()
        decoded.ParseFromString(proto_bytes)
        return cls(decoded.drips)

    def __eq__(self, other):
        if (self.__class__ == other.__class__ and
                self._drips == other._drips):
            return True
        else:
            return False

    def __repr__(self):
        return "drips={}".format(self._drips)


class SetDripCountMessage(ProtoBuffableMessage):
    TYPE_ID = 4

    def __init__(self, drips):
        self._drips = drips

    @property
    def drips(self):
        return self._drips

    def get_bytes(self):
        encoded = SetDripCount()
        encoded.drips = self._drips
        if encoded.IsInitialized():
            return encoded.SerializeToString()
        else:
            logger.error("Protobuf Message encoding incomplete. Did the spec change? Have you compiled your proto files?")
            raise Exception("Protobuf Message encoding incomplete")

    @classmethod
    def from_bytes(cls, proto_bytes):
        decoded = SetDripCount()
        decoded.ParseFromString(proto_bytes)
        return cls(decoded.drips)

    def __eq__(self, other):
        if (self.__class__ == other.__class__ and
                self._drips == other._drips):
            return True
        else:
            return False

    def __repr__(self):
        return "drips={}".format(self._drips)


class MoveToDripCountMessage(ProtoBuffableMessage):
    TYPE_ID = 5

    def __init__(self, drips):
        self._drips = drips

    @property
    def drips(self):
        return self._drips

    def get_bytes(self):
        encoded = MoveToDripCount()
        encoded.drips = self._drips
        if encoded.IsInitialized():
            return encoded.SerializeToString()
        else:
            logger.error("Protobuf Message encoding incomplete. Did the spec change? Have you compiled your proto files?")
            raise Exception("Protobuf Message encoding incomplete")

    @classmethod
    def from_bytes(cls, proto_bytes):
        decoded = MoveToDripCount()
        decoded.ParseFromString(proto_bytes)
        return cls(decoded.drips)

    def __eq__(self, other):
        if (self.__class__ == other.__class__ and
                self._drips == other._drips):
            return True
        else:
            return False

    def __repr__(self):
        return "drips={}".format(self._drips)
