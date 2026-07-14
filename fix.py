import os

root_dir = r'D:\01.TheScriptureAudit\the-scripture-audit'

# 1. Update internal speaker names in all md files
for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.git' in dirpath: continue
    for filename in filenames:
        if filename.endswith('.md'):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Replace TheScripture.org with TheScriptureBeliever
                content = content.replace('TheScripture.org', 'TheScriptureBeliever')
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'Updated speaker name in: {filepath}')
            except Exception as e:
                print(f'Error processing {filepath}: {e}')

# 2. Insert Disclaimer for v2
filepath = os.path.join(root_dir, r'05_REPORT\bible_believer', 'REPORT_TheScriptureOrg_VS_Researcher_v2.md')
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    note_text = """> [!NOTE]
> **※ Disclaimer (The Meaning of 'TheScriptureBeliever')**
> The speaker '**TheScriptureBeliever**' appearing in this document holds a distinct identity different from the traditional term 'Bible Believer' used in mainstream Christianity.
> Traditionally, the word 'Bible' is a man-made title that does not appear even once in the entire 66 books of the original KJV text. On the contrary, when Jesus and Paul referred to the absolute Word of God, the exact word inspired directly by the Holy Spirit is exclusively **"The Scripture"** (John 5:39, 2 Tim 3:16).
> This speaker sets themselves apart from traditional doctrines (Bible Believer) that promote a term absent from the original text, clarifying that they are one who believes and defends only the original language of recorded truth (The Scripture) itself.

"""
    if "The Meaning of 'TheScriptureBeliever'" not in content:
        if '# TheScriptureBeliever' in content:
            content = content.replace('# TheScriptureBeliever', note_text + '# TheScriptureBeliever', 1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Added disclaimer to v2')
