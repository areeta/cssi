echo "Hello World"

# Add a command to the file you created above that navigates into the folder you’re creating.
      # (What command do we use to change directories?)
# Date stamp your new folder name. For example, your program should create a folder named
      # “2017-12-07my_super_cool_folder”
mkdir 12-24-pm
cd 12-24-pm

# Prints out “My current directory is: “ followed by your working directory, and
    # “Here is a list of everything in this directory! “ followed by the contents
    # of your current directory.

echo "My current directory is: "
pwd

echo "Here is a list of everything in this directory!"
cd ..
echo `ls`

# Figure out how to give your bash script an input, and create a file based on
  # that input string. The tutorial linked earlier in the lab has some great examples
  # in the variables section to check out.
