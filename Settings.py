HOST = "irc.twitch.tv" #Twitch server
PORT = 6667 #Server port
PASS = "" #your oauth goes here. Get it from https://twitchapps.com/tmi/
BOTNAME = "retrasobot" #the name the bot will have when connecting to IRC. Note: This is NOT the name you will see in chat
CHANNEL = "capitanretraso" #your channel name. Use lowercase
ALLOW_REMOTE_SHUTDOWN = "true" #if this is set to true, the password below will work. Set it to false if you don't want it enabled
REMOTE_SHUTDOWN_PASSWORD = "!shutdown" #if this is written in the chat the bot will shut down
HELP = "Write UP, DOWN, LEFT, RIGHT, A, B, L, R, SELECT or START to control the game! (only 1 input per message is supported)" #The message the bot will send if someone writes the !help command

class KEYMAPS:
	keymap = { #the numbers after the colon (:) correspond to the virtual key that will be pressed with each command (list below)
		"up": 56, #8
		"down": 50, #2
		"left": 52, #4
		"right": 54, #6
		"a": 55, #7
		"b": 57, #9
		"start": 49, #1
		"select": 51, #3
		"l": 48, #0
		"r": 53, #5
	} #more keys can be added or removed

	
""" VIRTUAL KEY LIST

vk_BackSpace = 8
vk_Tab = 9
vk_Return = 13
vk_Shift = 16	
vk_Control = 17
vk_Alt = 18	
vk_Pause = 19	
vk_CapsLock = 20
vk_Escape = 27
vk_Space = 32	
vk_PageUp = 33
vk_PageDown = 34
vk_End = 35	
vk_Home = 36
vk_Left = 37
vk_Up = 38	
vk_Right = 39
vk_Down = 40
vk_PrintScreen = 44	
vk_Insert = 45
vk_Delete = 46 


vk_0 = 48
vk_1 = 49
vk_2 = 50
vk_3 = 51
vk_4 = 52
vk_5 = 53
vk_6 = 54
vk_7 = 55
vk_8 = 56
vk_9 = 57


vk_A = 65	
vk_B = 66
vk_C = 67
vk_D = 68
vk_E = 69
vk_F = 70
vk_G = 71
vk_H = 72
vk_I = 73
vk_J = 74
vk_K = 75
vk_L = 76
vk_M = 77
vk_N = 78
vk_O = 79
vk_P = 80
vk_Q = 81
vk_R = 82
vk_S = 83
vk_T = 84
vk_U = 85
vk_V = 86
vk_W = 87
vk_X = 88
vk_Y = 89
vk_Z = 90

   
vk_NumPad0 = 96
vk_NumPad1 = 97
vk_NumPad2 = 98
vk_NumPad3 = 99
vk_NumPad4 = 100
vk_NumPad5 = 101
vk_NumPad6 = 102
vk_NumPad7 = 103
vk_NumPad8 = 104
vk_NumPad9 = 105


vk_Multiply = 106
vk_Add = 107
vk_Subtract = 109
vk_Decimal = 110
vk_Divide = 111
vk_F1 = 112
vk_F2 = 113
vk_F3 = 114
vk_F4 = 115
vk_F5 = 116
vk_F6 = 117
vk_F7 = 118
vk_F8 = 119
vk_F9 = 120
vk_F10 = 121
vk_F11 = 122
vk_F12 = 123
vk_F13 = 124
vk_F14 = 125
vk_F15 = 126
vk_F16 = 127
 

vk_NumLock = 144
vk_ScrollLock = 145
vk_LShift = 160
vk_RShift = 161 
vk_LControl = 162 
vk_RControl = 163 
vk_LAlt = 164
vk_RAlt = 165
vk_SemiColon = 186
vk_Equals = 187
vk_Comma = 188
vk_UnderScore = 189
vk_Period = 190
vk_Slash = 191
vk_BackSlash = 220
vk_RightBrace = 221
vk_LeftBrace = 219
vk_Apostrophe = 222
"""
