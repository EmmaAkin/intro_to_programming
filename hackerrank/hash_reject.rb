hashes = Hash.new
values_only = ->(hashes){ hashes.values}
e = values_only.({1=> 3, 4=> 5})
puts e