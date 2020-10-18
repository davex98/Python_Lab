import xml.dom.minidom


def modifyXML(path: str):
    root = xml.dom.minidom.parse(path)

    element = root.getElementsByTagName("throughout")
    element.item(0).firstChild.data = "random Characters"

    file = open("newfile.xml", "w")
    file.write(root.toxml())
    file.close()


if __name__ == '__main__':
    modifyXML("random.xml")
