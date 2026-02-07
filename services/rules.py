def basic_rule_check(code: str):
    issues = []

    if "print(" in code:
        issues.append("Avoid print statements in production.")

    if "TODO" in code or "FIXME" in code:
        issues.append("Pending TODO/FIXME found.")

    if "except:" in code:
        issues.append("Avoid bare except. Catch specific exceptions.")

    if len(code.splitlines()) > 300:
        issues.append("Large file. Consider modularization.")

    return issues
