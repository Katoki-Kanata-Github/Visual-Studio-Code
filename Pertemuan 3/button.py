import PySimpleGUI as sg
sg.theme("DarkGreen4") #penentuan tema
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Contoh Button",layout=[[sg.Text("Contoh Button",font=("Helvetica",24))],
                                           [sg.Button("Simpan",)],
                                            [sg.Button("Keluar")]],
                   size=(400,200),
                   font=("Times", 18))
kejadian,nilai = window.read()
print(kejadian, "=>",nilai)
window.close()