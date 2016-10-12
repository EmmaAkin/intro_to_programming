def mul_arr_positon(arr,value)
    result = []
    # Loop through the array to find the index of element in the inner array
    arr.each do|i|
       if !(i.index(value)).nil?
            result=[arr.index(i), i.index(value)]
       end
    end
    result
end

puts returnPosition([[1,2,3,4],[5,6,7,8]],5)
