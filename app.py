from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_a_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    def metros_a_pies(self, metros):
        pies = metros * 3.28084
        return pies

    def pies_a_metros(self, pies):
        metros = pies * 0.3048
        return metros

    def decimal_a_binario(self, decimal):
        binario = bin(decimal)
        return binario

    def binario_a_decimal(self, binario):
        decimal = int(binario, 2)
        return decimal

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        conv = Conversion()
        
        if self.path == '/':
            html = '''<h1>Conversion App</h1>
            <ul>
            <li><a href="/celsius?value=389">Celsius 389 a Fahrenheit</a></li>
            <li><a href="/fahrenheit?value=100">Fahrenheit 100 a Celsius</a></li>
            <li><a href="/metros?value=10">Metros 10 a Pies</a></li>
            <li><a href="/pies?value=32">Pies 32 a Metros</a></li>
            <li><a href="/decimal?value=10">Decimal 10 a Binario</a></li>
            <li><a href="/binario?value=1010">Binario 1010 a Decimal</a></li>
            </ul>'''
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())
            
        elif self.path.startswith('/celsius'):
            query = parse_qs(urlparse(self.path).query)
            value = float(query['value'][0])
            resultado = conv.celsius_a_fahrenheit(value)
            html = f'<h1>Resultado: {value}°C = {resultado}°F</h1><a href="/">Volver</a>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())
            
        elif self.path.startswith('/fahrenheit'):
            query = parse_qs(urlparse(self.path).query)
            value = float(query['value'][0])
            resultado = conv.fahrenheit_a_celsius(value)
            html = f'<h1>Resultado: {value}°F = {resultado}°C</h1><a href="/">Volver</a>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())

        elif self.path.startswith('/metros'):
            query = parse_qs(urlparse(self.path).query)
            value = float(query['value'][0])
            resultado = conv.metros_a_pies(value)
            html = f'<h1>Resultado: {value}m = {resultado} pies</h1><a href="/">Volver</a>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())

        elif self.path.startswith('/pies'):
            query = parse_qs(urlparse(self.path).query)
            value = float(query['value'][0])
            resultado = conv.pies_a_metros(value)
            html = f'<h1>Resultado: {value} pies = {resultado}m</h1><a href="/">Volver</a>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())

        elif self.path.startswith('/decimal'):
            query = parse_qs(urlparse(self.path).query)
            value = int(query['value'][0])
            resultado = conv.decimal_a_binario(value)
            html = f'<h1>Resultado: {value} = {resultado}</h1><a href="/">Volver</a>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())

        elif self.path.startswith('/binario'):
            query = parse_qs(urlparse(self.path).query)
            value = query['value'][0]
            resultado = conv.binario_a_decimal(value)
            html = f'<h1>Resultado: {value} = {resultado}</h1><a href="/">Volver</a>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), Handler)
    print('Servidor corriendo en puerto 5000')
    server.serve_forever()
