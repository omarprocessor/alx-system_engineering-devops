#!/usr/bin/env ruby
# Match a 10-digit phone number with no spaces or symbols
puts ARGV[0].scan(/^\d{10}$/).join
