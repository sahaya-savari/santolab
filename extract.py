import os

content_path = r'C:\Users\SANTO\.gemini\antigravity-ide\brain\3671226e-bb66-47b3-825d-2819732c7fdd\.system_generated\steps\6\content.md'
out_path = r'd:\VDLAB\index.html'

try:
    with open(content_path, 'r', encoding='utf-8') as f:
        content = f.read()

    html_start = content.find('<!DOCTYPE html>')
    if html_start != -1:
        html_content = content[html_start:]
        head_start = html_content.find('<head>')
        if head_start != -1:
            html_content = html_content[:head_start + 6] + '\n<base href="https://www.vplayed.com/">\n' + html_content[head_start + 6:]
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print('SUCCESS')
    else:
        print('FAILED: Could not find HTML tag.')
except Exception as e:
    print(f'ERROR: {e}')
