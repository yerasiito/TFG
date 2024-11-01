replacements = {
    '├': r'\TreeBranch',
    '└': r'\TreeEnd',
    '─': r'\TreeLine',
    '│': r'\TreeVert',
    '  ': r'  ',
}

with open('source.txt', 'r') as file:
    content = file.read()

for char, command in replacements.items():
    content = content.replace(char, f'|{command}|')

with open('processed_source.tex', 'w') as file:
    file.write(content)
