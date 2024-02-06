Language = input("Language: ")

match Language:
	case "Gnglish":
		from po.English import *
	case "German":
		from po.German import *
	case _:
		quit("Unknown Language")


MSG_ID = input("Message id: " )

Call = MSG_ID
Call += "()"
exec(Call)