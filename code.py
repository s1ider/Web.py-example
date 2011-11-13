import web
from web import form

render = web.template.render('templates/')

urls = (
	'/(.*)', 'index',
	'/login', 'login'
)
app = web.application(urls, globals())

class index:
	def GET(self, name=None):
		return render.index(name)
	
if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
