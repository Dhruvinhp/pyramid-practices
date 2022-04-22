from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

def sum(request):
    a = int(request.matchdict['a'])
    b = int(request.matchdict['b'])
    return Response('%d + %d = %d' % (a, b, a + b))

def sub(request):
    a = int(request.matchdict['a'])
    b = int(request.matchdict['b'])
    return Response('%d - %d = %d' % (a, b, a - b))

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', 'hello/{name}')
        config.add_route('sum', 'sum/{a}+{b}')
        config.add_route('sub', 'sub/{a}-{b}')
        config.add_view(hello_world, route_name='hello')
        config.add_view(sum, route_name='sum')
        config.add_view(sub, route_name='sub')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
    