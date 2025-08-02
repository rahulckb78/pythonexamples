import markdown

def converted_html(html):
	return markdown.markdown(html)

html = "'http://www.google.com/search?q=flowers+%3Cscript%3Eevil_script()%3C/script%3E'"

print(converted_html(html))