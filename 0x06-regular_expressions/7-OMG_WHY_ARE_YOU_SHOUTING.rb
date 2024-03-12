#!/usr/bin/env ruby
result = ARGV[0].scan(/[A-Z]*/)
for x in result do
    print x
end
puts
