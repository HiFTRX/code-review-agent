from services.compressor import compress_code
from services.rules import basic_rule_check
from services.prompt_builder import build_prompt
from utils.ollama_client import ask_llm


def review(code: str):
    compressed = compress_code(code)
    issues = basic_rule_check(code)
    prompt = build_prompt(compressed, issues)

    ai_feedback = ask_llm(prompt)

    return issues, ai_feedback
