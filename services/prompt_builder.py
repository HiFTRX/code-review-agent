def build_prompt(context: str, issues):
    issues_text = "\n".join(issues) if issues else "No rule violations."

    return f"""
You are a senior code reviewer.

Important Extracted Code:
{context}

Static Findings:
{issues_text}

Provide:
- Bug risks
- Code smells
- Performance ideas
- Security problems
- Refactoring suggestions

Use bullet points.
"""
