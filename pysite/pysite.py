"""
    A module that takes python definitions and
    writes HTML script out of settings the user
    specifies.
"""
def file_name(file_n="default.html"):
    """
        Creating the html file.
    """
    handle = open(file_n, "w")
    handle.close()
    return file_n


def clear():
    """
        Clearing the html file.
    """
    global FILE
    # open file
    handle = open(FILE, "w")
    # clear file
    handle.write("")
    # close file
    handle.close()


def css(
        background="white",
        parafront="black",
        paraback="white",
        divback="gray",
        div="black",
        header="black",
        link_color="red",
):
    """
        Creates the CSS of the HTML script.
        NOTE: this definition can also be used, alone,
        to create external CSS
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that begins CSS
    handle.write("<html>\n\t<head>\n\t\t<style>\n\n\t\t\t")
    # write CSS that handles background color for the main text body
    handle.write("body {\n\t\t\t\tbackground-color: " + background + ";\n\t\t\t}\n\n\t\t\t")
    # write CSS that handles colors for the paragraphs
    handle.write(
        "p {\n\t\t\t\tbackground-color:"
        + paraback
        + ";\n\t\t\t\tcolor:"
        + parafront
        + ";\n\t\t\t}\n\t\t\t"
    )
    # write CSS that handles colors for the divisions
    handle.write(
        "div {\n\t\t\t\tbackground-color:"
        + divback
        + ";\n\t\t\t\tcolor:"
        + div
        + ";\n\t\t\t}\n\t\t\t"
    )
    # write CSS that handles foreground color for the links
    handle.write("a {\n\t\t\t\tcolor:" + link_color + ";\n\t\t\t}\n\t\t\t")
    # write CSS that handles foreground color for the different size headers
    handle.write("h1 {\n\t\t\t\tcolor:" + header + ";\n\t\t\t}\n\t\t\t")
    handle.write("h2 {\n\t\t\t\tcolor:" + header + ";\n\t\t\t}\n\t\t\t")
    handle.write("h3 {\n\t\t\t\tcolor:" + header + ";\n\t\t\t}\n\t\t\t")
    handle.write("h4 {\n\t\t\t\tcolor:" + header + ";\n\t\t\t}\n\t\t\t")
    # write HTML that ends CSS
    handle.write("</style>\n\t</head>\n</html>\n\n")
    # close file
    handle.close()


def paragraph(text="\n"):
    """
        Creates paragraphs.
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that handles a paragraph
    handle.write("<p>" + text + "</p>\n")
    # close file
    handle.close()


def header1(text="\n"):
    """
        Creates largest header size.
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that handles a large header
    handle.write("<h1>" + text + "</h1>\n")
    # close file
    handle.close()


def header2(text="\n"):
    """
        Creates second largest header size.
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that handles a smaller header
    handle.write("<h2>" + text + "</h2>\n")
    # close file
    handle.close()


def header3(text="\n"):
    """
        Creates third largest header size.
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that handles an even smaller header
    handle.write("<h3>" + text + "</h3>\n")
    # close file
    handle.close()


def header4(text="\n"):
    """
    Creates fourth largest header size.
    """
    global FILE
    # open FILE
    handle = open(FILE, "a")
    # write HTML that handles the tinest header
    handle.write("<h4>" + text + "</h4>\n")
    # close file
    handle.close()


def image(text=""):
    """
        Creates an image given a url or file path.
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that handles a division
    handle.write("<img src='" + text + "'>\n")
    # close file
    handle.close()


def link(url, text):
    """
        Creates a link.
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that handles a division
    handle.write("<a href=" + url + ">" + text + "</a>\n")
    # close file
    handle.close()


def division(text):
    """
        Creates a divison, or diferently colered area.
    """
    global FILE
    # open file
    handle = open(FILE, "a")
    # write HTML that handles a division
    handle.write("<div>" + text + "</div>\n")
    # close file
    handle.close()


# create example website
if __name__ == "__main__":
    # open a file
    FILE = file_name("example.html")
    # clear the file
    clear()
    # create the css for the Website
    css(background="green", paraback="green", divback="rgb(100,100,200)")
    # add content to the Website
    header1("Header 1")
    header2("Header 2")
    header3("Header 3")
    header4("Header 4")
    paragraph("Paragraph")
    division("Division")
    link("https://www.rapidtables.com/web/color/RGB_Color.html", "RGB values")
    paragraph("Image:")
    image(
        "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.sketchappsources.com%2Fre" +
        "sources%2Fsource-image%2Fpython-logo.png&f=1&nofb=1"
    )
