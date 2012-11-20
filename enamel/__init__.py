from html_converter import HTMLConverter
from text_converter import TextConverter


def toENML(fp, contentType=None):
    """
    Takes in input as either a string or file object and returns a string representing
    the ENML of the resultant document converted to the desired format.

    contentType designates the format of the original
    file - by default we try to guess based on the file or fall back to text/html
    """
    #could do this as a map, we'll see.
    if contentType == "text/plain":
        converter = TextConverter()
    elif contentType == "text/html":
        converter = HTMLConverter()
    else:
        converter = HTMLConverter()

    return converter.convertTo(fp)


def fromENML(fp, contentType="text/html"):
    """
    Takes in input as either a string or file object and returns a string representing
    the document converted to the resultant ENML.

    contentType designates the desired format of the outputted file. Defaults to text/html
    """
    #could do this as a map, we'll see.
    if contentType == "text/plain":
        converter = TextConverter()
    elif contentType == "text/html":
        converter = HTMLConverter()
    else:
        converter = HTMLConverter()

    return converter.convertFrom(fp)
