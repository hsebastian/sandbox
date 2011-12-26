#!/usr/bin/env ruby

"Doesn't print Hello World unless it tells shell to run with env command"
puts "Also prints Hello World"
puts 3**2
puts Math.sqrt(25)

# methods

def h
  puts "method printing Hello World"
end
h
h()

def hn(name)
  puts "method with arg printing #{name}"
end
hn "hans"
hn('hans')

def hnc(name="world")
  puts "The bit between the braces is turned into a string. Hello #{name.capitalize}!"
end
hnc
hnc "dunia"

# class

class Greeter
  def initialize(name="world")
    # instance variable
    @name = name
  end
  def say_hi
    puts "Hi #{@name}!"
  end
end

g = Greeter.new("martha")
g.say_hi
Greeter.instance_methods

# inspection of object not defined by ancestor classes

Greeter.instance_methods(false)

# instance variable is by default hidden and not accessible

puts g.respond_to?("name")
puts g.respond_to?("say_hi")
puts g.respond_to?("to_s")

# online doc containing books, core API, and std API; http://www.ruby-doc.org/core-1.9.3/index.html

# classes can be opened up again and modified (even if already defined above)

class Greeter
  # this is a getter and a setter
  attr_accessor :name
end

go = Greeter.new("felix")
go.say_hi
go.name
go.name = "akhiong"
go.say_hi

# final example (lots of new things thrown in):

class MegaGreeter
  attr_accessor :names

  def initialize(names="world")
    @names = names
  end

  def say_hi
    # By convention, methods that answer questions
    # (i.e. Array#empty? returns true if the receiver is empty)
    # end in question marks.
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("each")

      # @names is a list of some kind, iterate!
      @names.each do |name|
        puts "Hello #{name}!"
      end
    else
      # otherwise it's a normal string
      puts "Hello #{@names}"
    end
  end

  def say_bye
    if @names.nil?
      puts "..."
    # Duck typing: It determines what it is based on what it does or has ability to do
    elsif @names.respond_to?("join")
      puts "Bye #{@names.join(",")}. Come back soon!"
    else
      puts "Bye #{@names}!"
    end
  end
end

# It looks at $0 to see if this file is used to start the program.
# If it is, then execute as an executable. Otherwise, it's a library.

if __FILE__ == $0
  mg = MegaGreeter.new
  puts mg.names
  mg.names = nil
  puts mg.names
  mg.say_hi
  mg.names = "String"
  mg.say_hi
  mg.say_bye
  mg.names = ["banana", "apple"]
  mg.say_hi
  mg.say_bye
end

