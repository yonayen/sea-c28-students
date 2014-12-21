#!/usr/bin/env python

import cStringIO
import itertools

class Element(object): 
    tags = (u"<>", u"</>")
    indent = u"    "

    def __init__(self, contents=None, **kwargs):
        #Start list for content of html elements

        if contents:
            self.contents = [contents]
        else:
            self.contents = []

        self.kwargs = kwargs

    def append(self, string):
        try:
            f = cStringIO.StringIO()
            string.render(f)
        except AttributeError:
            self.contents += [string]
        else:
            f.reset()
            self.contents += [f.read()]
            f.close()

    def render(self, file_out, ind=indent):
        # begin to apply proper indentation

        content = list(itertools.chain.from_iterable([x.split(u"\n") for x in self.contents]))

        # tags for manipulation
        temp_tags = list(self.tags)
        if self.kwargs:
            list_tag = list(temp_tags[0])
            # split string into list

            for key in self.kwargs:
                # add tag attributes and style to tag
                list_tag.insert(-1, u'  {}="{}" '.format(key, self.kwargs[keys])) 
            # combine tag into string
            temp_tags[0]] = " ".join(list_tag)

        # put together the tags and text into a list
        all_out = [temp_tags[0]] + \ [ind + x for x in content] + \ [temp_tags[1]]

        # put tags and text into string with newlines 
        file_out.write("\n".join(all_out))


class Html(Element):
    tags = (u"<!DOCTYPE html> \n<html>", u"</html>")

class Body(Element):
    tags = (u"<body>", u"</body>")

class P(Element):
    tags = (u"<p>", u"</p>")

class Head(Element):
    tags = (u"<head>", u"</head>")

class OneLineTag(Element):
    indent = u" "
    
    def render(self, file_out, ind=indent):
        # Modified render from Element class, see file_out.write
         content = list(itertools.chain.from_iterable([x.split(u"\n") for x in self.contents]))


        temp_tags = list(self.tags)
        if self.kwargs:
            list_tag = list(self.tags[0])

            for key in self.kwargs:
                list_tag.insert(-1, u' {}="{}"'.format(key, self.kwargs[key]))
            temp_tags[0] = "".join(list_tag)

        all_out = [temp_tags[0]] + \ [ind + x for x in content] + \ [temp_tags[1]]
        # Combine list of tags and text into a sting with no spaces
        file_out.write("".join(all_out))

class Title(OneLineTag):
    tags = (u"<title>", u"</title>")
 
 
 class SelfClosingTag(Element):
    indent = u" "

    def render(self, file_out, ind=indent):
        temp_tags = list(self.tags)
        if self.kwargs:
            list_tag = temp_tags

            for key in self.kwargs:
                list_tag.insert(-2, u'{}="{}"'.format(key, self.kwargs[key]))
            temp_tags = "".join(list_tag)


        # Combine the single tag into a list.
        all_out = temp_tags
        file_out.write(" ".join(all_out))

class Hr(SelfClosingTag):
    tags = (u"<hr />")
 
 
class Br(SelfClosingTag):
    tags = (u"<br />")
 
 
class A(OneLineTag):
    tags = (u"<a>", u"</a>")

    def __init__(self, *args):
        OneLineTag.__init__(self, args[1], href=args[0])


class Ul(Element):
    tags = (u"<ul>", u"</ul>")
 
 
class Li(Element):
    tags = (u"<li>", u"</li>")
 
 
class H(OneLineTag):
    tags = (u"<h>", u"</h>")

    def __init__(self, *args):
        # Modify name of tag with arg[0]
        list_tags = [list(x) for x in self.tags]
        [x.insert(-1, u"{}".format(args[0])) for x in list_tags]
        self.tags = ["".join(x) for x in list_tags]
        OneLineTag.__init__(self, args[1])

class Meta(SelfClosingTag):
    tags = (u"<meta />")

















































