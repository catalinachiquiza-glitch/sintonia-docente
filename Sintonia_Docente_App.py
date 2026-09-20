import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Sintonía Docente - Ecosistema Transmedia",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Personalizados - Estética Oscura Estilo Spotify (Negro, Verde #1DB954, Ámbar #FFB703)
st.markdown("""
<style>
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .css-1d38157, [data-testid="stSidebar"] {
        background-color: #181818 !important;
        border-right: 1px solid #282828;
    }
    .album-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .album-header-2 {
        background: linear-gradient(135deg, #d4145a 0%, #fbb03b 100%);
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .track-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #333333;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .prompt-card {
        background-color: #1A2421;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1DB954;
        box-shadow: 0 4px 10px rgba(29,185,84,0.15);
    }
    .badge-area {
        background-color: #282828;
        color: #FFB703;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.85em;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 8px;
    }
    .teacher-name {
        color: #1DB954;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 4px;
    }
    .track-title {
        color: #FFFFFF;
        font-size: 1.6em;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .stButton>button {
        background-color: #1DB954 !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border-radius: 24px !important;
        padding: 10px 24px !important;
        border: none !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1ed760 !important;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# Base de datos de las 14 Pistas
pistas = {
    "Álbum 1: El latido en el silencio": [
        {
            "id": "p1",
            "titulo": "Pista 01: El Eco de las Miradas Perdidas",
            "docente": "Claudia Avilés",
            "area": "Preescolar y Primaria • Colegio Colombo Francés",
            "sinopsis": "Narración sobre la sorpresa inicial en preescolar, las anécdotas cotidianas del hogar tras la pantalla (papás que aparecían en toalla por descuido) y la preservación de la esencia humana en el aula virtual.",
            "prompt": """Actúa como docente especialista en Educación Inicial. Diseña una guía didáctica de 3 dinámicas de pausas activas socioemocionales para niños de preescolar en entornos mixtos. 
Incluye: 1) Nombre de la actividad, 2) Objetivo pedagógico, 3) Instrucción paso a paso integrando expresión corporal y cuentos animados, y 4) Una consigna de reflexión para los padres de familia.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        },
        {
            "id": "p2",
            "titulo": "Pista 02: Detrás del Cuadro Negro",
            "docente": "Susy Téllez",
            "area": "Educación Inicial y Preescolar • Gimnasio Calibío",
            "sinopsis": "Relato sobre la incertidumbre inicial y cómo el confinamiento impulsó la exploración de recursos tecnológicos variados para enriquecer el lenguaje infantil.",
            "prompt": """Actúa como educador en lenguaje infantil. Genera una secuencia de 4 actividades gamificadas para animación a la lectura en primer grado utilizando presentaciones digitales interactivas. 
Estructura cada actividad con: Nivel de dificultad, Recurso interactivo sugerido, Consigna para el estudiante y Criterio de evaluación formativa.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        },
        {
            "id": "p3",
            "titulo": "Pista 03: El Abrazo que Atraviesa la Pantalla",
            "docente": "Kelly Fernández",
            "area": "Básica Primaria • Gimnasio Latinoamericano",
            "sinopsis": "Experiencia centrada en la empatía, el acompañamiento socioemocional y la contención frente a las brechas de conectividad de cada hogar.",
            "prompt": """Actúa como psicopedagogo escolar. Diseña un taller de acompañamiento socioemocional de 15 minutos para iniciar la jornada en primaria, enfocado en la escucha activa y la empatía. 
Proporciona el guion verbal del docente, 3 preguntas detonantes de diálogo en círculo y una actividad de cierre en papel.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
        },
        {
            "id": "p4",
            "titulo": "Pista 04: Caminar sobre la Incertidumbre",
            "docente": "Diana Gutiérrez",
            "area": "Básica Primaria • Colegio Colombo Francés",
            "sinopsis": "Vivencia en Jardín sobre cómo mantener la motivación de los niños pequeños y la hermosa anécdota de las tarjetas digitales en Paint para el Día del Profesor.",
            "prompt": """Actúa como docente de tecnología infantil. Diseña un proyecto de aula de 3 sesiones para enseñar el uso básico de herramientas de dibujo digital (como Paint) integrando mensajes de afecto. 
Incluye: Objetivos de motricidad fina digital, plantilla de trabajo paso a paso y rúbrica cualitativa de desempeño.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
        },
        {
            "id": "p5",
            "titulo": "Pista 05: El Movimiento Desafiante",
            "docente": "Michael Acosta",
            "area": "Educación Física y Deporte • Colegio Colombo Francés",
            "sinopsis": "Reinvención de la educación física en casa utilizando tarros de aseo, escobas y cojines para armar circuitos motrices en espacios reducidos.",
            "prompt": """Actúa como educador físico escolar. Crea un circuito de motricidad y acondicionamiento físico escolar utilizando únicamente objetos domésticos reutilizables (tarros, cojines, cintas). 
Estructura el plan con: Calentamiento articulado, 4 estaciones de movimiento progresivo, adaptar a espacios reducidos y técnica de respiración consciente.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
        },
        {
            "id": "p6",
            "titulo": "Pista 06: Sanar la Brecha con Amor",
            "docente": "Manuela Chamorro",
            "area": "Matemáticas en Primaria • Colombo Francés",
            "sinopsis": "Anécdota del gato caminante en prejardín y las ruletas aleatorias para motivar la participación sin temor en las clases de matemáticas.",
            "prompt": """Actúa como especialista en didáctica de las matemáticas primarias. Diseña una estrategia de gamificación para pensamiento numérico utilizando ruletas interactivas de participación y retos rápidos. 
Proporciona 5 ejercicios de cálculo mental contextualizado, reglas de juego en aula y método de retroalimentación positiva.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"
        },
        {
            "id": "p7",
            "titulo": "Pista 07: El Lenguaje de la Invención",
            "docente": "Jimmy Cerquera",
            "area": "Lenguas Modernas e Inglés • Colegio Colombo Francés",
            "sinopsis": "Transformación de la enseñanza del inglés mediante retos interactivos, producciones audiovisuales y pedagogía lúdica sin caer en el llenado de PDFs.",
            "prompt": """Actúa como docente de Inglés EFL/ESL. Crea un desafío de simulación de rol (Role-Play) de 15 minutos para primaria, donde los estudiantes resuelvan un 'misterio escolar' usando vocabulario cotidiano. 
Incluye: Banco de expresiones clave (chunks), tarjeta de rol para el estudiante, rúbrica de fluidez oral y actividad de autoevaluación.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"
        }
    ],
    "Álbum 2: La alquimia pedagógica": [
        {
            "id": "p8",
            "titulo": "Pista 08: La Física de la Conexión",
            "docente": "John Jairo Londoño",
            "area": "Física y Ciencias Exactas • Seminario Menor",
            "sinopsis": "Anécdota de dar clase a los abuelitos y padres que acompañaban a los niños, y el uso de cámaras enfocadas al tablero de la casa para explicar física.",
            "prompt": """Actúa como docente de Ciencias Físicas. Diseña una plantilla de clase invertida (Flipped Classroom) para física de secundaria sobre mecánica y movimiento. 
Incluye: Guia para video explicativo breve de 3 minutos, 3 preguntas de comprobación previa y un taller práctico de resolución de problemas en vivo.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"
        },
        {
            "id": "p9",
            "titulo": "Pista 09: Cartografía de una Metamorfosis",
            "docente": "Adriana Martínez",
            "area": "Ciencias Sociales • Colombo Francés Popayán",
            "sinopsis": "Uso de fuentes históricas digitales y prensa comparada para transformar la crisis en un laboratorio de pensamiento crítico e historia en tiempo real.",
            "prompt": """Actúa como historiadora y pedagoga de Ciencias Sociales. Diseña una guía de análisis crítico comparativo entre dos noticias históricas sobre pandemias o eventos globales. 
Proporciona: Criterios de verificación de fuentes, 4 preguntas socráticas de contraste y una matriz de análisis de sesgos mediáticos para estudiantes.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"
        },
        {
            "id": "p10",
            "titulo": "Pista 10: La Armonía de la Palabra",
            "docente": "Gloria Rosero",
            "area": "Lengua Extranjera Francés • Colegio Colombo-Francés",
            "sinopsis": "Integración de recursos fonéticos multimedia y expresiones culturales en red para fortalecer la competencia comunicativa en francés con calidez humana.",
            "prompt": """Actúa como docente de Francés Lengua Extranjera (FLE). Diseña un taller de fonética y pronunciación apoyado en recursos multimedia breves para nivel principiante (A1). 
Estructura la lección con: Ejercicios de discriminación auditiva, trabalenguas fonéticos culturales y pauta de grabación de audio reflexiva.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"
        },
        {
            "id": "p11",
            "titulo": "Pista 11: El Retorno a lo Esencial",
            "docente": "Nazly Bolaños",
            "area": "Español y Literatura • Colegio Colombo Francés",
            "sinopsis": "Postura pedagógica de 'pedagogía del equilibrio', revalorizando la lectura en libro impreso, la escritura en papel y el aprendizaje manipulativo tras el hiperconsumo digital.",
            "prompt": """Actúa como docente especialista en Literatura. Diseña un taller de comprensión lectora profunda y escritura creativa en papel (máximo 45 minutos) sin pantallas. 
Incluye: Consignas de lectura pausada de un texto impreso, 3 detonantes de escritura a mano en libreta y rúbrica de sensibilidad poética y estética.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        },
        {
            "id": "p12",
            "titulo": "Pista 12: La Magia de la Adaptación",
            "docente": "Andrés Ayala",
            "area": "Ciencias Naturales y Biología • Colombo Francés",
            "sinopsis": "Transformación de la mesa de la cocina en laboratorio de biología y exploración entusiasta de prompts de Inteligencia Artificial para la indagación científica.",
            "prompt": """Actúa como biólogo y educador científico. Diseña una guía de laboratorio casero seguro con materiales de cocina (vinagre, bicarbonato, pigmentos vegetales) para explicar reacciones naturales. 
Proporciona: Tabla de variables independientes/dependientes, 3 preguntas de formulación de hipótesis y rúbrica cualitativa de informe de laboratorio.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        },
        {
            "id": "p13",
            "titulo": "Pista 13: Ventanas al Pensamiento Crítico",
            "docente": "Alma Flor",
            "area": "Ciencias Sociales y Política • Colombo Francés",
            "sinopsis": "Postura analítica y cautelosa frente a la IA, utilizándola con sentido ético para enseñar a verificar fuentes y dudar de las respuestas del algoritmo.",
            "prompt": """Actúa como docente de Ciencias Políticas y Ética. Diseña una actividad de debate en aula donde los estudiantes evalúen un texto generado por IA sobre un hecho histórico relevante. 
Incluye: Pauta para identificar sesgos del algoritmo, checklist de verificación en fuentes académicas reales y rúbrica de argumentación crítica.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
        },
        {
            "id": "p14",
            "titulo": "Pista 14: La Arquitectura de la Improvisación",
            "docente": "Gerson Achury",
            "area": "Tecnología e Informática • Gimnasio Calibío",
            "sinopsis": "Enseñar tecnología sin plataforma previa, dando prioridad a la sustentación oral y enseñando hoy a entrenar bots y prompts con visión sobria y crítica.",
            "prompt": """Actúa como docente de Tecnología e Informática. Diseña una guía práctica para enseñar a estudiantes a estructurar 'prompts' efectivos de revisión lógica y sintáctica en proyectos tecnológicos. 
Estructura: Anatomía de un prompt (Rol, Contexto, Tarea, Restricciones), 3 ejemplos comparativos (malo vs. excelente) y taller práctico de evaluación oral.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
        }
    ]
}

# --- ENCABEZADO Y BARRA LATERAL ---
st.sidebar.markdown("## 🎧 Sintonía Docente")
st.sidebar.markdown("*Ecosistema Transmedia de Resignificación Docente*")
st.sidebar.markdown("---")

album_seleccionado = st.sidebar.radio(
    "Selecciona el Álbum / Volumen:",
    list(pistas.keys())
)

lista_pistas = pistas[album_seleccionado]
nombres_pistas = [p["titulo"] for p in lista_pistas]

pista_tit_seleccionada = st.sidebar.selectbox(
    "Selecciona la Pista Sonora:",
    nombres_pistas
)

# Buscar objeto de la pista seleccionada
pista_actual = next(p for p in lista_pistas if p["titulo"] == pista_tit_seleccionada)

# Header según el álbum
if "Álbum 1" in album_seleccionado:
    st.markdown("""
    <div class="album-header">
        <h1 style="margin:0; color:#FFFFFF;">🎧 Álbum 1: El latido en el silencio</h1>
        <p style="margin:4px 0 0 0; color:#FFB703; font-size:1.1em;">Volumen 1: Historias del Afecto, el Vínculo y la Resiliencia Humana</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="album-header-2">
        <h1 style="margin:0; color:#FFFFFF;">🎧 Álbum 2: La alquimia pedagógica</h1>
        <p style="margin:4px 0 0 0; color:#FFB703; font-size:1.1em;">Volumen 2: Reinvención Didáctica, Innovación y Mediación Tecnológica con Sentido</p>
    </div>
    """, unsafe_allow_html=True)

# --- ÁREA PRINCIPAL EN 2 COLUMNAS / CUADROS ---
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown('<div class="track-card">', unsafe_allow_html=True)
    
    # Avatar y Título del docente
    col_img, col_info = st.columns([1, 3])
    with col_img:
        # Avatar ilustrativo con icono elegante
        st.markdown("""
        <div style="background-color:#282828; width:80px; height:80px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:2px solid #1DB954; font-size:35px;">
            👤
        </div>
        """, unsafe_allow_html=True)
    with col_info:
        st.markdown(f'<div class="badge-area">{pista_actual["area"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="teacher-name">{pista_actual["docente"]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f'<div class="track-title">{pista_actual["titulo"]}</div>', unsafe_allow_html=True)
    st.markdown(f'**📝 Sinopsis / Sentido de la Vivencia:**\n\n{pista_actual["sinopsis"]}')
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 🎙️ Relato Sonoro (1.5 min)")
    st.audio(pista_actual["audio_demo"], format="audio/mp3")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="prompt-card">', unsafe_allow_html=True)
    st.markdown("### 🤖 Ficha de Transferibilidad & Prompt de IA")
    st.markdown("*Consigna optimizada para ChatGPT / Gemini / Claude basada en la experiencia de esta asignatura:*")
    
    st.code(pista_actual["prompt"], language="markdown")
    
    st.info("💡 **Indicación para el Docente:** Haz clic en el botón a continuación para copiar esta consigna pedagógica y pegarla directamente en la herramienta de IA de tu preferencia.")
    
    if st.button("📋 Copiar Prompt para IA al Portapapeles", key=f"btn_{pista_actual['id']}"):
        st.success("¡Prompt copiado conceptualmente! Listo para usar en ChatGPT o Claude.")
        
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Ecosistema Transmedia Sintonía Docente • Universidad de Nariño • Tesis de Maestría 2026")
