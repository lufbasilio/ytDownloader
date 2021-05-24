import PySimpleGUI as sg
import pytube


def downloader(url):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        global result_request
        result_request = 'Download Feito com Sucesso'
    except:
        result_request = 'Erro ao fazer Download'


sg.theme('BluePurple')	

layout = [
	[sg.Text('URL do Video')],
	[sg.Text('URL', size =(15, 1)), sg.InputText()],
	[sg.Submit(), sg.Cancel()]
]

window = sg.Window('ytDownloader', layout)
event, values = window.read()


url = values[0]
downloader(url)


layoutFinished = [
	[sg.Text(result_request)],
	[sg.Ok()]
]

window = sg.Window('ytDownloader', layoutFinished)
event, values = window.read()
window.close()

window.close()

print(f'log: {event} {values[0]}')