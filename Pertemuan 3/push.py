import PySimpleGUI as sg
susunan= [[sg.VPush(),
         sg.Text("UNISKA MABA", font=("helvetica",24)),
         sg.VPush()],
         
         [sg.VPush(),
         sg.Text("BANJARMASIN", font=("Courier",18)),
         sg.VPush()],
          
         [sg.VPush()]
         ]
window = sg.Window(title="Element Text",
                   layout=susunan,
                   size=(430,200))
window()
window.close()