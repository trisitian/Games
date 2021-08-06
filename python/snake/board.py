import tkinter as tk
from tkinter import *
from win32api import GetSystemMetrics 
class Board:
	def __init__(self):
		self.dim = min(GetSystemMetrics(0), GetSystemMetrics(1)) *(2/3);
	def startup(self):
		root = tk.Tk();
		root.title("Snake")
		canvas = tk.Canvas(root, height=self.dim, width=self.dim, bg="#082032");
		canvas.pack();
		frame = tk.Frame(root, bg="#334756");
		frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1);
		root.mainloop();





		#use this for snake colour #FF4C29