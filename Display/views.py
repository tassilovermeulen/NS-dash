from django.shortcuts import render
# Create your views here.
from django.views import View

from nsapi import NSApi


class IndexView(View):
    def get(self, request):
        apiwrapper = NSApi("527188@student.glu.nl", "pd6lcTRQk3UXIy5KgRUi1qR6gCBCeBZuocc4vuNajaKi6I9G2D6gmQ")
        gutt = apiwrapper.get_departures("ut")
        # Yeet

        for train in gutt:
            gutt[train]["departure_time"] = gutt[train]["departure_time"].strftime("%H:%M")
            gutt[train]["comments"] = "\n".join(gutt[train]["comments"])
            if gutt[train]["route"]:
                gutt[train]["via_text"] = "via {}".format(gutt[train]["route"])
            else:
                gutt[train]["via_text"] = ""

        return render(request, "Display/home.html", {
            "gutt": gutt
        })
