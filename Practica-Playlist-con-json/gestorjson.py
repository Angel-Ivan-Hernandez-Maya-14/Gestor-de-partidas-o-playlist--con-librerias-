import json
import random
import os

clasica=("Sinfonía n.º 5 de udwig van Beethoven", "Una pequeña música nocturna de Wolfgang Amadeus Mozart","Las cuatro estaciones de Antonio Vivaldi", "Tocata y fuga en re menor de Johann Sebastian Bach","Nocturnos, Op. 9 de Frédéric Chopin","Nuvole Bianche de Ludovico Einaudi")
country=("Beautiful Crazy de Luke Combs","Last Night de Morgan Wallen","Ring of Fire de Johnny Cash","Tennessee Whiskey de Chris Stapleton","Something in the Orange de Zach Bryan")
electro=("One More Time de Daft Punk","Wake Me Up de Avicii","The Business de Tiësto","Happier de Marshmello y Bastille","Where You Are de John Summit")
hiphop=("FE!N de Travis Scott","God's Plan de Drake","Lose Yourself de Eminem","California Love de 2Pac","HUMBLE. de Kendrick Lamar","Sprinter de Central Cee","Munch (Feelin' U) de Ice Spice")
jazz=("What a Wonderful World de Louis Armstrong","So What de Miles Davis","My Favorite Things de John Coltrane","Don't Know Why de Norah Jones","Truth de Kamasi Washington")
popm=("Billie Jean de Michael Jackson","Levitating de Dua Lipa","Blinding Lights de The Weeknd","Good Luck, Babe! de Chappell Roan","Anti-Hero de Taylor Swift","Espresso de Sabrina Carpenter","That's So True de Gracie Abrams","Thriller de Michael Jackson","Save Your Tears de The Weeknd","Sugar de Marron 5","Shape of You de Ed Sheeran","Mirrors de Justin Timberlake", "Happy de Pharrell Williams","STAY de The Kid LAROI y Justin Bieber","golden hour de JVKE","7 Years de Lukas Graham","Youngblood de 5 Seconds of Summer","Bad Romance de Lady Gaga","As It Was de Harry Styles")
punk=("Blitzkrieg Bop de Ramones","Anarchy in the UK de The Sex Pistols","Basket Case de Green Day","All the Small Things de Blink-182","Misery Business de Paramore","BLACKOUT de Turnstile")
rock=("Bohemian Rhapsody de Queen","Stairway to Heaven de Led Zeppelin","Back in Black de AC/DC","Smells Like Teen Spirit de Nirvana","Everlong de Foo Fighters","ZITTI E BUONI de Måneskin","Highway Tune de Greta van Fleet")
reggae=("No Woman, No Cry de Bob Marley y The Wailers","The Harder They Come de Jimmy Cliff","Sweat (A La La La La Long) de Inner Circle","Welcome to Jamrock de Damian Marley","Smile Jamaica de Chronixx","Three Little Birds de Bob Marley y The Wailers","Red Red Wine de UB40","Tus Ojos de Los Cafres","Sentimiento Original de Gondwana","Ilegal de Cultura Profética")
raeggeton=("Gasolina de Daddy Yankee","Danza Kuduro de Don Omar","Tití Me Preguntó de Bad Bunny","PROVENZA de Karol G","Todo De Ti de Rauw Alejandro","Wiggy de Young Miko","BABY KEILAN de Omar Courtz")
metal=("Paranoid de Black Sabbath","Enter Sandman de Metallica","The Trooper de Iron Maiden","Duality de Slipknot","Stranded de Gojira","The Summoning de Sleep Token")
blues=("The Thrill Is Gone de B.B King","Cross Road Blues de Robert Johnson","Mannish Boy de Muddy Waters","Layla (Acoustic) de Eric Clapton","Bright Lights de Gary Clark Jr.")
disco=("Stayin' Alive de Bee Gees","September de Earth, Wind & Fire","I Will Survive de Gloria Gaynor","Dancing Queen de ABBA","I Feel Love de Donna Summer","Physical de Dua Lipa","Hypnotized de Purple Disco Machine")
opera=("Nessun dorma de Luciano Pavarotti","Casta Diva de Maria Callas","Time to Say Goodbye de Andrea Bocelli","E lucevan le stelle de Plácido Domingo","Phantom of the Opera de Sarah Brightman")
flamenco=("La Leyenda del Tiempo de Camarón de la Isla","Entre dos aguas de Paco de Lucía","Omega de Enrique Morente","Malamente de Rosalía","Volver de Estrella Morente","Pequeño Reloj de Israel Fernández","Guerrita de Dellafuente")
salsa=("La Vida Es Un Carnaval de Celia Cruz","El Cantante de Héctor Lavoe","Pedro Navaja de Rubén Blades","Vivir Mi Vida de Marc Anthony","Cali Pachanguero de Grupo Niche","Cobarde de Yahaira Plasencia")
cumbia=("Nunca es Suficiente de Los Ángeles Azules","Cumbia Sobre el Río de Celso Piña","Como la Flor de Selena","No Te Voy Perdonar de Grupo Cañaveral","Se Me Perdió la Cadenita de La Sonora Dinamita")
mariachi=("El Rey de Vicente Fernández","El Jinete de José Alfredo Jiménez","Me Dediqué a Perderte de Alejandro Fernández","La Bikina de Luis Miguel","El Son de la Negra de Mariachi Vargas de Tecalitlán","No Voy a Llorar de Majo Aguilar")
rap=("N.Y. State of Mind de Nas","Juicy de The Notorious B.I.G.","Not Like Us de Kendrick Lamar","Middle Child de J. Cole","Stronger de Kanye West","Doja de Central Cee","Goteo de Duki")
trap=("SICKO MODE de Travis Scott","Mask Off de Future","Bad and Boujee de Migos","Soy Peor de Bad Bunny","Sola de Anuel AA","BLF de Luar La L","Gatita Gangster de Dei V","TORE UP de Don Toliver")
ryb=("I Will Always Love You de Whitney Houston","Let's Get It On de Marvin Gaye","Yeah! de Usher","Snooze de SZA","Thinkin Bout You de Frank Ocean","Coming Home de Leon Bridges","On My Mama de Victoria Monét")
regional=("Contrabando y Traición de Los Tigres del Norte","Nieves de Enero de Chalino Sánchez","un x100to de Grupo Frontera","Ella Baila Sola de Peso Pluma","Madonna de Óscar Maydon","Princesa de Tito Double P")
indie=("Last Nite de The Strokes","Do I Wanna Know? de Artic Monkeys","The Less I Know The Better de Tame Impala","Dog Days Are Over de Florence + The Machine","Are You Bored Yet? de Wallows","Promise de Laufey","Hush de The Marías")
kpop=("Dynamite de BTS","DDU-DU DDU-DU de BLACKPINK","God's Menu de Stray Kids","Super Shy de NewJeans","EASY de LE SSERAFIM")
ska=("Ghost Town de The Specials","Our House de Madness","Santeria de Sublime","La Carencia de Panteón Rococó","Matador de Los Fabulosos Cadillacs","Amargo Adés de Inspector","Todos Locos de  Los Caligaris")
balada=("El Triste de José José","La Incondicional de Luis Miguel","Vivir Así Es Morir de Amor de Camilo Sesto","Tu Falta de Querer de Mon Laferte","Querida de Juan Gabriel","Azul de Cristian Castro")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_JSON = os.path.join(BASE_DIR, "playlist.json")

if os.path.exists(RUTA_JSON):
    with open(RUTA_JSON,"r",encoding="utf-8") as archivo:
        datospl=json.load(archivo)
        canciones=datospl["canciones"]
        artistas=datospl["artistas"]
        generos=datospl["generos"]
else:
    canciones=[]
    artistas=[]
    generos=[]

def menu():
    print("\n===MENU DE PLAYLIST===")
    print("1. Agregar cancion")
    print("2. Mostrar playlist")
    print("3. Buscar cancion")
    print("4. Eliminar cancion")
    print("5. Salir\n")

def agregar():
    cancion=str(input("Titulo de la cancion: "))
    artista=str(input("Artista: "))
    genero=str(input("Género: "))
    canciones.append(cancion)
    artistas.append(artista)
    generos.append(genero)
    print(f"´{cancion}´ de {artista} agregada con éxito.")
    datospl={"canciones":canciones,"artistas":artistas,"generos":generos}
    with open (RUTA_JSON,"w") as archivo:
        json.dump(datospl,archivo,indent=4)
    g=genero.strip().lower()
    crspg=None
    if g=="clasica" or g=="clásica" or g=="clasic" or g=="calsica":
        crspg= clasica
    elif g == "country" or g=="contry":
        crspg=country
    elif g=="electro" or g=="electronica" or g=="electrónica":
        crspg=electro
    elif g=="hiphop" or g=="hip hop":
        crspg=hiphop
    elif g=="jazz":
        crspg=jazz
    elif g=="pop":
        crspg=popm
    elif g=="punk":
        crspg=punk
    elif g=="rock" or g=="rock and roll" or g=="rock-roll" or g=="rock&roll" or g=="rock alternativo":
        crspg=rock
    elif g=="reggae" or g=="reggue" or g=="regue":
        crspg=reggae
    elif g=="reggaeton" or g=="raeggeton" or g=="reggaetón" or g=="raeggetón" or g=="regueton" or g=="reguetón":
        crspg=raeggeton
    elif g=="metal" or g=="heavy metal" or g=="heavy-metal":
        crspg=metal
    elif g=="blues":
        crspg= blues
    elif g=="disco":
        crspg=disco
    elif g=="opera" or g=="ópera":
        crspg=opera
    elif g=="flamenco":
        crspg=flamenco
    elif g=="salsa":
        crspg=salsa
    elif g=="cumbia" or g=="cumbion" or g=="cumbión":
        crspg=cumbia
    elif g=="mariachi":
        crspg=mariachi
    elif g=="rap":
        crspg=rap
    elif g=="trap":
        crspg=trap
    elif g=="ryb" or g=="r&b":
        crspg=ryb
    elif g=="regional":
        crspg=regional
    elif g=="indie" or g=="alternativo":
        crspg= indie
    elif g=="kpop" or g=="k-pop":
        crspg=kpop
    elif g=="ska":
        crspg=ska
    elif g=="balada" or g=="baladas":
        crspg=balada
    
    if crspg is not None:
        recomendaciones=random.sample(crspg,min(3,len(crspg)))
        print(f"\n=====CANCIONES RECOMENDADAS (para el género {genero})=====")
        numr=1
        for reco in recomendaciones:
            print(f"{numr}. {reco}")
            numr+=1
    else:
        print("Lo sentimos, por el momento no tenemos recomendaciones predefinidas para este género en particular.")
        print("La buena noticia es que el género se guardó con éxito")


def mostrar():
    try:
        print("\n===Lista de reproduccion===\n")
        with open(RUTA_JSON,"r") as archivo:
            datospl=json.load(archivo)
            canc=datospl["canciones"]
            arti=datospl["artistas"]
            gener=datospl["generos"]
            for i in range(len(canc)):
                print(f"{i+1}. {canc[i]} de {arti[i]}. La canción se caracteriza por ser del género {gener[i]}")
                
    except FileNotFoundError:
        print("La lista está vacía. Ingresa canciones a la playlist por favor.")

def buscar():
    encontrado=False
    busca=str(input("Ingrese el nombre de la cancion a buscar: "))
    for i in range(len(canciones)):
        if canciones[i]==busca:
            print(f"Cancion encontrada: {canciones[i]} - {artistas[i]}")
            encontrado=True
            break
        else:
            encontrado=False
    if encontrado==False:
        print("Canción no encontrada")

def eliminar():
    eliminado=False
    busca1=str(input("Ingrese el nombre de la cancion a eliminar: "))
    for i in range(len(canciones)):
        if canciones[i]==busca1:
            print(f"Cancion eliminada: {canciones[i]} - {artistas[i]}")
            canciones.pop(i)
            artistas.pop(i)
            generos.pop(i)
            datospl={"canciones":canciones,"artistas":artistas,"generos":generos}
            with open (RUTA_JSON,"w") as archivo:
                json.dump(datospl,archivo,indent=4)
            eliminado=True
            break
        else:
            eliminado=False
    if eliminado==False:
        print("Canción no encontrada. Por lo tanto no se eliminó")