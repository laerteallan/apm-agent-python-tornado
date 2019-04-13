import tornado
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer

from tornado_elastic import ApiElasticHandlerAPM, TornadoApm


class MainTest1(ApiElasticHandlerAPM):

    def get(self, *args, **kwargs):
        self.write({'status': 'ok'})
        self.finish()


class MainTest2(ApiElasticHandlerAPM):

    def get(self):
        raise Exception("Value Error")

    def post(self):
        try:
            raise Exception("erro message")
        except Exception as error:
            # This error(Personalized) captured an send elastic
            self.capture_message("personalized error test")
            self.set_status(500)
            self.write("Internal Server Error")
            self.finish()


def make_app():
    settings = {
        'ELASTIC_APM':
            {
                "SERVICE_NAME": "Teste tornado",
                "SECRET_TOKEN": "",
                "Debug": False},
        "compress_response": True,
    }
    application = tornado.web.Application([
        (r"/", MainTest1),
        (r"/error", MainTest2),
    ], **settings)
    TornadoApm(application)
    return application


if __name__ == "__main__":
    app = make_app()
    server = HTTPServer(app)
    server.bind(8888)
    server.start(1)
    tornado.ioloop.IOLoop.current().start()
