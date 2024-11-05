#!/usr/bin/env ruby
# Extract sender, receiver, and flags from the log entry
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).map { |match| match.join(",") }
