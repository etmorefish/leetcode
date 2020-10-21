from fs import open_fs
from fs.zipfs import ZipFS, WriteZipFS

def count_python_loc(fs):
    """Count non-blank lines of Python code."""
    count = 0
    for path in fs.walk.files(filter=['*.py']):
        with fs.open(path) as python_file:
            count += sum(1 for line in python_file if line.strip())
    return count


# with open_fs('.') as fs:
#     print(count_python_loc(fs))

with ZipFS('foo.zip', write=True) as new_zip:
    new_zip.writetext(
        'readme.txt',
        'This zip file was written by PyFilesystem'
    )

