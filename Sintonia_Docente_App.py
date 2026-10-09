import streamlit as st
import os
import json

# Configuración de la página
st.set_page_config(
    page_title="Sintonía Docente - Ecosistema de Resignificación Docente",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Personalizados:
# 1. Fondo de pared de ladrillos estilo Stand-up / Escenario
# 2. Título principal en fuente 'Freestyle Script' verde neón
# 3. Menú desplegable (selectbox) con texto negro en negrita
# 4. Estructura en 2 cajitas independientes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Freestyle+Script&family=Caveat:wght@700&family=Permanent+Marker&family=Sedgwick+Ave&display=swap');

    .stApp {
        background-color: #0d0d0d !important;
        background-image: 
            linear-gradient(rgba(13, 13, 13, 0.82), rgba(13, 13, 13, 0.90)),
            radial-gradient(circle at 50% 20%, rgba(57, 255, 20, 0.15) 0%, transparent 60%),
            repeating-linear-gradient(0deg, transparent, transparent 19px, rgba(255, 255, 255, 0.05) 20px),
            repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(255, 255, 255, 0.05) 40px),
            linear-gradient(90deg, #1c1310 0%, #2b1d18 25%, #1f1411 50%, #2c1b16 75%, #180f0c 100%) !important;
        background-attachment: fixed !important;
        color: #F0F4F8 !important;
        font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    [data-testid="stSidebar"] {
        background-color: #12161f !important;
        background-image: linear-gradient(180deg, #151c28 0%, #0d121c 100%) !important;
        border-right: 2px solid #39FF14 !important;
        box-shadow: 2px 0 18px rgba(57, 255, 20, 0.2);
    }
    [data-testid="stSidebar"] * {
        color: #F0F4F8 !important;
    }

    /* MENÚ DESPLEGABLE (SELECTBOX): Letra Negra #000000 en negrita */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
        border: 2px solid #39FF14 !important;
        box-shadow: 0 0 10px rgba(57, 255, 20, 0.3);
    }
    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 800 !important;
    }
    div[data-baseweb="select"] span {
        color: #000000 !important;
    }
    div[data-baseweb="popover"] {
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="popover"] * {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }
    ul[role="listbox"] {
        background-color: #FFFFFF !important;
    }
    ul[role="listbox"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }
    ul[role="listbox"] li:hover {
        background-color: #39FF14 !important;
        color: #000000 !important;
    }

    /* TÍTULO PRINCIPAL EN FREESTYLE SCRIPT */
    .title-graffiti {
        font-family: 'Freestyle Script', 'Sedgwick Ave', 'Caveat', cursive, sans-serif !important;
        font-size: 3.8em !important;
        font-weight: 400 !important;
        color: #39FF14 !important;
        text-shadow: 0 0 8px rgba(57, 255, 20, 0.6), 0 0 18px rgba(57, 255, 20, 0.4), 2px 2px 4px #000000 !important;
        text-align: center !important;
        margin-top: -10px !important;
        margin-bottom: 2px !important;
        letter-spacing: 1px !important;
    }

    .subtitle-neon {
        font-size: 1.05em;
        color: #FF007F;
        text-shadow: 0 0 8px rgba(255, 0, 127, 0.5);
        text-align: center;
        font-weight: 600;
        margin-bottom: 22px;
    }

    /* CAJITAS INDEPENDIENTES PARA VIVENCIA Y ESTRATEGIA */
    .box-vivencia {
        background-color: #0f172a;
        border-radius: 14px;
        padding: 20px;
        border: 2px solid #00F0FF;
        box-shadow: 0 4px 15px rgba(0, 240, 255, 0.2);
        height: 100%;
    }

    .box-estrategia {
        background-color: #0f2419;
        border-radius: 14px;
        padding: 20px;
        border: 2px solid #39FF14;
        box-shadow: 0 4px 15px rgba(57, 255, 20, 0.2);
        height: 100%;
    }

    .box-title-vivencia {
        color: #00F0FF;
        font-size: 1.25em;
        font-weight: 800;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
        text-shadow: 0 0 6px rgba(0, 240, 255, 0.4);
    }

    .box-title-estrategia {
        color: #39FF14;
        font-size: 1.25em;
        font-weight: 800;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
        text-shadow: 0 0 6px rgba(57, 255, 20, 0.4);
    }

    .box-body {
        color: #F0F4F8;
        font-size: 1.03em;
        line-height: 1.65;
    }

    /* ENCABEZADO DE ÁLBUM */
    .album-header-1 {
        background: linear-gradient(135deg, #092235 0%, #113854 100%);
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 2px solid #00F0FF;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.3);
    }
    
    .album-header-2 {
        background: linear-gradient(135deg, #350922 0%, #541138 100%);
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 2px solid #FF007F;
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# PISTAS DE LA INVESTIGACIÓN (19 FICHAS ANOMIZADAS)
PISTAS_EMBEDDED = [
    {
        "doc_id": "DOC-01",
        "pista_num": "01",
        "titulo_full": "Pista 01",
        "titulo": "Pista 01",
        "titulo_corto": "Pista 01",
        "area": "Francés y Lenguas Extranjeras",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "En medio del aislamiento y la timidez inicial de hablar en pantalla, surgió un ejercicio de escritura en el que los estudiantes pudieron expresar de forma sincera sus temores y emociones sin temor al qué dirán. La profe descubrió que el lenguaje es, ante todo, un puente para conectarse con la vida de los muchachos.",
        "estrategia": "Proponer actividades reales y vivenciales en lengua extranjera: los alumnos describen su ropa favorita, objetos significativos de su habitación o lugares de su casa mediante dinámicas de participación cercana y respetuosa.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-02",
        "pista_num": "02",
        "titulo_full": "Pista 02",
        "titulo": "Pista 02",
        "titulo_corto": "Pista 02",
        "area": "Inglés (Educación Infantil y Primaria)",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "Al enseñar a niños pequeños durante el encierro, el profe utilizó Paint a pulso para simular los renglones del cuaderno y guiar los trazos con el mouse. Además, en fechas especiales organizó retos con objetos cotidianos de la casa, demostrando que el afecto y la creatividad mantienen vivo el entusiasmo de los niños.",
        "estrategia": "Aprovechar la lúdica y los objetos de la vida diaria: organizar búsquedas del tesoro en casa o en el salón, juegos de asociación visual con dibujos sencillos y dinámicas corporales para afianzar el vocabulario básico.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-03",
        "pista_num": "03",
        "titulo_full": "Pista 03",
        "titulo": "Pista 03",
        "titulo_corto": "Pista 03",
        "area": "Cátedra de Educación Emocional / Filosofía y Humanidades",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La docente comprendió que en momentos de incertidumbre enseñar no es acumular contenidos, sino acompañar al ser humano. Recordó con cariño cómo los niños crearon tarjetas digitales dibujadas por ellos mismos para expresar su gratitud, demostrando que el vínculo afectivo es el verdadero motor del aprendizaje.",
        "estrategia": "Iniciar las jornadas con un 'círculo de la palabra' o pausa de conexión emocional: dedicar los primeros 10 minutos a escuchar cómo se sienten los estudiantes, usando preguntas socráticas sencillas y reflexivas.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-04",
        "pista_num": "04",
        "titulo_full": "Pista 04",
        "titulo": "Pista 04",
        "titulo_corto": "Pista 04",
        "area": "Educación Inicial y Preescolar",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "Con niños de preescolar, la profe transformó la rutina guiando las actividades paso a paso con imágenes sencillas y diapositivas coloridas. Descubrió que coordinarse con las familias y mantener la ternura en cada instrucción era la clave para que los más pequeños se sintieran seguros y motivados.",
        "estrategia": "Estructurar secuencias visuales claras y cortas: combinar adivinanzas, pausas musicales y guías visuales sencillas para la familia, asegurando que cada niño avance a su propio ritmo sin saturarse.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-05",
        "pista_num": "05",
        "titulo_full": "Pista 05",
        "titulo": "Pista 05",
        "titulo_corto": "Pista 05",
        "area": "Ciencias Sociales y Desarrollo Humano (Primaria)",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La docente dio el salto de la clase magistral tradicional al uso de relatos y presentaciones participativas. Recordó con emoción cómo las familias escuchaban sus clases de fondo y cómo pequeños detalles espontáneos permitieron romper la frialdad y acercar la historia a la vida real de sus estudiantes.",
        "estrategia": "Transformar los contenidos teóricos en historias cercanas: utilizar casos cotidianos, imágenes icónicas y preguntas problematizadoras que inviten a los alumnos a dar su opinión y relacionar el tema con su entorno.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-06",
        "pista_num": "06",
        "titulo_full": "Pista 06",
        "titulo": "Pista 06",
        "titulo_corto": "Pista 06",
        "area": "Educación Física, Recreación y Deporte",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "El profesor enfrentó el enorme reto de adaptar la actividad física a espacios reducidos. Con ingenio, utilizó implementos de aseo, elementos del hogar y música motivadora para mantener a los estudiantes activos y saludables, demostrando que el movimiento es bienestar mental.",
        "estrategia": "Diseñar circuitos motrices dinámicos con elementos caseros o del aula: organizar rutinas de ejercicios de bajo impacto, pausas activas y juegos de coordinación usando botellas plásticas, escobas o marcadores.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-07",
        "pista_num": "07",
        "titulo_full": "Pista 07",
        "titulo": "Pista 07",
        "titulo_corto": "Pista 07",
        "area": "Física y Ciencias Exactas",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "El docente descubrió que al explicar temas complejos como la física, ver a los abuelos y padres sentados al lado de los niños aprendiendo juntos enriquecía el proceso. Perdió el miedo a las herramientas digitales y comenzó a grabar explicaciones breves con pizarras visuales.",
        "estrategia": "Utilizar la indagación guiada con simuladores y experimentos simples: plantear preguntas problema cotidianas (como el movimiento de una bicicleta o el calor de una taza) para explorar los conceptos antes de la fórmula.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-08",
        "pista_num": "08",
        "titulo_full": "Pista 08",
        "titulo": "Pista 08",
        "titulo_corto": "Pista 08",
        "area": "Educación Infantil y Dimensión Afectiva",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La maestra comprendió la importancia de la empatía y el buen humor en el aula. Usó historias vivas, fondos animados y cuentos interactivos para mantener la chispa del aprendizaje en los niños, aprendiendo que la tecnología debe sumar calidez y no distancia.",
        "estrategia": "Implementar dinámicas de ludificación y cuentos expresivos: intercalar momentos de lectura compartida con pausas de expresión gestual y artística que mantengan la alegría en el salón de clase.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-09",
        "pista_num": "09",
        "titulo_full": "Pista 09",
        "titulo": "Pista 09",
        "titulo_corto": "Pista 09",
        "area": "Español y Lengua Castellana",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Tras el exceso de pantallas, la profesora decidió hacer una pausa consciente y regresar a lo análogo y manipulativo: recortar, armar, escribir a mano y tocar el papel. Redescubrió que la lectura crítica y la escritura creativa se disfrutan más cuando se sienten en las manos.",
        "estrategia": "Alternar el trabajo digital con talleres análogos y manipulativos: crear diarios de lectura en papel, murales físicos de palabras y álbumes ilustrados hechos a mano por los mismos alumnos.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-10",
        "pista_num": "10",
        "titulo_full": "Pista 10",
        "titulo": "Pista 10",
        "titulo_corto": "Pista 10",
        "area": "Ciencias Naturales y Biología",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profesor no dejó morir la curiosidad científica y creó la estrategia de 'El laboratorio en mi cocina'. Con ingredientes caseros como repollo morado, vinagre y bicarbonato, demostró que la ciencia está viva en cualquier rincón del hogar.",
        "estrategia": "Diseñar laboratorios caseros e indagar la naturaleza cercana: proponer pequeñas observaciones científicas con elementos cotidianos para que los estudiantes formulen hipótesis y experimenten sin peligro.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-11",
        "pista_num": "11",
        "titulo_full": "Pista 11",
        "titulo": "Pista 11",
        "titulo_corto": "Pista 11",
        "area": "Matemáticas en Primaria (1° a 3°)",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente utilizó ruletas virtuales, juegos con semillas y desafíos de tienda escolar para que los niños de primaria perdieran el miedo a los números. Comprendió que cuando las matemáticas se juegan y se tocan, el aprendizaje perdura.",
        "estrategia": "Gamificar el pensamiento numérico con material concreto: organizar retos de cálculo mental rápido usando fichas, juegos de mercado escolar y tableros interactivos sencillos.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-12",
        "pista_num": "12",
        "titulo_full": "Pista 12",
        "titulo": "Pista 12",
        "titulo_corto": "Pista 12",
        "area": "Ciencias Sociales e Historia / Bilingüismo",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La profesora organizó momentos humanos memorables, como celebrar cumpleaños a través de las pantallas o debatir noticias actuales. Aprendió a sintetizar los contenidos en presentaciones breves para dar más tiempo a la conversación rica entre estudiantes.",
        "estrategia": "Implementar cuadros comparativos y análisis de casos reales: utilizar diapositivas breves para presentar ideas clave y abrir de inmediato espacio para el debate de opinión y la reflexión en grupos.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-13",
        "pista_num": "13",
        "titulo_full": "Pista 13",
        "titulo": "Pista 13",
        "titulo_corto": "Pista 13",
        "area": "Tecnología e Informática",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profe tomó la decisión humanizada de priorizar la sustentación oral y la lógica de los alumnos por encima de exigir cámaras encendidas a quienes tenían mala conexión. Enseñó que la tecnología debe estar al servicio de las personas y no al revés.",
        "estrategia": "Desarrollar el pensamiento computacional sin pantallas (actividades *unplugged*): usar juegos de lógica con tarjetas, instrucciones paso a paso humanas y diálogos donde el alumno explique cómo solucionó un problema.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-14",
        "pista_num": "14",
        "titulo_full": "Pista 14",
        "titulo": "Pista 14",
        "titulo_corto": "Pista 14",
        "area": "Coordinación Académica y Pedagogía Infantil",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente utilizó Paint como su tablero digital hecho a mano para explicar a su manera. Como directiva, construyó acuerdos de paciencia y confianza con los maestros y familias, recordando que la gestión educativa debe ser siempre cercana y comprensiva.",
        "estrategia": "Construir decálogos de convivencia y acuerdos claros de aula: establecer pautas amables para la escucha activa, la participación organizada y el uso con sentido de las herramientas digitales.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-15",
        "pista_num": "15",
        "titulo_full": "Pista 15",
        "titulo": "Pista 15",
        "titulo_corto": "Pista 15",
        "area": "Lengua Castellana y Proceso Lecto-Escritor",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "En los grados iniciales, la maestra estableció rutinas claras de escucha y normas sencillas para tomar la palabra. Descubrió que al combinar la lectura de cuentos con presentaciones sencillas, los niños fortalecieron enormemente su expresión verbal.",
        "estrategia": "Evaluar mediante sustentación oral y diálogo guiado: hacer preguntas cortas al final de las lecturas para que los alumnos cuenten con sus propias palabras lo que entendieron y compartan sus reflexiones.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-16",
        "pista_num": "16",
        "titulo_full": "Pista 16",
        "titulo": "Pista 16",
        "titulo_corto": "Pista 16",
        "area": "Ciencias Sociales y Ciencia Política",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Un estudiante tímido que casi no hablaba en clase presencial comenzó a escribir largos mensajes en el chat para compartir reflexiones muy profundas. La profesora descubrió que la tecnología abrió puertas a nuevas formas de expresión para quienes antes callaban.",
        "estrategia": "Aprovechar espacios de participación escrita y foros de opinión: combinar el diálogo en clase con pequeños muros colaborativos digitales donde los estudiantes respondan preguntas breves a su ritmo.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-17",
        "pista_num": "17",
        "titulo_full": "Pista 17",
        "titulo": "Pista 17",
        "titulo_corto": "Pista 17",
        "area": "Matemáticas y Física (Innovación y Humor)",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profesor decidió institucionalizar los últimos 5 minutos de su clase como 'el receso de chistes'. Usó la risa y el buen humor como la mejor estrategia para liberar el estrés, conectar con los jóvenes y hacer amables las materias más exigentes.",
        "estrategia": "Incorporar pausas de humor y acertijos lógicos en clase: usar juegos de palabras, adivinanzas numéricas o pequeños chistes al final de temas complejos para mantener un ambiente de aula relajado y motivante.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-18",
        "pista_num": "18",
        "titulo_full": "Pista 18",
        "titulo": "Pista 18",
        "titulo_corto": "Pista 18",
        "area": "Educación Artística y Plástica",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente aprovechó la tecnología para llevar a sus estudiantes a recorridos virtuales por más de 80 museos del mundo desde la pantalla. Luego, los guió para recrear las obras de arte con pintura, cartón y materiales reciclables de su propia casa.",
        "estrategia": "Conectar la exploración estética digital con la creación plástica manual: mostrar imágenes o videos breves de obras famosas y proponer retos de creación con materiales reciclables que los alumnos tengan a la mano.",
        "prompt": ""
    },
    {
        "doc_id": "DOC-19",
        "pista_num": "19",
        "titulo_full": "Pista 19",
        "titulo": "Pista 19",
        "titulo_corto": "Pista 19",
        "area": "Inglés y Ciencias en Educación Infantil",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Para captar la atención de los más pequeños, la profe creó a 'Mr. Whiskers', un gatito títere que solo hablaba inglés. Además, animó con herramientas sencillas los dibujos de los niños, llenándolos de orgullo y ganas de participar.",
        "estrategia": "Usar personajes guiados y proyectos creativos animados: incorporar un títere o personaje simbólico para hacer preguntas curiosas e interactuar con los alumnos en idiomas o ciencias.",
        "prompt": ""
    }
]

def buscar_audio_robusto(doc_code, pista_num):
    """Buscador automático universal de audios en cualquier carpeta y formato"""
    doc_num = str(int(pista_num)) if str(pista_num).isdigit() else str(pista_num)
    pista_z = f"{int(doc_num):02d}" if doc_num.isdigit() else doc_num
    
    rutas_directas = [
        f"sintonia_docente/{doc_code}.mp3",
        f"sintonia_docente/{doc_code}.wav",
        f"sintonia_docente/{doc_code}.ogg",
        f"sintonia_docente/{doc_code}.mp4",
        f"sintonia_docente/Pista_{pista_z}.mp3",
        f"sintonia_docente/pista_{pista_z}.ogg",
        f"sintonia_docente/pista_{pista_z}.mp4",
        f"sintonia_docente/Pista {pista_z}.mp3",
        f"sintonia_docente/{pista_z}.mp3",
        f"sintonia_docente/{pista_z}.ogg",
        f"audio/{doc_code}.mp3",
        f"{doc_code}.mp3",
        f"pista_{pista_z}.ogg",
        f"pista_{pista_z}.mp4",
        f"pista_{pista_z}.mp3"
    ]
    
    for r in rutas_directas:
        if os.path.exists(r):
            return r
            
    # Búsqueda escaneando carpetas
    for folder in ["sintonia_docente", "audio", "."]:
        if os.path.exists(folder):
            try:
                for fname in sorted(os.listdir(folder)):
                    fn_lower = fname.lower()
                    if fn_lower.endswith((".mp3", ".wav", ".m4a", ".ogg", ".mp4")):
                        if (doc_code.lower() in fn_lower or 
                            f"pista_{pista_z}" in fn_lower or 
                            f"pista {pista_z}" in fn_lower or
                            fn_lower.startswith(f"pista_{pista_z}") or
                            fn_lower.startswith(f"{pista_z}.")):
                            return os.path.join(folder, fname)
            except Exception:
                pass
    return None

pistas = PISTAS_EMBEDDED

# ENCABEZADO PRINCIPAL
st.markdown('<div class="title-graffiti">🎧 Sintonía Docente</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-neon">Ecosistema de Resignificación Docente • Universidad de Nariño</div>', unsafe_allow_html=True)

# BARRA LATERAL (SIDEBAR)
st.sidebar.markdown("<h2 style='color:#39FF14; font-family:Freestyle Script, cursive, sans-serif; font-size:2.5em; text-align:center;'>🎙️ Sintonía Docente</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#E0E0E0; font-style:italic; text-align:center;'>Ecosistema de Resignificación</p>", unsafe_allow_html=True)
st.sidebar.divider()

modo_vista = st.sidebar.radio(
    "📌 Selecciona la Colección:",
    ["Álbum 1: El Latido en el Silencio (DOC-01 a DOC-08)", 
     "Álbum 2: La Alquimia Pedagógica (DOC-09 a DOC-19)", 
     "Ver Todas las 19 Fichas Pedagógicas"]
)

if "Álbum 1" in modo_vista:
    pistas_filtradas = [p for p in pistas if p.get("album") == "Álbum 1: El Latido en el Silencio"]
elif "Álbum 2" in modo_vista:
    pistas_filtradas = [p for p in pistas if p.get("album") == "Álbum 2: La Alquimia Pedagógica"]
else:
    pistas_filtradas = pistas

opciones_titulos = [p["titulo"] for p in pistas_filtradas] if pistas_filtradas else ["Sin pistas disponibles"]

st.sidebar.markdown("<p style='color:#39FF14; font-weight:bold; margin-top:15px;'>🎵 Selecciona la Pista Sonora:</p>", unsafe_allow_html=True)

pista_seleccionada_titulo = st.sidebar.selectbox(
    "Despliega para elegir la pista:",
    opciones_titulos,
    index=0
)

pista_actual = next((p for p in pistas_filtradas if p["titulo"] == pista_seleccionada_titulo), pistas[0] if pistas else {})

tab_reproductor, tab_catalogo, tab_metodologia = st.tabs([
    "🎙️ Reproductor y Ficha Pedagógica", 
    "📚 Catálogo Completo (19 Fichas)", 
    "ℹ️ Acerca del Ecosistema"
])

with tab_reproductor:
    if pista_actual:
        if pista_actual.get("album") == "Álbum 1: El Latido en el Silencio":
            header_class = "album-header-1"
            album_color = "#00F0FF"
        else:
            header_class = "album-header-2"
            album_color = "#FF007F"
            
        st.markdown(f"""
        <div class="{header_class}">
            <span style="background-color:{album_color}; color:#000000; font-weight:bold; padding:4px 12px; border-radius:12px; font-size:0.85em;">{pista_actual.get('album', '')}</span>
            <h2 style="color:#FFFFFF; margin-top:10px; margin-bottom:5px; text-shadow:0 0 10px {album_color};">{pista_actual.get('titulo', '')}</h2>
            <p style="color:#E0E0E0; font-size:1.05em; margin:0;">📚 <b>Área Curricular:</b> {pista_actual.get('area', '')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#39FF14; margin-bottom:12px;'>🎙️ Reproductor de Voz y Sonido:</h4>", unsafe_allow_html=True)
        
        doc_code = pista_actual.get("doc_id", "DOC-01")
        pista_num = pista_actual.get("pista_num", "01")
        
        audio_encontrado = buscar_audio_robusto(doc_code, pista_num)
        
        if audio_encontrado:
            st.audio(audio_encontrado)
        else:
            st.info(f"🎧 **Audio detectado:** Al colocar la carpeta `sintonia_docente` con los archivos MP3 (`{doc_code}.mp3`), este reproductor los cargará automáticamente.")

        st.markdown("<br>", unsafe_allow_html=True)
        
        # ESTRUCTURA EN 2 CAJITAS INDEPENDIENTES (PARALELAS LADO A LADO)
        col_viv, col_est = st.columns(2, gap="medium")
        
        with col_viv:
            st.markdown(f"""
            <div class="box-vivencia">
                <div class="box-title-vivencia">💬 Vivencia del Profe:</div>
                <div class="box-body">{pista_actual.get('vivencia', '')}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col_est:
            st.markdown(f"""
            <div class="box-estrategia">
                <div class="box-title-estrategia">💡 Estrategia de Aula Replicable:</div>
                <div class="box-body">{pista_actual.get('estrategia', '')}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # UN SOLO PROMPT UNIFICADO ABAJO
        st.markdown("<h4 style='color:#FF007F; margin-bottom:8px;'>🤖 Prompt de Inteligencia Artificial Sugerido (Listo para usar):</h4>", unsafe_allow_html=True)
        st.code(pista_actual.get("prompt", ""), language="markdown")

with tab_catalogo:
    st.markdown("<h3 style='color:#00F0FF;'>📚 Compendio de las 19 Fichas Pedagógicas de la Investigación</h3>", unsafe_allow_html=True)
    st.write("Explora de forma directa las vivencias, estrategias y prompts desarrollados a partir de las narrativas de los docentes de Popayán (DOC-01 a DOC-19).")
    
    search_term = st.text_input("🔍 Buscar por palabra clave (ej. inglés, matemáticas, inicial, títere, juego):", "")
    
    for p in pistas:
        if not search_term or search_term.lower() in p["titulo"].lower() or search_term.lower() in p["area"].lower() or search_term.lower() in p["vivencia"].lower():
            with st.expander(f"🔹 {p['doc_id']} — {p['titulo_corto']} | 📚 {p['area']}"):
                st.markdown(f"**Área:** {p['area']}")
                st.markdown(f"**Vivencia del Profe:** {p['vivencia']}")
                st.markdown(f"**Estrategia de Aula:** {p['estrategia']}")
                st.markdown("**Prompt de IA Sugerido:**")
                st.code(p['prompt'], language="markdown")

with tab_metodologia:
    st.markdown("<h3 style='color:#00F0FF;'>ℹ️ Sobre el Ecosistema 'Sintonía Docente'</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Investigación:** SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA  
    **Investigadora:** Catalina Díaz Chíquiza  
    **Asesora:** Mg. Lady Johana Gómez Bernal  
    **Institución:** Universidad de Nariño — Maestría en Educación Virtual (e-MEV)  

    ---

    ### 🎯 Objetivo del Ecosistema (Objetivo Específico 3):
    El producto comunicativo *Sintonía Docente* ha sido co-construido como una herramienta multimodal y de acceso libre para la comunidad educadora. Cada ficha integra la memoria viva de la pandemia con estrategias didácticas y *prompts* de Inteligencia Artificial diseñados para enriquecer la labor docente actual en entornos presenciales, híbridos y virtuales.

    **Nota Ética:** La totalidad de los relatos ha sido anonimizada bajo la codificación de **DOC-01 a DOC-19** para resguardar la identidad de los maestros participantes de las instituciones educativas privadas de Popayán.
    """)
