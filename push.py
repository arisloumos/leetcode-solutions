import os
import re
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
folders = ["1-Easy", "2-Medium", "3-Hard"]
renamed = []
pattern = re.compile(r'^(\d+)\.\s*(.*?)(?:\.py)?$')

for f in folders:
    if not os.path.exists(f): continue
    for filename in os.listdir(f):
        match = pattern.match(filename)
        if match:
            num = match.group(1).zfill(4)
            new_name = f"{num}-{re.sub(r'\s+', '-', match.group(2))}.py"
            os.rename(os.path.join(f, filename), os.path.join(f, new_name))
            print(f"Renamed: {filename} -> {new_name}")
            renamed.append(num)

status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()

if status:
    print("\nChanges detected. Pushing to GitHub...")
    subprocess.run(["git", "add", "."])
    msg = f"Add solution(s): {', '.join(renamed)}" if renamed else "Update LeetCode solutions"
    subprocess.run(["git", "commit", "-m", msg], stdout=subprocess.DEVNULL)
    
    push = subprocess.run(["git", "push"], capture_output=True, text=True)
    if push.returncode == 0:
        print(f"Pushed successfully: '{msg}'")
    else:
        print(f"Push failed! Here is the error:\n{push.stderr}")
else:
    print("Everything is up to date!")