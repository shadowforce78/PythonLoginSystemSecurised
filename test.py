from simple_chalk import chalk, green

# both of these are the same
print(chalk.green("success"))
print(green("success"))

# chained
print(green.bold("success"))

# assign combinations
success = green.bold.underline
print(success("we did it!"))

# last color wins
print(green.red("this is red"))

# background and foreground colors are separate
whyNot = green.bgWhite.red.bgGray
print(whyNot("this is red text with a gray background"))