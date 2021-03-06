#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class AppState:
  APP_NOTFOUND = 0
  APP_ONLINE = 1
  APP_OFFLINE = 2
  APP_FINISHED = 3

  _VALUES_TO_NAMES = {
    0: "APP_NOTFOUND",
    1: "APP_ONLINE",
    2: "APP_OFFLINE",
    3: "APP_FINISHED",
  }

  _NAMES_TO_VALUES = {
    "APP_NOTFOUND": 0,
    "APP_ONLINE": 1,
    "APP_OFFLINE": 2,
    "APP_FINISHED": 3,
  }


class HeartbeatAppInfo:
  """
  Attributes:
   - app_id
   - state
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'app_id', None, None, ), # 1
    (2, TType.I32, 'state', None, None, ), # 2
  )

  def __init__(self, app_id=None, state=None,):
    self.app_id = app_id
    self.state = state

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.app_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.state = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('HeartbeatAppInfo')
    if self.app_id is not None:
      oprot.writeFieldBegin('app_id', TType.I32, 1)
      oprot.writeI32(self.app_id)
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 2)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
