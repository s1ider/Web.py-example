import web

render = web.template.render('templates/', base='base')

urls = (
	'/$', 'index',
	'/about$', 'about',
	'/flats$', 'flats',
)
app = web.application(urls, globals())

class index:
	def GET(self, name=None):
		return render.index()

class about:
	def GET(self):
		return render.about()

class flats:
	def GET(self):
		return render.flats()
	
if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
