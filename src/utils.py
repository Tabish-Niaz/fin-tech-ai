import json
import re

def parse_json_safely(text):
    try:
        cleaned = re.sub(r'```json\n|```\n?', '', text).strip()
        return json.loads(cleaned)
    except Exception as e:
        return None