import socket
# import neopixel
# import board

""" Neopixel Settings"""
"""
pixel_pin = board.D18
num_pixels = 50

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, pixel_order=neopixel.RGB)




"""
""" Sever Settings"""


host = 'localhost'  # "172.20.10.3"
port = 12345
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind((host, port))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    led_counter = 0
    while True:
        data = conn.recv(1024)  # receive data
        client_message = data.decode("utf-8")  # convert data from bytes to string
        if not data:
            break
        else:  # process the message, to light the correct pixels
            client_message = client_message.split(", ")
            print(client_message)
            """
            Reset LED lights before each new message
            
            pixels.fill((0, 0, 0))
            led_counter = 0
            
            """
            for led in client_message:
                print(int(led))
                """
                if led_counter == 0:
                    pixels[int(led)] = (0, 255, 0) # light the first led green
                    
                elif led_counter == len(client_message):
                    pixels[int(led)] = (255, 0, 0) # light the last led red
                else:
                    pixels[int(led)] = (0, 0, 255) # light all other led blue
                    
                led_counter += 1
                """

        conn.send("Message successfully delivered!".encode("utf-8"))
    conn.close()
    print("Connection closed!")
