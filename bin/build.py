import os, shutil, subprocess, sys, tempfile

# Run from the repository root:  python bin/build.py
# A landing page (home) is built into the root of docs.
# Each book is an independent mkdocs site; the results are published into the
# docs directory, which is the GitHub Pages location for this repo.

books = ['quick-start','sys-admin','developer','setup']

root = os.getcwd()
output = os.path.join(root, "docs")

for book in books:

    path = os.path.join(root, book)
    dest = os.path.join(output, book)

    # copy css
    orig_css = os.path.join(root, "common/extra.css")
    css = os.path.join(path, "docs/css")
    print("copy css to [%s]" % css)
    shutil.copy(orig_css, css)

    # copy javascript
    js = os.path.join(path, "docs/js")
    os.makedirs(js, exist_ok=True)
    shutil.copy(os.path.join(root, "common/extra.js"), js)

    # clear any previous build of this book
    if os.path.exists(dest):
        shutil.rmtree(dest)

    # build each site directly into docs/<book>
    cmd = ['mkdocs', 'build', '--clean', '-d', dest]
    print("cmd: ", ' '.join(cmd), "(in %s)" % path)
    if subprocess.call(cmd, cwd=path) != 0:
        sys.exit("mkdocs build failed for [%s]" % book)

# build the landing page (home) into a scratch folder and copy it into the
# root of docs, leaving the book folders in place
home = os.path.join(root, "home")
shutil.copy(os.path.join(root, "common/extra.css"), os.path.join(home, "docs/css"))
tmp = tempfile.mkdtemp()
try:
    cmd = ['mkdocs', 'build', '--clean', '-d', tmp]
    print("cmd: ", ' '.join(cmd), "(in %s)" % home)
    if subprocess.call(cmd, cwd=home) != 0:
        sys.exit("mkdocs build failed for [home]")
    shutil.copytree(tmp, output, dirs_exist_ok=True)
finally:
    shutil.rmtree(tmp)
