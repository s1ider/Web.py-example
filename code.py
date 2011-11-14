import web

render = web.template.render('templates/', base='base')
render_plain = web.template.render('templates/')

urls = (
	'/$', 'index',
	'/about$', 'about',
	'/flats$', 'flats',
)
app = web.application(urls, globals())

class index:
	def GET(self, name=None):
		navigation = render_plain.navigation('Home')
		return render.index(navigation)

class about:
	def GET(self):
		navigation = render_plain.navigation('About')
		return render.about(navigation)

class flats:
	def GET(self):
		navigation = render_plain.navigation('Flats')
		return render.flats(navigation)
	
if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
