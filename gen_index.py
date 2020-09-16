from markwise import *

md = MarkDown()

md.add_l([
    Heading(2, Text("Snow Programming Language")),

    Text("Programming Language to write short code."),

    Line(),

    Heading(3, Text("Download")),

    Link("https://github.com/SnowballSH/Snow-lang/archive/v0.1.0.tar.gz", Text("Github direct download")),

    Line(),

    Heading(3, Text("Support or Contact")),
    Text(f"{Link('https://github.com/SnowballSH/Snow-lang', Text('Github', bold=True))} page to view source code")
])

md.write("index.md")
