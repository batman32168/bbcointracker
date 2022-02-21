from marshmallow import Schema, fields
import uuid

class Currency():
  def __init__(self,name,description,token):
    self.description = description
    self.token = token
    self.name =name
    self.id = uuid.uuid4()

  def __repr__(self):
    return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
  description = fields.Str()
  id = fields.UUID()
  token =fields.Str()
  name=fields.Str()