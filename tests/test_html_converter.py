from .. import enamel


def test_simple_to_html():
    fp = open("files/enml_to_html_simple.enml", 'r')
    out = open("files/simple_html_output.html", 'r')

    assert enamel.fromENML(fp, "text/html") == out.read()
