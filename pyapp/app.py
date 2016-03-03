import web
from contribute.contribute import Contribute
from api.urls import urls

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
