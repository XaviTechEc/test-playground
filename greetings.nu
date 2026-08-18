export def hello [name: string] {
    $"hello ($name)!"
}

export def hi [where: string] {
    $"hi ($where)!"
}


# Greet a VIP and a list of names
# 
# Use for loop to iterate over the names and print a greeting for each one. Then, print a special greeting for the VIP.
#
# Category: Greetings
# 
# This command:
# - does not create a scope
# - is not a built-in command
# - is not a subcommand
# - is not part of a plugin
# - is not a keyword
#
# Usage:
#   > vip-greet <vip> <name1> <name2> ... <nameN>
# 
# Flags:
# 
# -h, --help - Show this help message for this command
# 
# Signatures: 
# 
#   <any> | vip-greet [<string> <string> ...] | <any>
# 
# Parameters:
# 
#   vip: <string> - The VIP's name
#   ...names: string - The list of other guests
export def vip-greet [
    vip: string # The VIP's name
    ...names: string # The list of other guests
] {
    for $name in $names {
        print $"hello ($name)"
    }

    print $"And hello to our VIP ($vip)!"
}

export def main [] {
    "greetings and salutations!"
}
