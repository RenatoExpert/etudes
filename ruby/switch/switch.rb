=begin
This newbie script can show some basics tokens from ruby.
That includes 'puts', loops, formating, switch, if/else
=end

puts "welcome to age analizing"

print "What is your name?"
name = gets.chomp.capitalize

puts "Nice to meet you, %s!" % [name]
born = nil

loop do
  print "%s, Would you dare to tell me the year you born?" % [name]
  borns = gets.chomp
  $born = borns.to_i
  if borns.length==4 and $born>1900 and $born<2022
    puts "Okay"
    break
  else
    puts "Insert a valid year"
  end
end

age = 2021 - $born
puts "Your age is about %d , %s" %  [age,name]

case age
when 0..12
  puts "You are only a kid"
when 13..17
  puts "You are a teenager"
when 18..39
  puts "You are a young adult"
else
  puts "You are pretty old"
end

