from UserInterface import displayNumericMenu
from NetworkRequests import BeautifulSoup_URL
from bs4 import BeautifulSoup as BS
import requests, datetime, json, os
import numpy as np

CleanCMD = lambda: os.system('cls') # Clean CMD.

URL = 'https://gestioacademica.upf.edu/pds/consultaPublica/look%5Bconpub%5DInicioPubHora?entradaPublica=true&idiomaPais=ca.ES' # De este enlace, obtengo la lista de centros disponibles.
URL_Object = BeautifulSoup_URL(URL, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}, requests.Session(), requestMethod='GET')

centersCodes = np.array(list(map(lambda x: x.get_text().split(' - '), URL_Object.Soup.find('select', {'class': 'form-control', 'id': 'centro'}).findAll('option')[1:]))) # CentersCodes[:,0] ---> Codes, CentersCodes[:,1] ---> Names

planDocente = str(datetime.datetime.now().year)

displayNumericMenu(centersCodes[:,1]) # Generamos la lista con los centros disponibles.
centro = centersCodes[:,0][int(input('Centro: '))-1] # Del centro que se ha selecionado, extraemos su código.
CleanCMD()

URL_Object.addToURL(f'&planDocente={planDocente}&centro={centro}') # Añadimos el Plan Docente (Año) y el código del Centro a nuestra URL para hacer la petición GET.
URL_Object.GET()

degreesCodes = np.array(list(map(lambda x: x.get_text().split(' - ')[:2], URL_Object.Soup.find('select', {'class': 'form-control', 'id': 'estudio'}).findAll('option')))) # DegreesCodes[:,0] ---> Codes, DegreesCodes[:,1] ---> Names
displayNumericMenu(degreesCodes[:, 1]) # Generamos la lista con los estudios disponibles, después de filtrar según el Plan Docente y el Centro.
estudio = degreesCodes[:,0][int(input('Estudio: '))-1] # Del estudio que se ha selecionado, extraemos su código.
CleanCMD()

URL_Object.addToURL(f'&estudio={estudio}') # Añadimos el estudio selecionado a nuestra URL, para hacer nuestra petición GET.
URL_Object.GET()

studyPlanCodes = list(map(lambda x: x.get_text().split(' - '), URL_Object.Soup.find('form', {'class': 'formee', 'id': 'formu_Edi_Estudio'}).findAll('div')))[3] # studyPlanCode[0] ---> Code, studyPlanCode[1] ---> Name
planEstudio = (''.join([studyPlanCode for studyPlanCode in studyPlanCodes[0] if studyPlanCode.isnumeric()])) # Del plan de estudio que se genera de forma predeterminada, eliminamos todo lo que no sean números.

URL_Object.addToURL(f'&planEstudio={planEstudio}') # Añadimos el Plan de Estudio a nuestra petición.
URL_Object.GET()

gradeNumber = list(map(lambda x: x.get_text(), URL_Object.Soup.find('select', {'class': 'form-control', 'id': 'curso'}).findAll('option')))
trimesterCodes = np.array(list(map(lambda x: [x['value'], x.get_text()], URL_Object.Soup.find('select', {'class': 'form-control', 'id': 'trimestre'}).findAll('option')[1:]))) # TrimesterCodes[:,0] ---> Codes, TrimesterCodes[:,1] ---> Names
groupCodes = np.array(list(map(lambda x: [x['value'], x.get_text()], URL_Object.Soup.find('select', {'name': 'grupos', 'id': 'grupos'}).findAll('option')))) # GroupCodes[:,0] ---> Codes, GroupCodes[:,1] ---> Names


if len(gradeNumber) <= 4: displayNumericMenu(gradeNumber)
else: displayNumericMenu(gradeNumber, indexZero=True)
curso = int(input('Curso: '))
if curso == 0: curso = -1 # En el sistema de la UPF, la opción de optativas se marca como un -1.
CleanCMD()

displayNumericMenu(trimesterCodes[:,1])
trimestre = trimesterCodes[:,0][int(input('Trimestre: '))-1]
CleanCMD()

displayNumericMenu(groupCodes[:,1])
grupo = groupCodes[:,0][int(input('Grupo: '))-1]
CleanCMD()

URL_Subjects = 'https://gestioacademica.upf.edu/pds/consultaPublica/look[conpub]ActualizarCombosPubHora'
DATA = f'planEstudio={planEstudio}&idiomaPais=es.ES&ultimoPlanDocente=&indExamenRecuperacion=true&trimestre={trimestre}&planDocente={planDocente}' \
       f'&accesoSecretaria=null&entradaPublica=true&centro={centro}&estudio={estudio}&idPestana=1&curso={curso}&grupo{grupo}={grupo}&grupos={grupo}'
URL_GetSubjects = BeautifulSoup_URL(URL_Subjects, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}, URL_Object.SESSION, requestMethod='POST', postData=DATA)
subjectsCodes = np.array(list(map(lambda x: x.get_text().split(' - '), URL_GetSubjects.Soup.find('select', {'name': 'asignaturas', 'id': 'asignaturas'}).findAll('option')))) # SubjectsCodes[:,0] ---> Codes, SubjectsCodes[:,1] ---> Names

displayNumericMenu(subjectsCodes[:,1])
asignaturas = list(map(lambda x: subjectsCodes[:,0][int(x)-1], input('Asignaturas (1,2,3,4...): ').split(',')))
CleanCMD()

URL_RND = 'https://gestioacademica.upf.edu/pds/consultaPublica/look[conpub]MostrarPubHora' # Esta URL nos va a permitir encontrar la URL con el RND que nos permite obtner el JSON.
for asignatura in asignaturas: DATA += str(f'&asignatura{asignatura}={asignatura}') # Añadimos a los datos antiguos, las asignaturas que consultar.
URL_GetRND = BeautifulSoup_URL(URL_RND, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}, URL_Object.SESSION, requestMethod='POST', postData=DATA)
javaScriptCode = str(URL_GetRND.Soup.findAll('script', type='text/javascript')[4])
initialPosition = javaScriptCode.find('selecionarRangoHorarios?rnd=') + len('selecionarRangoHorarios?rnd=') # Obteniendo la primera posición del número RND.
RND = javaScriptCode[initialPosition:initialPosition+6].replace("'", "").replace(" ", "")
URL_JSON ='https://gestioacademica.upf.edu/pds/consultaPublica/[Ajax]selecionarRangoHorarios'
DATA_RND = f'rnd={RND}&start=1577808000&end=1609344000'
URL_GetJSON = BeautifulSoup_URL(URL_JSON, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}, URL_Object.SESSION, requestMethod='POST', postData=DATA_RND)
JSON = URL_GetJSON.getJSON(exportFile=True)