from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import logging
from xml.dom import minidom
import random
import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from punchout.models import pouser

# Create your views here.

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

@csrf_exempt
def index(request):

    logging.basicConfig(level=logging.NOTSET) # Here
    
    doc = minidom.parseString(request.body.decode('utf-8'))
    laCookie = doc.getElementsByTagName("BrowserFormPost").item(0).getElementsByTagName("URL").item(0).firstChild.nodeValue
    logging.info("--------------------------------------------")
    logging.info("FECHA")
    logging.info(timezone.now() + datetime.timedelta(days=1))
    logging.info("--------------------------------------------")
    
    usuario = UsuarioPO()
    
    #No existe buyercookie
    
    if doc.getElementsByTagName("BuyerCookie").item(0) == None:
        
        for i in range(doc.getElementsByTagName("Extrinsic").length):
            if doc.getElementsByTagName("Extrinsic")[i].getAttribute("name") == "UniqueName":
                usuario.nombre_unico = doc.getElementsByTagName("Extrinsic")[i].firstChild.nodeValue
        
        p = pouser.objects.get(nombre_unico=usuario.nombre_unico)
        usuario.id = p.id
        usuario.nombre = p.nombre
        usuario.buyercookie = p.buyercookie
        usuario.apellido = p.apellido
        usuario.nombre_unico = p.nombre_unico
        usuario.email = p.email
        usuario.user = p.user
        usuario.businessunit = p.businessunit
        usuario.urlToRedirect = p.urlToRedirect
        usuario.secretID = p.secretID
        usuario.sessionExpiresAt = p.sessionExpiredAt
        
        if usuario.sessionExpiresAt < timezone.now():
          usuario.sessionExpiresAt = UsuarioPO().sessionExpiresAt
          usuario.secretID = getLoginParam()
        
        p.urlToRedirect = doc.getElementsByTagName("BrowserFormPost").item(0).getElementsByTagName("URL").item(0).firstChild.nodeValue
        p.sessionOpen = True
        p.totalSessions = p.totalSessions + 1
        p.sessionExpiredAt = usuario.sessionExpiresAt
        p.secretID = usuario.secretID
        p.updatedAt = usuario.updatedAt
        p.save()
        
    #Si existe buyercookie
        
    else:
        usuario.buyercookie = doc.getElementsByTagName("BuyerCookie").item(0).firstChild.nodeValue
        usuario.secretID = getLoginParam()
        usuario.sessionExpiresAt = usuario.sessionExpiresAt
        usuario.createdAt = usuario.createdAt
        usuario.urlToRedirect = doc.getElementsByTagName("BrowserFormPost").item(0).getElementsByTagName("URL").item(0).firstChild.nodeValue
        for i in range(doc.getElementsByTagName("Extrinsic").length):
            if doc.getElementsByTagName("Extrinsic")[i].getAttribute("name") == "FirstName":
                usuario.nombre = doc.getElementsByTagName("Extrinsic")[i].firstChild.nodeValue
            elif doc.getElementsByTagName("Extrinsic")[i].getAttribute("name") == "LastName":
                usuario.apellido = doc.getElementsByTagName("Extrinsic")[i].firstChild.nodeValue
            elif doc.getElementsByTagName("Extrinsic")[i].getAttribute("name") == "UniqueName":
                usuario.nombre_unico = doc.getElementsByTagName("Extrinsic")[i].firstChild.nodeValue
            elif doc.getElementsByTagName("Extrinsic")[i].getAttribute("name") == "UserEmail":
                usuario.email = doc.getElementsByTagName("Extrinsic")[i].firstChild.nodeValue
            elif doc.getElementsByTagName("Extrinsic")[i].getAttribute("name") == "User":
                usuario.user = doc.getElementsByTagName("Extrinsic")[i].firstChild.nodeValue
            elif doc.getElementsByTagName("Extrinsic")[i].getAttribute("name") == "BusinessUnit":
                usuario.businessunit = doc.getElementsByTagName("Extrinsic")[i].firstChild.nodeValue
                
        probas = pouser.objects.all()
        probas.delete()
        
        p = pouser(nombre=usuario.nombre, buyercookie=usuario.buyercookie, apellido=usuario.apellido, nombre_unico=usuario.nombre_unico, email=usuario.email, user=usuario.user, businessunit=usuario.businessunit, urlToRedirect=usuario.urlToRedirect, secretID = usuario.secretID, sessionExpiredAt = usuario.sessionExpiresAt, sessionOpen = True, totalSessions = 1,  createdAt = usuario.createdAt)
        p.save()
    
    xmlRespuesta = """<?xml version="1.0" encoding="UTF-8"?>
                        <!DOCTYPE cXML SYSTEM "http://xml.cxml.org/schemas/cXML/1.1.010/cXML.dtd">
                        <cXML version="1.1.007" xml:lang="en-US" payloadID="200303450803006749@b2b.euro.com" timestamp="2020-06-02T14:36:53-05:00">
                            <Response>
                                <Status code="200" text="OK" />
                                <PunchOutSetupResponse>
                                    <StartPage>
                                        <URL>%s</URL>
                                    </StartPage>
                                </PunchOutSetupResponse>
                            </Response>
                        </cXML>
                    """ % (usuario.getUrlToLogin())
    
    
    #respuesta = HttpResponse(doc.toxml('utf-8'), content_type="application/xml; charset=utf-8")
    respuesta = HttpResponse(xmlRespuesta, content_type="application/xml; charset=utf-8")
    #respuesta.set_cookie('Probas', 'Probas')
       
    probas = pouser.objects.all()
    
    logging.info("----------------------------------------")
    logging.info(probas.values())
    logging.info("----------------------------------------")
    
    #probas.delete()
    
    return respuesta

@csrf_exempt
def fakeLogin(request):
    
    logging.basicConfig(level=logging.NOTSET) # Here
    
    usuario = UsuarioPO()
    
    p = pouser.objects.get(secretID=request.GET.get('id',''))
    
    usuario.id = p.id
    usuario.nombre = p.nombre
    usuario.buyercookie = p.buyercookie
    usuario.apellido = p.apellido
    usuario.nombre_unico = p.nombre_unico
    usuario.email = p.email
    usuario.businessunit = p.businessunit
    usuario.urlToRedirect = p.urlToRedirect
    usuario.secretID = p.secretID
    usuario.sessionExpiresAt = p.sessionExpiredAt
    usuario.sessionOpen = p.sessionOpen
    
    if usuario.sessionExpiresAt < timezone.now() or usuario.sessionOpen != True:
      return HttpResponseBadRequest()
    
    logging.info("--------------------------------------------")
    logging.info("User")
    logging.info(usuario.nombre)
    logging.info("--------------------------------------------")
    
    return HttpResponse(request.GET.get('id',''))