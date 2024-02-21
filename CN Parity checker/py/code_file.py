import random
import socket
import binascii

def generate_random_mac():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    mac_str = ":".join(f"{byte:02X}" for byte in mac)
    return mac_str

def text_to_binary(text):
    binary_string = ' '.join(format(ord(char), '08b') for char in text)
    return binary_string

def sender_MAC():
    sender = generate_random_mac()
    print(sender)
    return sender

def receiver_MAC():
    receiver = generate_random_mac()
    return receiver

def Frame_creation(string,frame_size,char_bit):
  binary_letters = []
  for letter in string:
    binary_letter = bin(ord(letter))[2:].zfill(char_bit)
    binary_letters.append(binary_letter)
  print("The letters converted to binary binary_letters",binary_letters)

  frames = []
  counter = 0
  frame = ""

  for binary_letter in binary_letters:
    frame += binary_letter
    counter += char_bit

    if counter == frame_size:
      frames.append(frame)
      counter = 0
      frame = ""


  if counter > 0:
    frame += "0" * (frame_size - counter)
    frames.append(frame)
  
  print(frames)
  
  bit = 48 
  binr = bin(bit)
  binary_string = binr[2:]
  sender_MAC =   binary_string
  receiver_mac = binary_string

  Header = str(sender_MAC) + str(receiver_MAC)
  print("The Message converted to binary ")
  Payload = str(text_to_binary(string))
  Trailer = str(frames)

  arr=[]
  for frame in frames:
    frame = Header + Payload + Trailer
    arr.append(frame)
  
  for frame in frames:
    parity = 0
    for bit in frame:
      parity = parity^int(bit)
    frame += str(parity) + str(parity ^ 1)

    if not parity:
      print(f"The frame has even parity.")
    else:
      print(f"The frame has odd parity.")

  return frames

def Error_randomizer(frame, error_rate, skip_probability):
  if error_rate == 0:
    return frame 

  corrupted_frame = ""
  for bit in frame:
    if random.random() < skip_probability:
      continue

    if random.random() < error_rate:
      corrupted_frame += "0" if bit == "1" else "1"
    else:
      corrupted_frame += bit
    
  if len(corrupted_frame) < len(frame):
    corrupted_frame += "0" * (len(frame) - len(corrupted_frame))

  return corrupted_frame

def simulate_frame_corruption(frames, error_rate, skip_probability):
  corrupted_frames = []
  for frame in frames:
    if random.random() < skip_probability:
      corrupted_frames.append(frame)
      continue

    corrupted_frame = Error_randomizer(frame, error_rate, skip_probability)
    corrupted_frames.append(corrupted_frame)
  return corrupted_frames

# MY PSEUDO CODE
# def Parity_checker(frames,received_frames):
#   for i in frames,received_frame:
#     count_ones1 = frames.count('1')
    
#     if count_ones1 % 2 == 0:
#       print("{frames} It is an even Parity Frame which was sent ")
    
#     continue 
    
#     count_ones2 = received_frames[i].count('1')
#     if count_ones2 % 2 == 0:
#       print("It is an even Parity Frame Received Accepted , matching if Sender message matches ")
    
#     continue

#     if frames[i] == received_frame[i]:
#       print("Frames matched !")

#     else :
#       print("Frame at receiver end Corrupted ")

#     return 

def check_parity(frame):
    count_ones = frame.count('1')
    is_even_parity = count_ones % 2 == 0
    frame_type = "Even" if is_even_parity else "Odd"
    print
    return frame_type

def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_no = ('localhost', 8080)
    server_socket.bind(port_no)
    server_socket.listen(1)
    print("Waiting for a connection...")

    
    connection, client_address = server_socket.accept()
    print("Connection accepted ! ")
    received_data = []
    parity_type_holder2 = []
    while True:
        data = connection.recv(1024)
        if not data:
            break
        received_frame = data.decode()
        received_data.append(received_frame)

    print(received_data)

    print("for Receiver side ")
    print(" RECEIVER MAC : ",receiver_MAC())
    for frame in received_data:
        frame_type = check_parity(frame)
        parity_type_holder2.append(frame_type)

    connection.close()
    server_socket.close()


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_no = ('localhost', 8080)
    client_socket.connect(port_no)
    string = input("\n\nEnter a message > > ")

    frame_size = 32
    
    char_bit = 4
    
    error_rate = 1
    
    skip_probability = 0.5
    
    frames = Frame_creation(string,frame_size,char_bit)
    print(f"\nFrames divided into {frame_size} bit frames \n",frames)
    
    parity_type_holder1 = []
    print("\n\nfor Sender side ")
    print(" SENDER MAC : ")
    sender_MAC()
    print("Message sent > > ",string)
    for fr in frames:
        frame_type = check_parity(fr)
        parity_type_holder1.append(frame_type)


    C_received_frames = simulate_frame_corruption(frames, error_rate, skip_probability) 

    for frame in C_received_frames:
        client_socket.send(frame.encode())
    client_socket.close()