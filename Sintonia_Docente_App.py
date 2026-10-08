import streamlit as st
import os
import json

# Configuración de la página
st.set_page_config(
    page_title="Sintonía Docente - Ecosistema Transmedia",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Datos de los 19 relatos pedagógicos
pistas = [
  {
    "doc_id": "DOC-01",
    "pista_num": "01",
    "titulo_full": "Pista 01: Las Voces Anónimas del Corazón",
    "titulo_corto": "Las Voces Anónimas del Corazón",
    "area": "Francés y Lenguas Extranjeras",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "En medio del aislamiento y la timidez inicial de hablar en pantalla, surgió un ejercicio de escritura en el que los estudiantes pudieron expresar de forma sincera sus temores y emociones sin temor al qué dirán. La profe descubrió que el lenguaje es, ante todo, un puente para conectarse con la vida de los muchachos.",
    "estrategia": "Proponer actividades reales y vivenciales en lengua extranjera: los alumnos describen su ropa favorita, objetos significativos de su habitación o lugares de su casa mediante dinámicas de participación cercana y respetuosa.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-02",
    "pista_num": "02",
    "titulo_full": "Pista 02: Enseñar es Acompañar",
    "titulo_corto": "Enseñar es Acompañar",
    "area": "Inglés (Educación Infantil y Primaria)",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "Al enseñar a niños pequeños durante el encierro, el profe utilizó Paint a pulso para simular los renglones del cuaderno y guiar los trazos con el mouse. Además, en fechas especiales organizó retos con objetos cotidianos de la casa, demostrando que el afecto y la creatividad mantienen vivo el entusiasmo de los niños.",
    "estrategia": "Aprovechar la lúdica y los objetos de la vida diaria: organizar búsquedas del tesoro en casa o en el salón, juegos de asociación visual con dibujos sencillos y dinámicas corporales para afianzar el vocabulario básico.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-03",
    "pista_num": "03",
    "titulo_full": "Pista 03: Tarjetas de Afecto en la Pantalla",
    "titulo_corto": "Tarjetas de Afecto en la Pantalla",
    "area": "Cátedra de Educación Emocional / Filosofía y Humanidades",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "La docente comprendió que en momentos de incertidumbre enseñar no es acumular contenidos, sino acompañar al ser humano. Recordó con cariño cómo los niños crearon tarjetas digitales dibujadas por ellos mismos para expresar su gratitud, demostrando que el vínculo afectivo es el verdadero motor del aprendizaje.",
    "estrategia": "Iniciar las jornadas con un 'círculo de la palabra' o pausa de conexión emocional: dedicar los primeros 10 minutos a escuchar cómo se sienten los estudiantes, usando preguntas socráticas sencillas y reflexivas.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-04",
    "pista_num": "04",
    "titulo_full": "Pista 04: Ventanas Abiertas a la Cotidianidad",
    "titulo_corto": "Ventanas Abiertas a la Cotidianidad",
    "area": "Educación Inicial y Preescolar",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "Con niños de preescolar, la profe transformó la rutina guiando las actividades paso a paso con imágenes sencillas y diapositivas coloridas. Descubrió que coordinarse con las familias y mantener la ternura en cada instrucción era la clave para que los más pequeños se sintieran seguros y motivados.",
    "estrategia": "Estructurar secuencias visuales claras y cortas: combinar adivinanzas, pausas musicales y guías visuales sencillas para la familia, asegurando que cada niño avance a su propio ritmo sin saturarse.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-05",
    "pista_num": "05",
    "titulo_full": "Pista 05: El Visitante Inesperado",
    "titulo_corto": "El Visitante Inesperado",
    "area": "Ciencias Sociales y Desarrollo Humano (Primaria)",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "La docente dio el salto de la clase magistral tradicional al uso de relatos y presentaciones participativas. Recordó con emoción cómo las familias escuchaban sus clases de fondo y cómo pequeños detalles espontáneos permitieron romper la frialdad y acercar la historia a la vida real de sus estudiantes.",
    "estrategia": "Transformar los contenidos teóricos en historias cercanas: utilizar casos cotidianos, imágenes icónicas y preguntas problematizadoras que inviten a los alumnos a dar su opinión y relacionar el tema con su entorno.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-06",
    "pista_num": "06",
    "titulo_full": "Pista 06: Cumpleaños en Comunidad",
    "titulo_corto": "Cumpleaños en Comunidad",
    "area": "Educación Física, Recreación y Deporte",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "El profesor enfrentó el enorme reto de adaptar la actividad física a espacios reducidos. Con ingenio, utilizó implementos de aseo, elementos del hogar y música motivadora para mantener a los estudiantes activos y saludables, demostrando que el movimiento es bienestar mental.",
    "estrategia": "Diseñar circuitos motrices dinámicos con elementos caseros o del aula: organizar rutinas de ejercicios de bajo impacto, pausas activas y juegos de coordinación usando botellas plásticas, escobas o marcadores.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-07",
    "pista_num": "07",
    "titulo_full": "Pista 07: La Mirada Incompleta",
    "titulo_corto": "La Mirada Incompleta",
    "area": "Física y Ciencias Exactas",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "El docente descubrió que al explicar temas complejos como la física, ver a los abuelos y padres sentados al lado de los niños aprendiendo juntos enriquecía el proceso. Perdió el miedo a las herramientas digitales y comenzó a grabar explicaciones breves con pizarras visuales.",
    "estrategia": "Utilizar la indagación guiada con simuladores y experimentos simples: plantear preguntas problema cotidianas (como el movimiento de una bicicleta o el calor de una taza) para explorar los conceptos antes de la fórmula.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-08",
    "pista_num": "08",
    "titulo_full": "Pista 08: El Refugio del Chat",
    "titulo_corto": "El Refugio del Chat",
    "area": "Educación Infantil y Dimensión Afectiva",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "La maestra comprendió la importancia de la empatía y el buen humor en el aula. Usó historias vivas, fondos animados y cuentos interactivos para mantener la chispa del aprendizaje en los niños, aprendiendo que la tecnología debe sumar calidez y no distancia.",
    "estrategia": "Implementar dinámicas de ludificación y cuentos expresivos: intercalar momentos de lectura compartida con pausas de expresión gestual y artística que mantengan la alegría en el salón de clase.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-09",
    "pista_num": "09",
    "titulo_full": "Pista 09: Dibujar el Alfabeto a Pulso",
    "titulo_corto": "Dibujar el Alfabeto a Pulso",
    "area": "Español y Lengua Castellana",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "Tras el exceso de pantallas, la profesora decidió hacer una pausa consciente y regresar a lo análogo y manipulativo: recortar, armar, escribir a mano y tocar el papel. Redescubrió que la lectura crítica y la escritura creativa se disfrutan más cuando se sienten en las manos.",
    "estrategia": "Alternar el trabajo digital con talleres análogos y manipulativos: crear diarios de lectura en papel, murales físicos de palabras y álbumes ilustrados hechos a mano por los mismos alumnos.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-10",
    "pista_num": "10",
    "titulo_full": "Pista 10: La Metamorfosis de la Voz",
    "titulo_corto": "La Metamorfosis de la Voz",
    "area": "Ciencias Naturales y Biología",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "El profesor no dejó morir la curiosidad científica y creó la estrategia de 'El laboratorio en mi cocina'. Con ingredientes caseros como repollo morado, vinagre y bicarbonato, demostró que la ciencia está viva en cualquier rincón del hogar.",
    "estrategia": "Diseñar laboratorios caseros e indagar la naturaleza cercana: proponer pequeñas observaciones científicas con elementos cotidianos para que los estudiantes formulen hipótesis y experimenten sin peligro.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-11",
    "pista_num": "11",
    "titulo_full": "Pista 11: El Gimnasio de los Objetos Olvidados",
    "titulo_corto": "El Gimnasio de los Objetos Olvidados",
    "area": "Matemáticas en Primaria (1° a 3°)",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "La docente utilizó ruletas virtuales, juegos con semillas y desafíos de tienda escolar para que los niños de primaria perdieran el miedo a los números. Comprendió que cuando las matemáticas se juegan y se tocan, el aprendizaje perdura.",
    "estrategia": "Gamificar el pensamiento numérico con material concreto: organizar retos de cálculo mental rápido usando fichas, juegos de mercado escolar y tableros interactivos sencillos.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-12",
    "pista_num": "12",
    "titulo_full": "Pista 12: El Aula de Tres Generaciones",
    "titulo_corto": "El Aula de Tres Generaciones",
    "area": "Ciencias Sociales e Historia / Bilingüismo",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "La profesora organizó momentos humanos memorables, como celebrar cumpleaños a través de las pantallas o debatir noticias actuales. Aprendió a sintetizar los contenidos en presentaciones breves para dar más tiempo a la conversación rica entre estudiantes.",
    "estrategia": "Implementar cuadros comparativos y análisis de casos reales: utilizar diapositivas breves para presentar ideas clave y abrir de inmediato espacio para el debate de opinión y la reflexión en grupos.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-13",
    "pista_num": "13",
    "titulo_full": "Pista 13: La Pedagogía del Equilibrio",
    "titulo_corto": "La Pedagogía del Equilibrio",
    "area": "Tecnología e Informática",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "El profe tomó la decisión humanizada de priorizar la sustentación oral y la lógica de los alumnos por encima de exigir cámaras encendidas a quienes tenían mala conexión. Enseñó que la tecnología debe estar al servicio de las personas y no al revés.",
    "estrategia": "Desarrollar el pensamiento computacional sin pantallas (actividades *unplugged*): usar juegos de lógica con tarjetas, instrucciones paso a paso humanas y diálogos donde el alumno explique cómo solucionó un problema.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-14",
    "pista_num": "14",
    "titulo_full": "Pista 14: El Laboratorio en la Cocina",
    "titulo_corto": "El Laboratorio en la Cocina",
    "area": "Coordinación Académica y Pedagogía Infantil",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "La docente utilizó Paint como su tablero digital hecho a mano para explicar a su manera. Como directiva, construyó acuerdos de paciencia y confianza con los maestros y familias, recordando que la gestión educativa debe ser siempre cercana y comprensiva.",
    "estrategia": "Construir decálogos de convivencia y acuerdos claros de aula: establecer pautas amables para la escucha activa, la participación organizada y el uso con sentido de las herramientas digitales.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-15",
    "pista_num": "15",
    "titulo_full": "Pista 15: La Palabra sobre la Imagen",
    "titulo_corto": "La Palabra sobre la Imagen",
    "area": "Lengua Castellana y Proceso Lecto-Escritor",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "En los grados iniciales, la maestra estableció rutinas claras de escucha y normas sencillas para tomar la palabra. Descubrió que al combinar la lectura de cuentos con presentaciones sencillas, los niños fortalecieron enormemente su expresión verbal.",
    "estrategia": "Evaluar mediante sustentación oral y diálogo guiado: hacer preguntas cortas al final de las lecturas para que los alumnos cuenten con sus propias palabras lo que entendieron y compartan sus reflexiones.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-16",
    "pista_num": "16",
    "titulo_full": "Pista 16: La Orquesta de los Micrófonos",
    "titulo_corto": "La Orquesta de los Micrófonos",
    "area": "Ciencias Sociales y Ciencia Política",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "Un estudiante tímido que casi no hablaba en clase presencial comenzó a escribir largos mensajes en el chat para compartir reflexiones muy profundas. La profesora descubrió que la tecnología abrió puertas a nuevas formas de expresión para quienes antes callaban.",
    "estrategia": "Aprovechar espacios de participación escrita y foros de opinión: combinar el diálogo en clase con pequeños muros colaborativos digitales donde los estudiantes respondan preguntas breves a su ritmo.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-17",
    "pista_num": "17",
    "titulo_full": "Pista 17: El Receso de los Chistes",
    "titulo_corto": "El Receso de los Chistes",
    "area": "Matemáticas y Física (Innovación y Humor)",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "El profesor decidió institucionalizar los últimos 5 minutos de su clase como 'el receso de chistes'. Usó la risa y el buen humor como la mejor estrategia para liberar el estrés, conectar con los jóvenes y hacer amables las materias más exigentes.",
    "estrategia": "Incorporar pausas de humor y acertijos lógicos en clase: usar juegos de palabras, adivinanzas numéricas o pequeños chistes al final de temas complejos para mantener un ambiente de aula relajado y motivante.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-18",
    "pista_num": "18",
    "titulo_full": "Pista 18: Museos sin Fronteras",
    "titulo_corto": "Museos sin Fronteras",
    "area": "Educación Artística y Plástica",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "La docente aprovechó la tecnología para llevar a sus estudiantes a recorridos virtuales por más de 80 museos del mundo desde la pantalla. Luego, los guió para recrear las obras de arte con pintura, cartón y materiales reciclables de su propia casa.",
    "estrategia": "Conectar la exploración estética digital con la creación plástica manual: mostrar imágenes o videos breves de obras famosas y proponer retos de creación con materiales reciclables que los alumnos tengan a la mano.",
    "prompt": ""
  },
  {
    "doc_id": "DOC-19",
    "pista_num": "19",
    "titulo_full": "Pista 19: El Títere que Aprendió a Enseñar",
    "titulo_corto": "El Títere que Aprendió a Enseñar",
    "area": "Inglés y Ciencias en Educación Infantil",
    "album": "Álbum 2: La Alquimia Pedagógica",
    "vivencia": "Para captar la atención de los más pequeños, la profe creó a 'Mr. Whiskers', un gatito títere que solo hablaba inglés. Además, animó con herramientas sencillas los dibujos de los niños, llenándolos de orgullo y ganas de participar.",
    "estrategia": "Usar personajes guiados y proyectos creativos animados: incorporar un títere o personaje simbólico para hacer preguntas curiosas e interactuar con los alumnos en idiomas o ciencias.",
    "prompt": ""
  }
]

# Estilos CSS - Estética Escenario Stand-Up Comedy con Fondo de Ladrillo Oscuro y Neón Verde
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Great+Vibes&family=Pacifico&family=Satisfy&family=Montserrat:wght@400;600;800&display=swap');

    /* Fondo general estilo Escenario Stand-Up Comedy (Ladrillos en CSS puro + Foco Verde Neón) */
    .stApp {
        background-color: #0f080a !important;
        background-image: 
            radial-gradient(circle at 50% 18%, rgba(57, 255, 20, 0.20) 0%, rgba(15, 8, 10, 0.95) 75%),
            linear-gradient(335deg, rgba(0,0,0,0.85) 0%, rgba(20,10,12,0.9) 100%),
            repeating-linear-gradient(0deg, #1c0e12, #1c0e12 24px, #0a0406 25px, #0a0406 26px),
            repeating-linear-gradient(90deg, #1c0e12, #1c0e12 48px, #0a0406 49px, #0a0406 50px) !important;
        background-attachment: fixed !important;
        color: #FFFFFF !important;
        font-family: 'Montserrat', sans-serif;
    }

    /* Barra lateral estilo camerino de teatro */
    [data-testid="stSidebar"] {
        background-color: #12090b !important;
        background-image: linear-gradient(180deg, rgba(20, 10, 12, 0.98) 0%, rgba(10, 5, 6, 0.98) 100%) !important;
        border-right: 2px solid #39FF14 !important;
        box-shadow: 2px 0 15px rgba(57, 255, 20, 0.25) !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* FORZAR LETRA NEGRA Y FONDO CLARO EN EL SELECTBOX (MENÚ DESPLEGABLE) */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 2px solid #39FF14 !important;
    }
    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    div[data-baseweb="popover"] div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    ul[role="listbox"] li {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    /* TÍTULO PRINCIPAL - NEÓN VERDE Y LETRA CURSIVA ESTILIZADA DE ESCENARIO */
    .title-neon-green {
        font-family: 'Pacifico', 'Great Vibes', 'Satisfy', 'Caveat', cursive !important;
        font-size: 4.2em !important;
        color: #39FF14 !important;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 0px;
        text-shadow: 
            0 0 5px #39FF14,
            0 0 10px #39FF14,
            0 0 20px #39FF14,
            0 0 40px #00FF66,
            0 0 80px #00FF66;
        letter-spacing: 2px;
    }

    .subtitle-research {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.02em;
        font-weight: 700;
        color: #F1F5F9;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 25px;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }

    /* Tarjeta estilo Escenario / Stand-Up */
    .stage-card {
        background: rgba(22, 12, 15, 0.92);
        border: 1.5px solid rgba(57, 255, 20, 0.45);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 0 25px rgba(0, 0, 0, 0.85), 0 0 15px rgba(57, 255, 20, 0.2);
        margin-bottom: 20px;
    }

    /* Cajas de texto y prompts */
    .section-label {
        color: #39FF14;
        font-size: 1.1em;
        font-weight: 700;
        margin-top: 14px;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    .content-box {
        background-color: rgba(255, 255, 255, 0.07);
        border-left: 4px solid #39FF14;
        padding: 14px 18px;
        border-radius: 8px;
        color: #F8FAFC;
        font-size: 1.02em;
        line-height: 1.6;
    }

    .prompt-box-neon {
        background-color: rgba(57, 255, 20, 0.09);
        border: 1.5px solid #39FF14;
        border-radius: 12px;
        padding: 16px;
        color: #E2FCE0;
        box-shadow: 0 0 12px rgba(57, 255, 20, 0.22);
        font-size: 1.02em;
        line-height: 1.5;
    }

    .badge-code {
        background-color: #39FF14;
        color: #000000;
        font-weight: 800;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.9em;
        display: inline-block;
        margin-right: 8px;
    }

    .badge-area {
        background-color: rgba(255, 255, 255, 0.15);
        color: #FFFFFF;
        font-weight: 600;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.9em;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<div class="title-neon-green">🎙️ Sintonía Docente</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-research">SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA</div>', unsafe_allow_html=True)

# Barra Lateral (Sidebar)
st.sidebar.markdown("<h2 style='font-family: Pacifico, cursive; color:#39FF14; text-shadow:0 0 8px #39FF14;'>🎙️ Sintonía Docente</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#CBD5E1; font-style:italic;'>Ecosistema Transmedia de Resignificación</p>", unsafe_allow_html=True)
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

opciones_titulos = [p["titulo_full"] for p in pistas_filtradas] if pistas_filtradas else ["Sin pistas disponibles"]

st.sidebar.markdown("<p style='color:#39FF14; font-weight:bold; margin-top:15px;'>🎵 Selecciona el Relato Sonoro:</p>", unsafe_allow_html=True)

pista_seleccionada_titulo = st.sidebar.selectbox(
    "Despliega para elegir:",
    opciones_titulos,
    index=0
)

pista_actual = next((p for p in pistas_filtradas if p["titulo_full"] == pista_seleccionada_titulo), pistas[0] if pistas else {})

tab_reproductor, tab_catalogo, tab_metodologia = st.tabs([
    "🎙️ Escenario y Ficha Pedagógica", 
    "📚 Catálogo Completo (19 Fichas)", 
    "ℹ️ Acerca de la Investigación"
])

with tab_reproductor:
    if pista_actual:
        doc_code = pista_actual.get("doc_id", "DOC-01")
        pista_num = pista_actual.get("pista_num", "01")
        
        # Búsqueda exhaustiva de audios en múltiples nombres y extensiones
        posibles_rutas = [
            f"sintonia_docente/{doc_code}.mp3",
            f"sintonia_docente/{doc_code}.ogg",
            f"sintonia_docente/{doc_code}.wav",
            f"sintonia_docente/pista_{pista_num}.ogg",
            f"sintonia_docente/pista_{pista_num}.mp4",
            f"sintonia_docente/pista_{pista_num}.mp3",
            f"pista_{pista_num}.ogg",
            f"pista_{pista_num}.mp4",
            f"pista_{pista_num}.mp3",
            f"{doc_code}.mp3",
            f"{doc_code}.ogg"
        ]
        
        audio_encontrado = None
        for ruta in posibles_rutas:
            if os.path.exists(ruta):
                audio_encontrado = ruta
                break

        # Layout de 2 columnas (Lado a Lado): Izquierda -> Reproductor | Derecha -> Ficha & Prompt
        col_audio, col_ficha = st.columns([1, 1.2])

        with col_audio:
            st.markdown(f"""
            <div class="stage-card" style="text-align: center;">
                <span class="badge-code">{pista_actual.get("doc_id", "")}</span>
                <span class="badge-area">{pista_actual.get("album", "")}</span>
                <h2 style="color:#39FF14; margin-top:15px; margin-bottom:5px; font-family:'Montserrat', sans-serif; font-weight:800; text-shadow:0 0 10px rgba(57,255,20,0.5);">{pista_actual.get("titulo_full", "")}</h2>
                <p style="color:#E2E8F0; font-size:1.05em; margin-bottom:20px;">📚 <b>Área Curricular:</b> {pista_actual.get("area", "")}</p>
                <div style="font-size: 4.5em; margin: 15px 0;">🎙️</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<h4 style='color:#39FF14; margin-bottom:8px;'>🔊 Reproductor de Voz y Sonido:</h4>", unsafe_allow_html=True)
            if audio_encontrado:
                st.audio(audio_encontrado)
            else:
                st.info(f"🎧 **Audio preparado:** El reproductor reproducirá automáticamente el archivo (`pista_{pista_num}.ogg` / `{doc_code}.mp3`) una vez cargado.")

        with col_ficha:
            st.markdown(f"""
            <div class="stage-card">
                <div class="section-label">💬 Vivencia del Profe:</div>
                <div class="content-box">{pista_actual.get("vivencia", "")}</div>
                
                <div class="section-label">💡 Estrategia de Aula Replicable:</div>
                <div class="content-box">{pista_actual.get("estrategia", "")}</div>
                
                <div class="section-label">🤖 Prompt de Inteligencia Artificial Sugerido:</div>
                <div class="prompt-box-neon">{pista_actual.get("prompt", "")}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Copiar Prompt de IA:**")
            st.code(pista_actual.get("prompt", ""), language="markdown")

with tab_catalogo:
    st.markdown("<h3 style='color:#39FF14;'>📚 Compendio General de Fichas Pedagógicas (19 Relatos)</h3>", unsafe_allow_html=True)
    st.write("Explora las vivencias, estrategias de aula y prompts generativos co-construidos con los docentes participantes de Popayán.")
    
    search_term = st.text_input("🔍 Buscar por palabra clave (ej. inglés, matemáticas, inicial, títere, juego, química):", "")
    
    for p in pistas:
        if not search_term or search_term.lower() in p["titulo_full"].lower() or search_term.lower() in p["area"].lower() or search_term.lower() in p["vivencia"].lower():
            with st.expander(f"🔹 {p['doc_id']} — {p['titulo_corto']} | 📚 {p['area']}"):
                st.markdown(f"**Área:** {p['area']}")
                st.markdown(f"**Vivencia del Profe:** {p['vivencia']}")
                st.markdown(f"**Estrategia de Aula:** {p['estrategia']}")
                st.markdown("**Prompt de IA Sugerido:**")
                st.code(p['prompt'], language="markdown")

with tab_metodologia:
    st.markdown("<h3 style='color:#39FF14;'>ℹ️ Acerca de la Investigación</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Título del Proyecto:** SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA  
    **Investigadora Principal:** Catalina Díaz Chíquiza  
    **Asesora de Tesis:** Mg. Lady Johana Gómez Bernal  
    **Institución:** Universidad de Nariño — Maestría en Educación Virtual (e-MEV)  

    ---
    
    ### 🎯 Propósito del Ecosistema Transmedia
    Este recurso constituye el producto comunicativo y de devolución del **Objetivo Específico 3** de la investigación. Su finalidad es poner a disposición de la comunidad educadora una herramienta interactiva que combina la memoria pedagógica sonora con guías y *prompts* de Inteligencia Artificial, facilitando la resignificación del quehacer docente en entornos educativos digitales e híbridos actuales.
    """)
