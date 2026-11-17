import json

transcript_path = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.system_generated\logs\transcript_full.jsonl'

lines_to_check = [2807, 2843, 2876, 2891, 2892, 2901, 2902]

with open(transcript_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i in lines_to_check:
            try:
                data = json.loads(line)
                print(f"Line {i}: step={data.get('step_index')}, type={data.get('type')}")
                # check tool calls or content
                tool_calls = data.get('tool_calls', [])
                for tc in tool_calls:
                    print(f"   ToolCall: {tc.get('toolName')}, args keys: {list(tc.get('args', {}).keys())}")
                # check content
                content = data.get('content', '')
                if isinstance(content, str):
                    print(f"   Content len: {len(content)}, preview: {content[:100]}...")
            except Exception as e:
                print(f"Error {i}: {e}")
