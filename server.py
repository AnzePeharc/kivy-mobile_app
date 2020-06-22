import socket
# import neopixel


""" Neopixel Settings"""
"""
pixel_pin = board.D18
num_pixels = 50

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.8, auto_write=False, pixel_order=neopixel.RGB
)




"""
""" Sever Settings"""


host = 'localhost'  # "172.20.10.3"
port = 12345
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            for led in client_message:
                print(int(led))
                """
                if led_counter == 0:
                    pixels[led].fill(0, 255, 0) # light the first led green
                    
                elif led_counter == len(client_message):
                    pixels[led].fill(255, 0, 0) # light the last led red
                else:
                    pixels[led].fill(0, 0, 255) # light all other led blue
                    
                led_counter += 1
                """

        conn.send("Message successfully delivered!".encode("utf-8"))
    conn.close()
    print("Connection closed!")
