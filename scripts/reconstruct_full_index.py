import re

def clean_chunk(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Strip headers like Showing lines ...
    lines = text.splitlines()
    code_lines = []
    for l in lines:
        if re.match(r'^\d+:\s', l):
            # Line format is '123: content'
            idx = l.find(': ')
            code_lines.append(l[idx+2:])
        elif l.strip().isdigit() and ':' in l:
            idx = l.find(':')
            code_lines.append(l[idx+1:])
    return '\n'.join(code_lines)

# Inspect clean chunks
c2843 = clean_chunk('transcript_read_2843.txt')
c2845 = clean_chunk('transcript_read_2845.txt')
c2847 = clean_chunk('transcript_read_2847.txt')
c2849 = clean_chunk('transcript_read_2849.txt')
c2851 = clean_chunk('transcript_read_2851.txt')

print("c2843 lines:", len(c2843.splitlines()), "starts with:", c2843.splitlines()[:3])
print("c2845 lines:", len(c2845.splitlines()), "starts with:", c2845.splitlines()[:3])
print("c2847 lines:", len(c2847.splitlines()), "starts with:", c2847.splitlines()[:3])
print("c2849 lines:", len(c2849.splitlines()), "starts with:", c2849.splitlines()[:3])
print("c2851 lines:", len(c2851.splitlines()), "starts with:", c2851.splitlines()[:3])
