import PySimpleGUI as sg
sg.theme("DarkBlue7")
sg.theme_text_color("#F0FFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("Selamat Datang di Kelas",text_color=("#FFFF00"),font=("Times",40,"bold","underline"))],
                        [sg.Text("NPM         : 2210010663 ")],
                        [sg.Text("Nama       : Muhammad Maulidi ")],
                        [sg.Text("Kelas        : 5E Regular Banjarmasin ")],
                        [sg.Text("Matkul    : Pemograman Visual 3")],
                        [sg.Text("Prodi       : Teknik Informatika")],
                        [sg.Text("Fakultas : Fakultas Teknologi Informasi")]
                        ],
                size=(600,320),
                font=("Calibri", 18))
window()
window.close()
