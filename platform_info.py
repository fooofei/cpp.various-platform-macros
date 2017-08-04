#coding=utf-8

'''
uname -s print the operating system name.

uname -n machine name

uname -r a version

uname -v print the operating system version.

'''

import os
import sys
import subprocess


def _exec_check_output(*popenargs, **kwargs):
    ''' py2.6 py2.7
        copyed from python2.7 for run on py2.6
    '''
    from subprocess import Popen
    from subprocess import PIPE
    from subprocess import CalledProcessError
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise CalledProcessError(retcode, cmd, output=output)
    output = output.rstrip()
    return output.decode('utf-8')

def entry():
    commands = [
        [u'uname', u'-s'],
        [u'uname', u'-n'],
        [u'uname', u'-r'],
        [u'uname', u'-v'],
        [u'uname', u'-m'],
        [u'uname', u'-p'],
        [u'uname',u'-a'],
        [u'getconf',u'LONG_BIT'],
        [u'getconf',u'WORD_BIT'],
        [u'gcc',u'-dumpmachine'],
    ]

    for command in commands:
        r = _exec_check_output(command,stderr=subprocess.STDOUT)
        v =[(u'$ {0}'.format(u' '.join(command)))]
        v.append(u'  {0}'.format(r))
        print(os.linesep.join(v))

if __name__ == '__main__':
    entry()