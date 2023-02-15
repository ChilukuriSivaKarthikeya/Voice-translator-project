from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('listen',views.listen,name="listen"),
    path('RecognizedVoice',views.speak_src,name="speak_src"),
    path('TranslatedVoice',views.speak_dest,name="speak_dest")
]