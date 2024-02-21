import socket
import tkinter as tk
from tkinter import scrolledtext
from code_file import Frame_creation, check_parity, simulate_frame_corruption

class MultiGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sender's GUI")

        self.prompt_label = tk.Label(master, text="Type your message:")
        self.prompt_label.pack(pady=5)

        self.input_entry = tk.Entry(master, width=40)
        self.input_entry.pack(padx=10, pady=10)

        self.connect_button = tk.Button(master, text="Connect", command=self.connect_to_server)
        self.connect_button.pack(pady=10)

        self.prompt_label1 = tk.Label(master, text=f"Message converted to bit frames ")
        self.prompt_label1.pack(pady=5)
        self.text_area1 = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area1.pack(padx=10, pady=10)

        self.prompt_label2 = tk.Label(master, text="Message Sent")
        self.prompt_label2.pack(pady=5)
        self.text_area2 = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=2)
        self.text_area2.pack(padx=10, pady=10)

        self.prompt_label3 = tk.Label(master, text="Frames Sent")
        self.prompt_label3.pack(pady=5)
        self.text_area3 = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area3.pack(padx=10, pady=10)

        self.prompt_label4 = tk.Label(master, text="Frame Parity")
        self.prompt_label4.pack(pady=5)
        self.text_area4 = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area4.pack(padx=10, pady=10)

        self.prompt_label5 = tk.Label(master, text="Received Frames")
        self.prompt_label5.pack(pady=5)
        self.text_area5 = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area5.pack(padx=10, pady=10)

        self.prompt_label6 = tk.Label(master, text="Received Parity")
        self.prompt_label6.pack(pady=5)
        self.text_area6 = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area6.pack(padx=10, pady=10)
    

        self.text_area_msg = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area_msg.pack(padx=10, pady=10)

    def read_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return None

    def connect_to_server(self):
        string = self.input_entry.get()
        frame_size = 32
        char_bit = 4
        error_rate = 1
        skip_probability = 0.5

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_no = ('localhost', 8080)
        client_socket.connect(port_no)

        frames = Frame_creation(string, frame_size, char_bit)
        self.text_area1.insert(tk.END, f"\nFrames divided into {frame_size} bit frames \n{frames}\n")
        parity_type_holder1 = []
        self.text_area2.insert(tk.END, f"\nMessage sent > > {string}\n")
        for fr in frames:
            frame_type = check_parity(fr)
            parity_type_holder1.append(frame_type)

        for frame, parity in zip(frames, parity_type_holder1):
            client_socket.send(frame.encode())
            self.text_area3.insert(tk.END, f"\nSent frames: {frame}\n")
            self.text_area4.insert(tk.END, f"\nParity of frames: {parity}\n")

        with open("p1.txt", 'w') as file:
            for i in parity_type_holder1:
                file.write(i + '\n')

        content1 = self.read_file("p1.txt")
        C_received_frames = simulate_frame_corruption(frames, error_rate, skip_probability)
        parity_type_holder2 = []

        for fr2 in C_received_frames:
            client_socket.send(frame.encode())
            frame_type2 = check_parity(fr2)
            parity_type_holder2.append(frame_type)

        for frame, parity in zip(C_received_frames, parity_type_holder2):
            client_socket.send(frame.encode())
            self.text_area5.insert(tk.END, f"\nReceived frames: {frame}\n")
            self.text_area6.insert(tk.END, f"\nParity of frames: {parity}\n")

        with open("p2.txt", 'w') as file:
            for i in parity_type_holder2:
                file.write(i + '\n')

        
        

        client_socket.close()
        self.create_receiver_window(C_received_frames, parity_type_holder2)

    def create_receiver_window(self, received_frames, parity_types):
            receiver_window = tk.Toplevel(self.master)
            receiver_window.title("Receiver's GUI")

            prompt_label_received_frames1 = tk.Label(receiver_window, text="Received Frames")
            prompt_label_received_frames1.pack(pady=5)

            text_area_received_frames1 = scrolledtext.ScrolledText(receiver_window, wrap=tk.WORD, width=40, height=10)
            text_area_received_frames1.pack(padx=10, pady=10)

            prompt_label_received_parity2 = tk.Label(receiver_window, text="Received Parity")
            prompt_label_received_parity2.pack(pady=5)

            text_area_received_parity2 = scrolledtext.ScrolledText(receiver_window, wrap=tk.WORD, width=40, height=10)
            text_area_received_parity2.pack(padx=10, pady=10)


            for frame, parity in zip(received_frames, parity_types):
                text_area_received_frames1.insert(tk.END, f"\nReceived frame: {frame}\n")
                text_area_received_parity2.insert(tk.END, f"\nReceived parity: {parity}\n")

            content1 = self.read_file("p1.txt")
            content2 = self.read_file("p2.txt")

            if content1 == content2:
                result_message = "Message Received successfully"
            else:
                result_message = "Message Corrupted, please retransmit"

            # Display the result in the receiver's GUI
            result_label = tk.Label(receiver_window, text=f"Message accuracy: {result_message}")
            result_label.pack(pady=10)
            self.text_area_msg.insert(tk.END, f"\nMessage accuracy: {result_message}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiGUI(root)
    root.mainloop()
