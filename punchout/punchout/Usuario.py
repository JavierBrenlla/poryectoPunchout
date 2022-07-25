from django.utils import timezone
import datetime
import random

class UsuarioPO:
    id=""
    nombre = ""
    buyercookie = ""
    apellido = ""
    nombre_unico = ""
    email = ""
    user = ""
    businessunit = ""
    urlToRedirect = ""
    sessionExpiresAt = timezone.now() + datetime.timedelta(days=1)
    torvigoLoginUrl = "http://127.0.0.1:8000/punchout/login?id="
    secretID = ""
    sessionOpen = False
    concurrentSessions = 0
    payloadID = ""
    createdAt = timezone.now()
    updatedAt = timezone.now()
    
    def getUrlToLogin(self):
        return self.torvigoLoginUrl + self.secretID
    
    
def getLoginParam():
    listaCaracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    resultado = ""
    
    for item in range(8):
        numeroAletario = random.randint(0, len(listaCaracteres) - 1)
        resultado += listaCaracteres[numeroAletario]
    
    return resultado