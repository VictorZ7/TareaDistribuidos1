from grpc.tools import protoc

protoc.main(
    (
      '',
      '--proto_path=../../proto/',
      '--python_out=.',
      '--grpc_python_out=.',
      '../../proto/trafico_aereo.proto'
    )
)
