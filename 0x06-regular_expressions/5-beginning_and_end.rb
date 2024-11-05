#!/usr/bin/env ruby
# Match strings that start with "h" and end with "n" with any single character in between
puts ARGV[0].scan(/^h.n$/).join
