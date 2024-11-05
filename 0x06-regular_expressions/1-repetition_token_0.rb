#!/usr/bin/env ruby
# Match "hbt{2,5}n" pattern in the input string
puts ARGV[0].scan(/hbt{2,5}n/).join
