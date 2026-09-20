import streamlit as st
import os

# Configuración de página
st.set_page_config(
    page_title="Sintonía Docente - Ecosistema Transmedia",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Personalizados Avanzados - Estética Oscura Estilo Spotify (Negro #121212, Verde #1DB954, Ámbar #FFB703)
st.markdown("""
<style>
    /* Fondo general */
    .stApp {
        background-color: #121212 !important;
        color: #FFFFFF !important;
        font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Barra lateral (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #181818 !important;
        border-right: 1px solid #282828 !important;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    /* Texto de radio buttons y selectbox en la barra lateral */
    div[role="radiogroup"] label p, div[data-baseweb="select"] span {
        color: #FFFFFF !important;
        font-size: 1.05em !important;
        font-weight: 500 !important;
    }

    /* Encabezado del Álbum */
    .album-header-1 {
        background: linear-gradient(135deg, #0d254c 0%, #1a3a6e 100%);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 24px;
        border: 1px solid #1e4a8a;
        box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    }
    .album-header-2 {
        background: linear-gradient(135deg, #5c1d24 0%, #852b36 100%);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 24px;
        border: 1px solid #a33543;
        box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    }
    
    /* Tarjetas de Contenido (Cuadros) */
    .track-card {
        background-color: #181818;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #2A2A2A;
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    }
    .prompt-card {
        background-color: #14221A;
        padding: 24px;
        border-radius: 16px;
        border: 1.5px solid #1DB954;
        box-shadow: 0 6px 20px rgba(29,185,84,0.15);
    }
    
    /* Badges y Etiquetas */
    .badge-area {
        background-color: #282828;
        color: #FFB703 !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.9em;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 8px;
        border: 1px solid #383838;
    }
    .teacher-name {
        color: #1DB954 !important;
        font-size: 1.4em;
        font-weight: 800;
        margin-bottom: 4px;
    }
    .track-title {
        color: #FFFFFF !important;
        font-size: 1.6em;
        font-weight: 800;
        margin-bottom: 12px;
    }
    .copy-tip {
        background-color: #1DB95422;
        border: 1px solid #1DB954;
        border-radius: 10px;
        padding: 10px 14px;
        color: #1DB954 !important;
        font-size: 0.9em;
        font-weight: 600;
        margin-top: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Base de datos unificada de las 14 Pistas (Sin nombres de colegios para proteger confidencialidad)
pistas = {
    "Álbum 1: El latido en el silencio": [
        {
            "id": "p1",
            "titulo": "Pista 01: El Eco de las Miradas Perdidas",
            "docente": "Claudia Avilés",
            "area": "Preescolar y Primaria",
            "imagen": "images/claudia_aviles.png",
            "sinopsis": "Narración sobre la sorpresa inicial en preescolar, las anécdotas cotidianas del hogar tras la pantalla (papás que aparecían en toalla por descuido) y la preservación de la esencia humana en el aula virtual.",
            "prompt": """Actúa como docente especialista en Educación Inicial. Diseña una guía didáctica de 3 dinámicas de pausas activas socioemocionales para niños de preescolar en entornos mixtos. 

Incluye:
1. Nombre de la actividad y objetivo pedagógico.
2. Instrucción paso a paso integrando expresión corporal y cuentos animados.
3. Una consigna de reflexión para la familia.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        },
        {
            "id": "p2",
            "titulo": "Pista 02: Detrás del Cuadro Negro",
            "docente": "Susy Téllez",
            "area": "Educación Inicial y Preescolar",
            "imagen": "images/susy_tellez.png",
            "sinopsis": "Relato sobre la incertidumbre inicial y cómo el confinamiento impulsó la exploración de recursos tecnológicos variados para enriquecer el lenguaje infantil.",
            "prompt": """Actúa como educador en lenguaje infantil. Genera una secuencia de 4 actividades gamificadas para animación a la lectura en primer grado utilizando presentaciones digitales interactivas. 

Estructura:
1. Nivel de dificultad y recurso interactivo sugerido.
2. Consigna para el estudiante.
3. Criterio de evaluación formativa.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        },
        {
            "id": "p3",
            "titulo": "Pista 03: El Abrazo que Atraviesa la Pantalla",
            "docente": "Kelly Fernández",
            "area": "Básica Primaria",
            "imagen": "images/kelly_fernandez.png",
            "sinopsis": "Experiencia centrada en la empatía, el acompañamiento socioemocional y la contención frente a las brechas de conectividad de cada hogar.",
            "prompt": """Actúa como psicopedagogo escolar. Diseña un taller de acompañamiento socioemocional de 15 minutos para iniciar la jornada en primaria, enfocado en la escucha activa y la empatía. 

Incluye:
1. Guion verbal de apertura para el docente.
2. 3 preguntas detonantes de diálogo en círculo.
3. Actividad de cierre reflexivo.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
        },
        {
            "id": "p4",
            "titulo": "Pista 04: Caminar sobre la Incertidumbre",
            "docente": "Diana Gutiérrez",
            "area": "Básica Primaria",
            "imagen": "images/diana_gutierrez.png",
            "sinopsis": "Vivencia en Jardín sobre cómo mantener la motivación de los niños pequeños y la hermosa anécdota de las tarjetas digitales en Paint para el Día del Profesor.",
            "prompt": """Actúa como docente de tecnología infantil. Diseña un proyecto de aula de 3 sesiones para enseñar el uso básico de herramientas de dibujo digital (como Paint) integrando tarjetas de afecto. 

Incluye:
1. Objetivos de motricidad fina digital.
2. Guía paso a paso adaptada a transición y jardín.
3. Rúbrica cualitativa de desempeño.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
        },
        {
            "id": "p5",
            "titulo": "Pista 05: El Movimiento Desafiante",
            "docente": "Michael Acosta",
            "area": "Educación Física y Deporte",
            "imagen": "images/michael_acosta.png",
            "sinopsis": "Reinvención de la educación física en casa utilizando tarros de aseo, escobas y cojines para armar circuitos motrices en espacios reducidos.",
            "prompt": """Actúa como educador físico escolar. Crea un circuito de motricidad y acondicionamiento físico escolar utilizando objetos domésticos reutilizables (tarros, cojines, cintas) para realizar en espacios reducidos. 

Estructura:
1. Calentamiento articulado.
2. 4 estaciones de movimiento progresivo.
3. Técnica de respiración consciente al cierre.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
        },
        {
            "id": "p6",
            "titulo": "Pista 06: Sanar la Brecha con Amor",
            "docente": "Manuela Chamorro",
            "area": "Matemáticas en Primaria",
            "imagen": "images/manuela_chamorro.png",
            "sinopsis": "Anécdota del gato caminante en prejardín y las ruletas aleatorias para motivar la participación sin temor en las clases de matemáticas.",
            "prompt": """Actúa como especialista en didáctica de las matemáticas primarias. Diseña una estrategia de gamificación para pensamiento numérico utilizando ruletas interactivas de participación aleatoria y retos rápidos. 

Incluye:
1. 5 ejercicios de cálculo mental contextualizado.
2. Reglas de juego participativo.
3. Pauta de retroalimentación positiva.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"
        },
        {
            "id": "p7",
            "titulo": "Pista 07: El Lenguaje de la Invención",
            "docente": "Jimmy Cerquera",
            "area": "Lenguas Modernas e Inglés",
            "imagen": "images/jimmy_cerquera.png",
            "sinopsis": "Transformación de la enseñanza del inglés mediante retos interactivos, producciones audiovisuales y pedagogía lúdica sin caer en el llenado pasivo de guías.",
            "prompt": """Actúa como docente de Inglés (EFL). Crea un desafío de simulación de rol (Role-Play) de 15 minutos para primaria, donde los estudiantes resuelvan un 'misterio escolar' usando vocabulario cotidiano. 

Incluye:
1. Banco de expresiones clave (chunks de lenguaje).
2. Tarjetas de rol interactivo.
3. Rúbrica de expresión oral y autoevaluación.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"
        }
    ],
    "Álbum 2: La alquimia pedagógica": [
        {
            "id": "p8",
            "titulo": "Pista 08: La Física de la Conexión",
            "docente": "John Jairo Londoño",
            "area": "Física y Ciencias Exactas",
            "imagen": "images/john_jairo_londono.png",
            "sinopsis": "Anécdota de dar clase a los abuelitos y padres que acompañaban a los niños, y el uso de cámaras enfocadas al tablero de la casa para explicar física.",
            "prompt": """Actúa como docente de Ciencias Físicas. Diseña una plantilla de clase invertida (Flipped Classroom) para física de secundaria sobre mecánica y movimiento. 

Incluye:
1. Estructura para video explicativo breve de 3 minutos.
2. 3 preguntas de comprobación previa.
3. Taller de resolución de problemas contextualizados en vivo.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"
        },
        {
            "id": "p9",
            "titulo": "Pista 09: Cartografía de una Metamorfosis",
            "docente": "Adriana Martínez",
            "area": "Ciencias Sociales",
            "imagen": "images/adriana_martinez.png",
            "sinopsis": "Uso de fuentes históricas digitales y prensa comparada para transformar la crisis en un laboratorio de pensamiento crítico e historia en tiempo real.",
            "prompt": """Actúa como historiadora y pedagoga de Ciencias Sociales. Diseña una guía de análisis crítico comparativo entre dos noticias históricas sobre pandemias o transformaciones globales. 

Incluye:
1. Criterios de verificación de fuentes informativas.
2. 4 preguntas socráticas de contraste histórico.
3. Matriz de análisis de sesgos mediáticos.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"
        },
        {
            "id": "p10",
            "titulo": "Pista 10: La Armonía de la Palabra",
            "docente": "Gloria Rosero",
            "area": "Lengua Extranjera Francés",
            "imagen": "images/gloria_rosero.png",
            "sinopsis": "Integración de recursos fonéticos multimedia y expresiones culturales en red para fortalecer la competencia comunicativa en francés con calidez humana.",
            "prompt": """Actúa como docente de Francés Lengua Extranjera (FLE). Diseña un taller de fonética y pronunciación apoyado en recursos multimedia breves para nivel principiante (A1). 

Estructura:
1. Ejercicios de discriminación auditiva fonética.
2. Trabalenguas culturales francófonos.
3. Pauta de grabación de audio reflexiva.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"
        },
        {
            "id": "p11",
            "titulo": "Pista 11: El Retorno a lo Esencial",
            "docente": "Nazly Bolaños",
            "area": "Español y Literatura",
            "imagen": "images/nazly_bolanos.png",
            "sinopsis": "Postura pedagógica de 'pedagogía del equilibrio', revalorizando la lectura en libro impreso, la escritura en papel y el aprendizaje manipulativo tras el hiperconsumo digital.",
            "prompt": """Actúa como docente especialista en Literatura. Diseña un taller de comprensión lectora profunda y escritura creativa en papel (máximo 45 minutos) sin pantallas. 

Incluye:
1. Consignas de lectura pausada de un texto impreso.
2. 3 detonantes de escritura a mano en libreta.
3. Rúbrica de sensibilidad poética y estética.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        },
        {
            "id": "p12",
            "titulo": "Pista 12: La Magia de la Adaptación",
            "docente": "Andrés Ayala",
            "area": "Ciencias Naturales y Biología",
            "imagen": "images/andres_ayala.png",
            "sinopsis": "Transformación de la mesa de la cocina en laboratorio de biología y exploración entusiasta de prompts de Inteligencia Artificial para la indagación científica.",
            "prompt": """Actúa como biólogo y educador científico. Diseña una guía de laboratorio casero seguro con materiales de cocina (vinagre, bicarbonato, pigmentos vegetales) para explicar reacciones naturales. 

Estructura:
1. Tabla de variables independientes y dependientes.
2. 3 preguntas de formulación de hipótesis científicas.
3. Rúbrica cualitativa de informe de indagación.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        },
        {
            "id": "p13",
            "titulo": "Pista 13: Ventanas al Pensamiento Crítico",
            "docente": "Alma Flor",
            "area": "Ciencias Sociales y Política",
            "imagen": "images/alma_flor.png",
            "sinopsis": "Postura analítica y cautelosa frente a la IA, utilizándola con sentido ético para enseñar a verificar fuentes y dudar de las respuestas del algoritmo.",
            "prompt": """Actúa como docente de Ciencias Políticas y Ética. Diseña una actividad de debate en aula donde los estudiantes evalúen un texto generado por IA sobre un hecho histórico relevante. 

Incluye:
1. Pauta para identificar sesgos del algoritmo de IA.
2. Checklist de verificación en fuentes académicas reales.
3. Rúbrica de argumentación crítica.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
        },
        {
            "id": "p14",
            "titulo": "Pista 14: La Arquitectura de la Improvisación",
            "docente": "Gerson Achury",
            "area": "Tecnología e Informática",
            "imagen": "images/gerson_achury.png",
            "sinopsis": "Enseñar tecnología sin plataforma previa, dando prioridad a la sustentación oral y enseñando hoy a entrenar bots y prompts con visión sobria y crítica.",
            "prompt": """Actúa como docente de Tecnología e Informática. Diseña una guía práctica para enseñar a estudiantes a estructurar 'prompts' efectivos de revisión lógica y sintáctica en proyectos tecnológicos. 

Estructura:
1. Anatomía de un prompt (Rol, Contexto, Tarea, Restricciones).
2. 3 ejemplos comparativos (malo vs. excelente).
3. Taller práctico de evaluación oral.""",
            "audio_demo": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
        }
    ]
}

# --- BARRA LATERAL (CONTROLES Y NAVEGACIÓN) ---
st.sidebar.markdown("<h2 style='color:#1DB954;'>🎧 Sintonía Docente</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#CCCCCC; font-style:italic;'>Ecosistema Transmedia de Resignificación Docente</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

album_seleccionado = st.sidebar.radio(
    "📌 Selecciona el Álbum / Volumen:",
    list(pistas.keys())
)

lista_pistas = pistas[album_seleccionado]
nombres_pistas = [p["titulo"] for p in lista_pistas]

st.sidebar.markdown("<br>", unsafe_allow_html=True)
pista_tit_seleccionada = st.sidebar.selectbox(
    "🎵 Selecciona la Pista Sonora:",
    nombres_pistas
)

# Buscar objeto de la pista seleccionada
pista_actual = next(p for p in lista_pistas if p["titulo"] == pista_tit_seleccionada)

# --- ENCABEZADO PRINCIPAL DEL ÁLBUM ---
if "Álbum 1" in album_seleccionado:
    st.markdown("""
    <div class="album-header-1">
        <h1 style="margin:0; color:#FFFFFF; font-size:2em;">🎧 Álbum 1: El latido en el silencio</h1>
        <p style="margin:6px 0 0 0; color:#FFB703; font-size:1.15em; font-weight:600;">Volumen 1: Historias del Afecto, el Vínculo y la Resiliencia Humana</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="album-header-2">
        <h1 style="margin:0; color:#FFFFFF; font-size:2em;">🎧 Álbum 2: La alquimia pedagógica</h1>
        <p style="margin:6px 0 0 0; color:#FFB703; font-size:1.15em; font-weight:600;">Volumen 2: Reinvención Didáctica, Innovación y Mediación Tecnológica con Sentido</p>
    </div>
    """, unsafe_allow_html=True)

# --- ÁREA PRINCIPAL DIVIDIDA EN 2 CUADROS LIMPIOS ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="track-card">', unsafe_allow_html=True)
    
    col_img, col_info = st.columns([1, 2.8])
    with col_img:
        # Si existe la imagen personalizada del docente, la muestra; si no, muestra el avatar de respaldo
        if os.path.exists(pista_actual["imagen"]):
            st.image(pista_actual["imagen"], use_column_width=True)
        else:
            st.markdown("""
            <div style="background-color:#282828; width:85px; height:85px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:2px solid #1DB954; font-size:38px; margin-bottom:10px;">
                👤
            </div>
            """, unsafe_allow_html=True)
            
    with col_info:
        st.markdown(f'<div class="badge-area">{pista_actual["area"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="teacher-name">{pista_actual["docente"]}</div>', unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color:#333; margin:15px 0;'>", unsafe_allow_html=True)
    st.markdown(f'<div class="track-title">{pista_actual["titulo"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#DDDDDD; font-size:1.05em; line-height:1.6;"><b>📝 Sinopsis de la Vivencia:</b><br>{pista_actual["sinopsis"]}</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#1DB954; margin-bottom:8px;'>🎙️ Reproductor del Relato Sonoro (1.5 min)</h4>", unsafe_allow_html=True)
    st.audio(pista_actual["audio_demo"], format="audio/mp3")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="prompt-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#1DB954; margin-top:0;'>🤖 Ficha de Transferibilidad & Prompt de IA</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#E0E0E0; font-size:0.95em;'>Consigna optimizada para la práctica pedagógica en esta asignatura:</p>", unsafe_allow_html=True)
    
    # Bloque de código con la función nativa de copia rápida en la esquina superior derecha
    st.code(pista_actual["prompt"], language="markdown")
    
    # Tip explicativo funcional para copiar con 1 clic sin botones inútiles
    st.markdown("""
    <div class="copy-tip">
        📋 <b>¿Cómo copiar el prompt?</b> Pasa el cursor sobre la casilla negra de arriba y haz clic en el icono de copiar (📋) en la esquina superior derecha para pegarlo en ChatGPT, Gemini o Claude.
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><hr style='border-color:#333;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888888; font-size:0.9em;'>Ecosistema Transmedia Sintonía Docente • Universidad de Nariño • Tesis de Maestría 2026</p>", unsafe_allow_html=True)
