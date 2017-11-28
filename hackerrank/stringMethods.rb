
# Enter your code here. Read input from STDIN. Print output to STDOUT
def process_text(arr_string)
    new_string = ""
    arr_string.each do |word|
        new_string = new_string.strip + " "+word.strip
    end
    new_string
end
puts process_text(["Hi \n", " what is wrong \r"])