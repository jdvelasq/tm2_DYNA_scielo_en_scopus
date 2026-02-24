from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"csl": "http://purl.org/net/xbiblio/csl"}
ET.register_namespace("", NS["csl"])


def _q(tag: str) -> str:
    return f"{{{NS['csl']}}}{tag}"


def _set_text_first(root: ET.Element, xpath: str, text: str) -> None:
    el = root.find(xpath, NS)
    if el is None:
        raise RuntimeError(f"Missing element at xpath: {xpath}")
    el.text = text


def _set_attr_first(root: ET.Element, xpath: str, **attrs: str) -> None:
    el = root.find(xpath, NS)
    if el is None:
        raise RuntimeError(f"Missing element at xpath: {xpath}")
    for k, v in attrs.items():
        el.set(k, v)


def _invert_name_order_in_macro(
    root: ET.Element, macro_name: str, names_variable: str
) -> None:
    macro = root.find(f".//csl:macro[@name='{macro_name}']", NS)
    if macro is None:
        raise RuntimeError(f"Missing macro: {macro_name}")

    names = macro.find(f".//csl:names[@variable='{names_variable}']", NS)
    if names is None:
        raise RuntimeError(
            f"Missing <names variable='{names_variable}'> in macro '{macro_name}'"
        )

    name = names.find("csl:name", NS)
    if name is None:
        raise RuntimeError(
            f"Missing <name> inside <names variable='{names_variable}'> in macro '{macro_name}'"
        )

    # Apellido primero: Bustelo, J.L.
    name.set("name-as-sort-order", "all")
    name.set("sort-separator", ", ")
    name.set("initialize-with", ".")
    name.set("delimiter", ", ")


def main() -> None:
    in_path = Path("ieee.csl")
    out_path = Path("ieee-apellido-primero.csl")

    if not in_path.exists():
        raise SystemExit(
            "No encuentro ieee.csl en esta carpeta. Descárgalo y ponlo aquí."
        )

    tree = ET.parse(in_path)
    root = tree.getroot()

    # Cambia identidad del estilo para NO sobrescribir IEEE
    _set_text_first(root, ".//csl:info/csl:title", "IEEE - Apellido Primero")
    _set_text_first(
        root, ".//csl:info/csl:id", "http://www.zotero.org/styles/ieee-apellido-primero"
    )

    # Actualiza link rel="self" si existe
    self_link = root.find(".//csl:info/csl:link[@rel='self']", NS)
    if self_link is not None:
        self_link.set("href", "http://www.zotero.org/styles/ieee-apellido-primero")

    # Mantén relación con IEEE (opcional, pero útil como “origen”)
    # (No rompe nada si ya existe; si no existe, lo agrega.)
    has_template = root.find(".//csl:info/csl:link[@rel='template']", NS) is not None
    if not has_template:
        info = root.find(".//csl:info", NS)
        if info is None:
            raise RuntimeError("Missing <info>")
        link = ET.Element(
            _q("link"), {"href": "http://www.zotero.org/styles/ieee", "rel": "template"}
        )
        info.append(link)

    # Aplica cambio clave: autores con apellido primero
    _invert_name_order_in_macro(root, macro_name="author", names_variable="author")

    # (Opcional recomendado) editores también con apellido primero, si el estilo tiene macro "editor"
    # Si no existe, no lo forzamos.
    try:
        _invert_name_order_in_macro(root, macro_name="editor", names_variable="editor")
    except RuntimeError:
        pass

    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"OK: generado {out_path.name}")


if __name__ == "__main__":
    main()
