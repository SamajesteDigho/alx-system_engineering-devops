#!/usr/bin/env ruby
from = ARGV[0].match(/from:[a-zA-Z0-9+]*/)
to = ARGV[0].match(/to:[a-zA-Z0-9+]*/)
flag = ARGV[0].match(/flags:[0-9:\-]*/)

f = from.to_s.split("from:")[1]
t = to.to_s.split("to:")[1]
fl = flag.to_s.split("flags:")[1]
puts "#{f.to_s},#{t.to_s},#{fl.to_s}"
