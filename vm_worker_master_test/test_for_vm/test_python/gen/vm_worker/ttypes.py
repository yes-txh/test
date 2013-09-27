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



class VM_AppInfo:
  """
  Attributes:
   - id
   - name
   - source
   - install_dir
   - exe
   - argument
   - out_dir
   - app_out_dir
   - run_type
   - interval
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'source', None, None, ), # 3
    (4, TType.STRING, 'install_dir', None, None, ), # 4
    (5, TType.STRING, 'exe', None, None, ), # 5
    (6, TType.STRING, 'argument', None, None, ), # 6
    (7, TType.STRING, 'out_dir', None, None, ), # 7
    (8, TType.STRING, 'app_out_dir', None, None, ), # 8
    (9, TType.STRING, 'run_type', None, None, ), # 9
    (10, TType.I32, 'interval', None, None, ), # 10
  )

  def __init__(self, id=None, name=None, source=None, install_dir=None, exe=None, argument=None, out_dir=None, app_out_dir=None, run_type=None, interval=None,):
    self.id = id
    self.name = name
    self.source = source
    self.install_dir = install_dir
    self.exe = exe
    self.argument = argument
    self.out_dir = out_dir
    self.app_out_dir = app_out_dir
    self.run_type = run_type
    self.interval = interval

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
          self.id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.source = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.install_dir = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.exe = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.argument = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.out_dir = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.app_out_dir = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.run_type = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.interval = iprot.readI32();
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
    oprot.writeStructBegin('VM_AppInfo')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.source is not None:
      oprot.writeFieldBegin('source', TType.STRING, 3)
      oprot.writeString(self.source)
      oprot.writeFieldEnd()
    if self.install_dir is not None:
      oprot.writeFieldBegin('install_dir', TType.STRING, 4)
      oprot.writeString(self.install_dir)
      oprot.writeFieldEnd()
    if self.exe is not None:
      oprot.writeFieldBegin('exe', TType.STRING, 5)
      oprot.writeString(self.exe)
      oprot.writeFieldEnd()
    if self.argument is not None:
      oprot.writeFieldBegin('argument', TType.STRING, 6)
      oprot.writeString(self.argument)
      oprot.writeFieldEnd()
    if self.out_dir is not None:
      oprot.writeFieldBegin('out_dir', TType.STRING, 7)
      oprot.writeString(self.out_dir)
      oprot.writeFieldEnd()
    if self.app_out_dir is not None:
      oprot.writeFieldBegin('app_out_dir', TType.STRING, 8)
      oprot.writeString(self.app_out_dir)
      oprot.writeFieldEnd()
    if self.run_type is not None:
      oprot.writeFieldBegin('run_type', TType.STRING, 9)
      oprot.writeString(self.run_type)
      oprot.writeFieldEnd()
    if self.interval is not None:
      oprot.writeFieldBegin('interval', TType.I32, 10)
      oprot.writeI32(self.interval)
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