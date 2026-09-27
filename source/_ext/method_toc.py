"""
Sphinx extension to add method summary tables to doxygenclass output.
Hooks into Breathe's rendering to inject a Qt-style TOC before detailed descriptions.
"""
import xml.etree.ElementTree as ET
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class DoxygenClassWithToc(SphinxDirective):
    """Directive that renders a method TOC followed by doxygenclass output."""

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    option_spec = {
        'members': directives.flag,
        'protected-members': directives.flag,
        'private-members': directives.flag,
        'undoc-members': directives.flag,
        'no-link': directives.flag,
    }

    def run(self):
        class_name = self.arguments[0]

        # Build TOC and get class brief from doxygen XML
        toc_nodes, class_brief = self._build_toc(class_name)

        result = []

        # 1. Brief description first (if available)
        if class_brief:
            para = nodes.paragraph(text=class_brief)
            result.append(para)

        # 2. TOC sections (Public Types, Public Methods)
        result.extend(toc_nodes)

        # 3. Detailed Description section with Breathe output
        detail_section = nodes.section(ids=['detailed-description'])
        detail_section += nodes.title(text='Detailed Description')

        # Use Breathe's doxygenclass with :members: for full formatted output
        rst_content = f"""
.. doxygenclass:: {class_name}
   :members:
"""
        from docutils.statemachine import StringList
        content = StringList(rst_content.split('\n'), source=self.state.document['source'])
        node = nodes.container()
        self.state.nested_parse(content, self.content_offset, node)

        detail_section += node.children
        result.append(detail_section)

        return result

    def _build_toc(self, class_name):
        """Build method summary table from doxygen XML. Returns (toc_nodes, class_brief)."""
        xml_dir = Path(self.env.app.confdir).parent / "xml"

        # Find the XML file
        xml_file = None
        for pattern in [f"class_{class_name}.xml", f"class{class_name}.xml"]:
            candidate = xml_dir / pattern
            if candidate.exists():
                xml_file = candidate
                break

        if not xml_file:
            # Try case-insensitive
            for f in xml_dir.glob("class_*.xml"):
                if f.stem.lower() == f"class_{class_name.lower()}":
                    xml_file = f
                    break

        if not xml_file or not xml_file.exists():
            return [], ""

        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
        except ET.ParseError:
            return [], ""

        result = []

        # Get class brief description
        class_brief = ""
        brief_elem = root.find(".//compounddef/briefdescription/para")
        if brief_elem is not None:
            class_brief = ''.join(brief_elem.itertext()).strip()

        # Collect enums
        enums = []
        for memberdef in root.findall(".//memberdef[@kind='enum'][@prot='public']"):
            name_elem = memberdef.find("name")
            if name_elem is not None and name_elem.text:
                enums.append(name_elem.text)

        if enums:
            section = nodes.section(ids=['public-types'])
            section += nodes.title(text='Public Types')
            bullet_list = nodes.bullet_list()
            for enum in sorted(enums):
                item = nodes.list_item()
                para = nodes.paragraph()
                para += nodes.literal(text=f'enum {enum}')
                item += para
                bullet_list += item
            section += bullet_list
            result.append(section)

        # Collect methods
        methods = []
        for memberdef in root.findall(".//memberdef[@kind='function'][@prot='public']"):
            name_elem = memberdef.find("name")
            if name_elem is None or not name_elem.text:
                continue

            func_name = name_elem.text
            if func_name.startswith('~') or func_name.startswith('operator'):
                continue

            argsstring = memberdef.find("argsstring")
            args = argsstring.text if argsstring is not None and argsstring.text else "()"

            returntype = memberdef.find("type")
            ret = ''.join(returntype.itertext()).strip() if returntype is not None else ""
            # Fix pointer formatting: "QMenu *" -> "QMenu*"
            ret = ret.replace(" *", "*").replace(" &", "&")

            methods.append({
                "name": func_name,
                "args": args,
                "return": ret,
            })

        if methods:
            section = nodes.section(ids=['public-methods'])
            section += nodes.title(text='Public Methods')

            # Two-column table: return type | method signature
            table = nodes.table()
            tgroup = nodes.tgroup(cols=2)
            tgroup += nodes.colspec(colwidth=30)
            tgroup += nodes.colspec(colwidth=70)

            tbody = nodes.tbody()
            for m in sorted(methods, key=lambda x: x["name"]):
                row = nodes.row()

                # Return type column
                entry1 = nodes.entry()
                entry1 += nodes.paragraph('', '', nodes.literal(text=m["return"] or "void"))
                row += entry1

                # Method signature column
                entry2 = nodes.entry()
                para2 = nodes.paragraph()
                para2 += nodes.strong(text=m["name"])
                para2 += nodes.Text(m["args"])
                entry2 += para2
                row += entry2

                tbody += row

            tgroup += tbody
            table += tgroup
            section += table
            result.append(section)

        return result, class_brief


def setup(app):
    app.add_directive('doxygenclass-toc', DoxygenClassWithToc)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
