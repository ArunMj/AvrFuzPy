# indent Element objects of xml.etree.ElementTree module
import xml.etree.ElementTree  as Et


def indent(elem, level=0):
    i = "\n" + level * "  "
    j = "\n" + (level - 1) * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem


if __name__ == '__main__':
    tree = Et.parse('sample.xml')
    root = tree.getroot()
    Et.dump(tree)
    root = Et.parse('sample.xml').getroot()
    indent(root)
    # Et.dump(root)
