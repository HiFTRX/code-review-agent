import ast


def compress_code(code: str) -> str:
    try:
        tree = ast.parse(code)
        parts = []

        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom)):
                segment = ast.get_source_segment(code, node)
                if segment:
                    parts.append(segment)

        return "\n\n".join(parts)

    except Exception:
        # if parsing fails, send original
        return code
