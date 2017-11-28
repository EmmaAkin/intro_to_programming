# Your code here
def prime?(n)
  checker = true
  (2..n/2).each do |d|
   if (n % d) == 0
    checker = false
   end
  end
    return checker
end
puts prime?(980817)