from django import template
register = template.Library()
def decrement_variable(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, variable1, decrement_by = token.split_contents()
        print variable1
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly two arguments" % token.contents.split()[0]
    variable1 = variable1 - int(decrement_by)
    return variable1

register.tag('decrement' , decrement_variable)
