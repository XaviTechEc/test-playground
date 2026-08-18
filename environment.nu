export-env { $env.MYNAME = "John Snow, King of Northland" }
export def hello [] { $"hello ($env.MYNAME)" }
