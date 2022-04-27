# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess
import cPickle
import base64
import flask

# Input injection
def transcode_file(request, filename):
    '''An epic docstring.'''
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def bruh(request, user):
    '''An epic docstring.'''
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh:
    '''An epic docstring.'''
    def __reduce__(self):
        '''An epic docstring.'''
        return (subprocess.Popen, (('/bin/sh',),))

def import_urlib_version(version):
    '''An epic docstring.'''
    exec("import urllib%s as urllib" % version)

@app.route('/')
def index():
    '''An epic docstring.'''
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
