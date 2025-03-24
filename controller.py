from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNMax(self):
        return self._model.NMax

    def getTMax(self):
        return self._model.TMax

    def reset(self, e):
        self._model.reset()
        self._view._txtOutT.value = self._model.T
        self._view._lv.controls.clear()
        self._view._lv.controls.append(ft.Text("Indovina il numero"))
        self._view._txtInGuess.disabled = False
        self._view._btnPlay.disabled = False
        self._view.update()

    def play(self, e):
        tentativoStr = self._view._txtInGuess.value

        if tentativoStr == "":
            self._view._lv.controls.append(ft.Text("Attenzione, inserisci un numero", color="red"))
            self._view.update()
            return

        try:
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(ft.Text("Attenzione, devi inserire un numero intero", color="red"))
            self._view.update()
            return

        result = self._model.play(tentativoInt)
        self._view._txtInGuess.value = ""

        if result == 0: # vittoria
            self._view._lv.controls.append(ft.Text(f"Hai vinto! Il segreto era {tentativoInt}", color="green"))
            self._view._btnPlay.disabled = True     # disabilito la possibilità di giocare o scrivere cose nuove
            self._view._txtInGuess.disabled = True
            self._view.update()
            return
        else:
            self._view._txtOutT.value = self._model.T
            if result == 2: # sconfitta, vite finite
                self._view._lv.controls.append(ft.Text(f"Hai perso! Il segreto era {self._model.segreto}", color="red"))
                self._view._btnPlay.disabled = True
                self._view._txtInGuess.disabled = True
                self._view.update()

            elif result == -1:
                self._view._lv.controls.append(ft.Text(f"Il segreto è più piccolo di {tentativoInt}"))
                self._view.update()

            elif result == 1:
                self._view._lv.controls.append(ft.Text(f"Il segreto è più grande di {tentativoInt}"))
                self._view.update()