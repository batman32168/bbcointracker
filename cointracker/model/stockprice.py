from marshmallow import Schema, fields
import uuid


class Currency():
    def __init__(self, valutadate, currencyid, amount):
        self.valutadate = valutadate
        self.currencyid = currencyid
        self.amount = amount
        self.id = uuid.uuid4()

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    amount = fields.Float()
    id = fields.UUID()
    currencyid = fields.UUID()
    valutadate = fields.DateTime()
