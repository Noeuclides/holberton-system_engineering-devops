#!/usr/bin/env ruby
puts ARGV[0].scan(/(?!from:)(\w+)(?>\]\s+\[to:)(\+\d+)(?>\]\s\[flags:)([1\:0-]+)/).join(",")
