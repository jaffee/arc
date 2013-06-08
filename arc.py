#!/usr/bin/python
'''
Arc (from ARChive) is a program for getting things out of your way
that you don't want to delete. It takes files that you specify on the
command line and moves them under the archive-dir, mirroring their
original location in your filesystem. Ex:

My archive-dir is /home/me/.archives/ and I'm working in /home/me/projects/
I run:
$ arc project1.py sometempfile

Those two files will be moved to
/home/me/.archives/home/me/projects/project1.py and
/home/me/.archives/home/me/projects/sometempfile

Usage:
  arc <file>... [options]

Options:
  -a DIR,  --archive-dir DIR   Specifies the directory to which files will be archived. [default: ~/.archives]

'''

import docopt
import shutil
import os, errno

def main():
    args = docopt.docopt(__doc__)
    if args['--config']:
        args['--config'].replace("~", os.environ['HOME'])

    if args['--archive-dir']:
        archive_dir = args['--archive-dir'].replace("~", os.environ['HOME'])

    files = args['files']
    cwd = os.getcwd()

    if archive_dir[-1] == "/":
        archive_dir = archive_dir[:-1]
    for f in files:
        filepath = cwd + "/" + f
        archive_path = archive_dir + filepath
        mkdir_p(os.path.dirname(archive_path))
        shutil.move(filepath, archive_path)


# from http://stackoverflow.com/a/600612/2088767
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise


if __name__=="__main__":
    main()
