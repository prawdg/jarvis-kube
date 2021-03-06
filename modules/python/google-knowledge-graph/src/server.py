from controller import mapping

import cherrypy

if __name__ == '__main__':
    cherrypy.tree.graft(mapping, "/module/googknowledge")

    cherrypy.server.unsubscribe()

    server = cherrypy._cpserver.Server()
    server.socket_host = "0.0.0.0"
    server.socket_port = 8080
    server.thread_pool = 10
    server.subscribe()

    cherrypy.engine.start()
    cherrypy.engine.block()
