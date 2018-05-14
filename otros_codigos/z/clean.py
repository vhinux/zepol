from tempfile import NamedTemporaryFile
from shutil import move

def remove_empty_lines(filename):
    try:
        with open(filename, "rb") as fin, NamedTemporaryFile(delete=False) as fout:
            temp_filename = fout.name
            for line in fin:
                if line.strip():
                    fout.write(line)
    except FileNotFoundError:
        print("{} does not exist.".format(filename))
    else:
        move(temp_filename, filename)

remove_empty_lines('datos_proveedor.txt')
