import random
import string
import subprocess
while True:
    def make_random_python(size=1000):
        data = ''.join(random.choices(
            string.ascii_letters + string.digits + " ",
            k=size
        ))

        return f'print("""{data}""")\n'

    filename = ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=16
    )) + ".py"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(make_random_python())

    subprocess.run(["git", "add", filename], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Add {filename}"],
        check=True
    )
    subprocess.run(["git", "push"], check=True)

    print("Pushed", filename)