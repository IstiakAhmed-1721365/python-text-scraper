from asyncio import constants
import main
# from bottle import route, run
# @route('/todo')
# def todo_list():
#     print (main.new_url)
# run()
from bottle import route, run

@route('/hello')
def hello():
    return ('<style> div.chr-c {  word-wrap: break-word;} </style>'+'<pre>' + str(main.wcon) + '</pre> <br>\n')

run(host='localhost', port=8080, debug=True)
