"""Generate the API reference pages and navigation for mkdocstrings."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
src = Path("shortfx")

for package_dir in sorted(src.glob("fx*")):
    if not package_dir.is_dir():
        continue

    package_name = package_dir.name

    for path in sorted(package_dir.glob("*.py")):
        if path.name.startswith("_"):
            continue

        module_name = path.stem
        doc_path = Path(package_name, f"{module_name}.md")
        full_doc_path = Path("reference", package_name, f"{module_name}.md")
        module_path = f"shortfx.{package_name}.{module_name}"

        nav[package_name, module_name] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            fd.write(f"# `{module_name}`\n\n")
            fd.write(f"::: {module_path}\n")

        mkdocs_gen_files.set_edit_path(full_doc_path, path.as_posix())

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
