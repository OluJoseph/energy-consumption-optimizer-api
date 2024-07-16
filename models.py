import enum
import datetime as dt

from extensions import db


class DevicesEnum(enum.Enum):
    AIRCONDITIONER = 'air conditioner'
    WATERHEATER = 'water heater'
    DECODER = 'decoder'
    SMARTTV = 'Smart Television'
    COFFEEMAKER = 'coffee maker'
    FRIDGE = 'fridge'
    WASHER = 'washer'


class DevicesGraph:
    _devices = [
        (DevicesEnum.AIRCONDITIONER, DevicesEnum.FRIDGE),
        (DevicesEnum.WATERHEATER, DevicesEnum.WASHER),
        (DevicesEnum.WATERHEATER, DevicesEnum.COFFEEMAKER),
        (DevicesEnum.DECODER, DevicesEnum.SMARTTV)
    ]

    def buildGraph():
        """
            Builds a directed graph from <class DevicesGraph>._devices tuple 'list'
            to represent the co-dependence between devices in a smart home.
        """
        graph = {}
        for x, y in DevicesGraph._devices:
            if x not in graph:
                graph[x] = [y]
            graph[x].append(y)
        return graph

    def __init__(self):
        self.graph = DevicesGraph.buildGraph()


class IdMixin(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)


class PowerUsage(IdMixin):
    date = db.Column(db.Date, default=dt.datetime.utcnow())
    device_id = db.Column(db.Integer, db.ForeignKey('Devices.id'))
    power_usage = db.Column(db.Float)

    def power_usage():
        pass


class Devices(IdMixin):
    device_name = db.Column(db.Enum(DevicesEnum))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    power_usage_data = db.relationship('PowerUsage', backref='device')


class User(IdMixin):
    name = db.Column(db.String)
    devices = db.relationship('Devices', backref='user')
