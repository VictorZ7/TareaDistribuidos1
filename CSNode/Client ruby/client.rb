#!/usr/bin/env ruby
#ruby_client.rb
$LOAD_PATH.unshift '.'
require 'grpc'
require 'a_services'
stub = A::Stub.new('localhost:50501', :this_channel_is_insecure)
req = M.new(s: "test")
response = stub.serve(req)
puts("got #{response}")
