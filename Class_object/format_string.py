def format_string(string,formatter=None,splitter=None):

    class DefaultSplit:
        def splite(self,string):
            return str(string).upper()

    class DefaultFormatter:
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)
    if not splitter:
        splitter=DefaultSplit()
    return splitter.splite(string)

hello_string = "hello world, how are you today?"
print(" input: " + hello_string)
print("output: " + format_string(hello_string))

'''def format_string_again(string,splitter=None):
    class DefaultSplit:
        def splite(self,string):
            return str(string).upper()
    if not splitter:
        splitter=DefaultSplit()
    return splitter.splite(string)
hello_string_again= "hello world how are you today?"
print(" input: " + hello_string_again)
print("output: " + format_string_again(hello_string_again))'''


