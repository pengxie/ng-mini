#!/usr/bin/env  python

from bottle import route ,run,template,TEMPLATE_PATH,static_file,TEMPLATES
TEMPLATE_PATH = 'views'

@route('/')
@route('/network')
@route('/mini')
@route('/other')
def greet():
    TEMPLATES.clear()
    return template('index')
@route('/static_files/css/<filename>')
def server_static(filename):
    return static_file(filename,root='./static_files/css/', mimetype='text/css')
@route('/static_files/pic/rrd/<filename>')
def server_static(filename):
    return static_file(filename,root='./static_files/pic/rrd')
@route('/static_files/js/<filename>')
def server_static(filename):
    return static_file(filename,root='./static_files/js')
run(server="paste",host='0.0.0.0', port=8083)