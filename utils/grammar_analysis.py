import language_tool_python
from config import LANGUAGE_TOOL_LANGUAGE, GRAMMAR_CHECK_THRESHOLD

def grammar_check(answer):
    tool = language_tool_python.LanguageTool(LANGUAGE_TOOL_LANGUAGE)
    matches = tool.check(answer)
    errors = len(matches)
    total_words = len(answer.split())
    accuracy = max(0, (total_words - errors) / total_words * 100)
    return accuracy
