import xss

x = xss.XssCleaner()
test = """A good link should remain.
A bad link should be stripped.
You should not mangle this link.
Authorized tags are fine, but unauthorized tags are not.
An ugly link  should be removed.
Ampersands Ordinarily, cgi.escape() provides complete protection from harmful HTML and javascript, because it strips out all tags completely.  However, sometimes you want to let the user use some HTML tags to include links, formatting, and so on.  This code lets you allow your users to define a subset of HTML tags that you choose, but scrubs them carefully to make sure no harmful code comes through."""
print(x.handle_data(test))