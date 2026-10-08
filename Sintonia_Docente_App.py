import os

app_code = '''import streamlit as st
import os
import json
import re

# Configuración de la página
st.set_page_config(
    page_title="Sintonía Docente - Ecosistema de Resignificación",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Personalizados Avanzados - Estética Escenario Stand-up Ladrillo & Neón
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Permanent+Marker&display=swap');

    .stApp {
        background-color: #0E1117 !important;
        background-image: 
            linear-gradient(rgba(14, 17, 23, 0.92), rgba(14, 17, 23, 0.92)),
            linear-gradient(335deg, rgba(20, 20, 20, 0.8) 0px, transparent 2px),
            linear-gradient(155deg, rgba(20, 20, 20, 0.8) 0px, transparent 2px),
            linear-gradient(335deg, rgba(30, 30, 30, 0.8) 0px, transparent 2px),
            linear-gradient(155deg, rgba(30, 30, 30, 0.8) 0px, transparent 2px);
        background-size: 100% 100%, 58px 58px, 58px 58px, 58px 58px, 58px 58px;
        background-position: 0 0, 0 2px, 4px 35px, 29px 31px, 33px 6px;
        color: #F0F4F8 !important;
        font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #121824 !important;
        border-right: 2px solid #39FF14 !important;
        box-shadow: 2px 0 15px rgba(57, 255, 20, 0.15);
    }
    [data-testid="stSidebar"] * {
        color: #F0F4F8 !important;
    }
    
    /* FIX DEL MENÚ DESPLEGABLE (SELECTBOX): Letra Negra (#000000) siempre */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
        border: 2px solid #39FF14 !important;
        box-shadow: 0 0 10px rgba(57, 255, 20, 0.3);
    }
    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 700 !important;
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

    .title-neon {
        font-family: 'Freestyle Script', 'Caveat', 'Permanent Marker', cursive !important;
        font-size: 3.4em !important;
        font-weight: 700;
        color: #39FF14 !important;
        text-shadow: 0 0 8px rgba(57, 255, 20, 0.6), 0 0 18px rgba(57, 255, 20, 0.3);
        text-align: center;
        margin-bottom: 2px;
        line-height: 1.1;
    }
    .subtitle-neon {
        font-size: 1.05em;
        color: #00F0FF;
        text-shadow: 0 0 8px rgba(0, 240, 255, 0.5);
        text-align: center;
        margin-bottom: 25px;
        font-weight: 600;
    }

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

# 19 Fichas Pedagógicas Anonimizadas (DOC-01 a DOC-19)
PISTAS_EMBEDDED = [
    {
        "doc_id": "DOC-01",
        "pista_num": "01",
        "titulo_full": "Pista 01: Las Voces Anónimas del Corazón",
        "titulo": "Pista 01: Las Voces Anónimas del Corazón",
        "titulo_corto": "Las Voces Anónimas del Corazón",
        "area": "Francés y Lenguas Extranjeras",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "En medio del aislamiento y la timidez inicial de hablar en pantalla, surgió un ejercicio de escritura en el que los estudiantes pudieron expresar de forma sincera sus temores y emociones sin temor al qué dirán. La profe descubrió que el lenguaje es, ante todo, un puente para conectarse con la vida de los muchachos.",
        "estrategia": "Proponer actividades reales y vivenciales en lengua extranjera: los alumnos describen su ropa favorita, objetos significativos de su habitación o lugares de su casa mediante dinámicas de participación cercana y respetuosa.",
        "prompt": "🤖 Prompt para Práctica de Idiomas y Expresión Cotidiana\\n\\\"Actúa como un profesor cercano y entusiasta de lenguas extranjeras. Diseña un ejercicio práctico de 15 minutos para que mis estudiantes describan en el idioma que aprenden objetos cotidianos de su entorno o prendas de vestir. Incluye 3 preguntas sencillas de calentamiento y una rúbrica cualitativa enfocada en la confianza y el esfuerzo comunicativo más que en la perfección gramatical.\\\""
    },
    {
        "doc_id": "DOC-02",
        "pista_num": "02",
        "titulo_full": "Pista 02: Enseñar es Acompañar",
        "titulo": "Pista 02: Enseñar es Acompañar",
        "titulo_corto": "Enseñar es Acompañar",
        "area": "Inglés (Educación Infantil y Primaria)",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "Al enseñar a niños pequeños durante el encierro, el profe utilizó Paint a pulso para simular los renglones del cuaderno y guiar los trazos con el mouse. Además, en fechas especiales organizó retos con objetos cotidianos de la casa, demostrando que el afecto y la creatividad mantienen vivo el entusiasmo de los niños.",
        "estrategia": "Aprovechar la lúdica y los objetos de la vida diaria: organizar búsquedas del tesoro en casa o en el salón, juegos de asociación visual con dibujos sencillos y dinámicas corporales para afianzar el vocabulario básico.",
        "prompt": "🤖 Prompt para Dinámicas Lúdicas y Vocabulario con Objetos Reales\\n\\\"Actúa como docente especialista en didáctica de inglés para primaria. Diseña una guía con 4 dinámicas breves de juego activo usando objetos comunes del aula o del hogar (ropa, útiles, juguetes) para repasar vocabulario básico. Cada dinámica debe durar menos de 10 minutos y promover la participación espontánea sin presionar al niño.\\\""
    },
    {
        "doc_id": "DOC-03",
        "pista_num": "03",
        "titulo_full": "Pista 03: Tarjetas de Afecto en la Pantalla",
        "titulo": "Pista 03: Tarjetas de Afecto en la Pantalla",
        "titulo_corto": "Tarjetas de Afecto en la Pantalla",
        "area": "Cátedra de Educación Emocional / Filosofía y Humanidades",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La docente comprendió que en momentos de incertidumbre enseñar no es acumular contenidos, sino acompañar al ser humano. Recordó con cariño cómo los niños crearon tarjetas digitales dibujadas por ellos mismos para expresar su gratitud, demostrando que el vínculo afectivo es el verdadero motor del aprendizaje.",
        "estrategia": "Iniciar las jornadas con un 'círculo de la palabra' o pausa de conexión emocional: dedicar los primeros 10 minutos a escuchar cómo se sienten los estudiantes, usando preguntas socráticas sencillas y reflexivas.",
        "prompt": "🤖 Prompt para Círculos de Palabra y Acompañamiento Socioemocional\\n\\\"Actúa como un orientador escolar y profesor de humanidades. Diseña una guía de 15 minutos para realizar un círculo de palabra afectivo al inicio de la jornada con estudiantes. Incluye 3 preguntas sencillas y cálidas para abrir el diálogo sobre cómo se sienten y un cierre reflexivo que fomente la empatía en el grupo.\\\""
    },
    {
        "doc_id": "DOC-04",
        "pista_num": "04",
        "titulo_full": "Pista 04: Ventanas Abiertas a la Cotidianidad",
        "titulo": "Pista 04: Ventanas Abiertas a la Cotidianidad",
        "titulo_corto": "Ventanas Abiertas a la Cotidianidad",
        "area": "Educación Inicial y Preescolar",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "Con niños de preescolar, la profe transformó la rutina escolar invitándolos a compartir aspectos de su hogar y sus juguetes favoritos. Aprendió a adaptarse al ritmo de la infancia y a valorar la presencia de las familias como aliadas en el aula.",
        "estrategia": "Estructurar secuencias visuales claras y cortas: combinar momentos de explicación breve con actividades prácticas manipulativas, pausas de movimiento activo y constante reconocimiento positivo.",
        "prompt": "🤖 Prompt para Experiencias de Aprendizaje Visual e Infantil\\n\\\"Actúa como una maestra experta en educación inicial. Ayúdame a diseñar una secuencia didáctica de 20 minutos basada en imágenes y cuentos breves para niños de preescolar. La actividad debe incluir una pausa activa de movimiento corporal y una recomendación práctica para coordinar fácilmente con los padres de familia.\\\""
    },
    {
        "doc_id": "DOC-05",
        "pista_num": "05",
        "titulo_full": "Pista 05: El Visitante Inesperado",
        "titulo": "Pista 05: El Visitante Inesperado",
        "titulo_corto": "El Visitante Inesperado",
        "area": "Ciencias Sociales y Desarrollo Humano (Primaria)",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La docente dio el salto de la clase magistral tradicional al uso de relatos y presentaciones participativas. Recordó con emoción cómo las familias escuchaban sus clases de fondo y cómo pequeños detalles espontáneos permitieron romper la frialdad y acercar la historia a la vida real de sus estudiantes.",
        "estrategia": "Transformar los contenidos teóricos en historias cercanas: utilizar casos cotidianos, imágenes icónicas y preguntas problematizadoras que inviten a los alumnos a dar su opinión y relacionar el tema con su entorno.",
        "prompt": "🤖 Prompt para Generar Historias y Casos Cotidianos en Sociales\\n\\\"Actúa como un profesor apasionado de ciencias sociales. Dame 3 ejemplos de relatos breves o dilemas sencillos basados en la vida cotidiana para explicar a niños de primaria la importancia de la convivencia y los derechos en la comunidad. Incluye preguntas orientadoras para abrir una conversación agradable en el salón.\\\""
    },
    {
        "doc_id": "DOC-06",
        "pista_num": "06",
        "titulo_full": "Pista 06: Cumpleaños en Comunidad",
        "titulo": "Pista 06: Cumpleaños en Comunidad",
        "titulo_corto": "Cumpleaños en Comunidad",
        "area": "Educación Física, Recreación y Deporte",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "El profesor enfrentó el enorme reto de adaptar la actividad física a espacios reducidos. Con ingenio, utilizó implementos de aseo, elementos del hogar y música motivadora para mantener a los estudiantes activos y saludables, demostrando que el movimiento es bienestar mental.",
        "estrategia": "Diseñar circuitos motrices dinámicos con elementos caseros o del aula: organizar rutinas de ejercicios de bajo impacto, pausas activas y juegos de coordinación usando botellas plásticas, escobas o marcadores.",
        "prompt": "🤖 Prompt para Pausas Activas y Circuitos Motrices Sencillos\\n\\\"Actúa como un entrenador pedagógico y profesor de educación física. Diseña un circuito de 4 estaciones de movimiento y flexibilidad pensado para realizarse en espacios pequeños usando objetos cotidianos (sillas, botellas de agua). Describe cada ejercicio con instrucciones breves y divertidas para los estudiantes.\\\""
    },
    {
        "doc_id": "DOC-07",
        "pista_num": "07",
        "titulo_full": "Pista 07: La Mirada Incompleta",
        "titulo": "Pista 07: La Mirada Incompleta",
        "titulo_corto": "La Mirada Incompleta",
        "area": "Física y Ciencias Exactas",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "El docente descubrió que al explicar temas complejos como la física, ver a los abuelos y padres sentados al lado de los niños aprendiendo juntos enriquecía el proceso. Perdió el miedo a las herramientas digitales y comenzó a grabar explicaciones breves con pizarras visuales.",
        "estrategia": "Utilizar la indagación guiada con simuladores y experimentos simples: plantear preguntas problema cotidianas (como el movimiento de una bicicleta o el calor de una taza) para explorar los conceptos antes de la fórmula.",
        "prompt": "🤖 Prompt para Indagación Guiada en Ciencias y Física\\n\\\"Actúa como un docente de ciencias exactas que busca hacer la física fácil y entretenida. Diseña una actividad de indagación de 20 minutos usando una situación común del hogar o un simulador interactivo gratuito. Formula 3 preguntas cotidianas que lleven al estudiante a deducir el concepto principal sin usar jerga matemática compleja.\\\""
    },
    {
        "doc_id": "DOC-08",
        "pista_num": "08",
        "titulo_full": "Pista 08: El Refugio del Chat",
        "titulo": "Pista 08: El Refugio del Chat",
        "titulo_corto": "El Refugio del Chat",
        "area": "Educación Infantil y Dimensión Afectiva",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La maestra comprendió la importancia de la empatía al descubrir que el chat privado era el canal donde los estudiantes más tímidos se desahogaban. Fortaleció la confianza del grupo mediante dinámicas grupales afectivas.",
        "estrategia": "Implementar dinámicas de ludificación y cuentos interactivos: utilizar el juego simbólico y la narración colaborativa para abordar las emociones y la resolución pacífica de conflictos.",
        "prompt": "🤖 Prompt para Cuentos Interactivos y Ludificación Infantil\\n\\\"Actúa como una educadora infantil experta en juego y literatura. Crea una idea para adaptar un cuento corto tradicional en una experiencia interactiva donde los niños participen haciendo sonidos, gestos o dibujando en un papel. Incluye 2 pausas de movimiento para mantenerlos atentos.\\\""
    },
    {
        "doc_id": "DOC-09",
        "pista_num": "09",
        "titulo_full": "Pista 09: Dibujar el Alfabeto a Pulso",
        "titulo": "Pista 09: Dibujar el Alfabeto a Pulso",
        "titulo_corto": "Dibujar el Alfabeto a Pulso",
        "area": "Español y Lengua Castellana",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Tras el exceso de pantallas, la profesora decidió volver al encanto de los cuadernos, el papel, los colores y las lecturas en voz alta, promoviendo la creación literaria manual como un espacio de calma y reflexión.",
        "estrategia": "Alternar el trabajo digital con talleres análogos de creación: proponer la elaboración de diarios ilustrados, fanzines o cartas escritas a mano que estimulen la lectoescritura desde la expresión artística.",
        "prompt": "🤖 Prompt para Talleres de Lectura Crítica y Creación Análoga\\n\\\"Actúa como un profesor de literatura enfocado en el aprendizaje manipulativo y humano. Diseña un taller de lectura y escritura de 30 minutos donde los estudiantes analicen un poema o cuento corto usando materiales físicos (papel, colores, tijeras) para construir un diario ilustrado. Explica el paso a paso de forma clara.\\\""
    },
    {
        "doc_id": "DOC-10",
        "pista_num": "10",
        "titulo_full": "Pista 10: La Metamorfosis de la Voz",
        "titulo": "Pista 10: La Metamorfosis de la Voz",
        "titulo_corto": "La Metamorfosis de la Voz",
        "area": "Ciencias Naturales y Biología",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profesor no dejó morir la curiosidad científica: guió a sus estudiantes para realizar pequeñas observaciones de plantas y fenómenos naturales en sus cocinas y jardines, transformando la casa en un laboratorio vivo.",
        "estrategia": "Diseñar laboratorios caseros e indagar la naturaleza cercana: motivar el método científico mediante la observación directa de objetos, plantas o materiales caseros seguros sin necesidad de insumos costosos.",
        "prompt": "🤖 Prompt para Experimentos Caseros e Indagación Científica\\n\\\"Actúa como un biólogo y educador científico. Diseña una guía para un experimento casero completamente seguro que los estudiantes puedan realizar con elementos de la cocina (como sal, agua, aceite o plantas) para entender un fenómeno natural. Incluye la hipótesis inicial y una forma sencilla de presentar sus observaciones.\\\""
    },
    {
        "doc_id": "DOC-11",
        "pista_num": "11",
        "titulo_full": "Pista 11: El Gimnasio de los Objetos Olvidados",
        "titulo": "Pista 11: El Gimnasio de los Objetos Olvidados",
        "titulo_corto": "El Gimnasio de los Objetos Olvidados",
        "area": "Matemáticas en Primaria (1° a 3°)",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente utilizó ruletas virtuales, juegos con dados y fichas manipulables para perderle el miedo a las matemáticas, convirtiendo cada clase en un reto lúdico donde equivocarse era parte del aprendizaje.",
        "estrategia": "Gamificar el pensamiento numérico con material concreto: estructurar retos matemáticos mediante juegos de mesa simples, tiendas virtuales escolares o desafíos de conteo con granos y fichas.",
        "prompt": "🤖 Prompt para Juegos Matemáticos y Pensamiento Numérico\\n\\\"Actúa como una maestra experta en didáctica de las matemáticas para primaria. Diseña una actividad gamificada de 15 minutos llamada 'El mercado del aula' para practicar sumas y restas básicas usando fichas o papelitos. Incluye las reglas del juego y 3 retos numéricos divertidos adaptados a niños.\\\""
    },
    {
        "doc_id": "DOC-12",
        "pista_num": "12",
        "titulo_full": "Pista 12: El Aula de Tres Generaciones",
        "titulo": "Pista 12: El Aula de Tres Generaciones",
        "titulo_corto": "El Aula de Tres Generaciones",
        "area": "Ciencias Sociales e Historia / Bilingüismo",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La profesora organizó momentos humanos memorables, invitando a los abuelos a contar historias del pasado en clase. Comprobó que la memoria oral de las familias es el mejor recurso para enseñar historia viva.",
        "estrategia": "Implementar cuadros comparativos y análisis de casos reales: organizar entrevistas intergeneracionales o debates amables sobre temas de actualidad para desarrollar el pensamiento crítico.",
        "prompt": "🤖 Prompt para Análisis de Casos y Debate Ciudadano\\n\\\"Actúa como un docente de ciencias sociales enfocado en el pensamiento crítico. Diseña una actividad de debate breve (20 minutos) basada en una noticia sencilla sobre el cuidado del medio ambiente en la ciudad. Incluye 3 preguntas contrapuestas para guiarlos y pautas para que dialoguen con respeto.\\\""
    },
    {
        "doc_id": "DOC-13",
        "pista_num": "13",
        "titulo_full": "Pista 13: La Pedagogía del Equilibrio",
        "titulo": "Pista 13: La Pedagogía del Equilibrio",
        "titulo_corto": "La Pedagogía del Equilibrio",
        "area": "Tecnología e Informática",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profe tomó la decisión humanizada de priorizar la salud mental de sus alumnos frente al cansancio de las pantallas, enseñando tecnología desde el pensamiento lógico y la creación responsable.",
        "estrategia": "Desarrollar el pensamiento computacional sin pantallas (unplugged): proponer juegos de lógica, diagramas de flujo en papel y diseño de algoritmos mediante instrucciones para tareas cotidianas.",
        "prompt": "🤖 Prompt para Pensamiento Computacional Desenchufado (*Unplugged*)\\n\\\"Actúa como un profesor de tecnología e informática. Diseña una dinámica de pensamiento computacional sin necesidad de computadores (*unplugged*) para explicar qué es un algoritmo usando la preparación de una receta o un juego de pasos en el salón. Describe la instrucción paso a paso de forma amena.\\\""
    },
    {
        "doc_id": "DOC-14",
        "pista_num": "14",
        "titulo_full": "Pista 14: El Laboratorio en la Cocina",
        "titulo": "Pista 14: El Laboratorio en la Cocina",
        "titulo_corto": "El Laboratorio en la Cocina",
        "area": "Coordinación Académica y Pedagogía Infantil",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente utilizó Paint como su tablero digital humano para corregir con cariño las tareas y mantener motivados a los niños de los primeros grados con stickers y caritas felices digitales.",
        "estrategia": "Construir decálogos de convivencia y acuerdos claros: acordar pautas amables para el uso de canales digitales, tiempos de descanso y entrega de trabajos con criterios flexibles.",
        "prompt": "🤖 Prompt para Decálogos de Convivencia y Acuerdos Pedagógicos\\n\\\"Actúa como un directivo docente enfocado en el clima escolar positivo. Ayúdame a redactar un decálogo amigable de 5 acuerdos de convivencia digital y uso responsable del celular en el aula, redactado en un lenguaje positivo, claro y motivador para estudiantes y familias.\\\""
    },
    {
        "doc_id": "DOC-15",
        "pista_num": "15",
        "titulo_full": "Pista 15: La Palabra sobre la Imagen",
        "titulo": "Pista 15: La Palabra sobre la Imagen",
        "titulo_corto": "La Palabra sobre la Imagen",
        "area": "Lengua Castellana y Proceso Lecto-Escritor",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "En los grados iniciales, la maestra estableció rutinas de lectura compartida en las que cada niño leía un párrafo desde su casa, dándoles protagonismo y seguridad al hablar en público.",
        "estrategia": "Evaluar mediante sustentación oral y diálogo guiado: reemplazar las pruebas memorísticas por diálogos cortos donde el alumno explique con sus propias palabras lo que comprendió del texto.",
        "prompt": "🤖 Prompt para Evaluación Formativa de la Expresión Oral\\n\\\"Actúa como docente de lenguaje y lectura. Diseña una pauta sencilla de retroalimentación oral en 3 pasos para evaluar cuando un estudiante cuenta un cuento o expone una idea frente al grupo. La pauta debe enfocarse en resaltar lo positivo, hacer una pregunta para profundizar y motivarlo a seguir hablando.\\\""
    },
    {
        "doc_id": "DOC-16",
        "pista_num": "16",
        "titulo_full": "Pista 16: La Orquesta de los Micrófonos",
        "titulo": "Pista 16: La Orquesta de los Micrófonos",
        "titulo_corto": "La Orquesta de los Micrófonos",
        "area": "Ciencias Sociales y Ciencia Política",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Un estudiante tímido que casi no hablaba en clase presencial encontró en los foros escritos su canal ideal para brillar y expresar posturas políticas profundas e informadas.",
        "estrategia": "Aprovechar espacios de participación escrita y foros: habilitar muros colaborativos (como Padlet o carteleras físicas) para que todos los alumnos expresen sus opiniones sin la presión del micrófono.",
        "prompt": "🤖 Prompt para Muros de Opinión y Diálogo Ciudadano\\n\\\"Actúa como un docente de ciencias sociales y ciudadanía. Genera 3 preguntas detonantes y reflexivas sobre la convivencia democrática en el colegio para que los estudiantes respondan en un foro o muro colaborativo. Asegúrate de que las preguntas motiven a los estudiantes más tímidos a dar su opinión.\\\""
    },
    {
        "doc_id": "DOC-17",
        "pista_num": "17",
        "titulo_full": "Pista 17: El Receso de los Chistes",
        "titulo": "Pista 17: El Receso de los Chistes",
        "titulo_corto": "El Receso de los Chistes",
        "area": "Matemáticas y Física (Innovación y Humor)",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profesor decidió institucionalizar los últimos 5 minutos de su clase como 'el receso de chistes'. Usó la risa y el buen humor como la mejor estrategia para liberar el estrés, conectar con los jóvenes y hacer amables las materias más exigentes.",
        "estrategia": "Incorporar pausas de humor y acertijos lógicos en clase: usar juegos de palabras, adivinanzas numéricas o pequeños chistes al final de temas complejos para mantener un ambiente de aula relajado y motivante.",
        "prompt": "🤖 Prompt para Pausas de Humor Educativo y Acertijos Lógicos\\n\\\"Actúa como un profesor lúdico de matemáticas. Diseña una lista de 3 acertijos lógicos y juegos de palabras matemáticos breves para usar como pausa activa o cierre relajante de clase (de 5 minutos). Cada acertijo debe incluir su solución explicada de forma sencilla y divertida.\\\""
    },
    {
        "doc_id": "DOC-18",
        "pista_num": "18",
        "titulo_full": "Pista 18: Museos sin Fronteras",
        "titulo": "Pista 18: Museos sin Fronteras",
        "titulo_corto": "Museos sin Fronteras",
        "area": "Educación Artística y Plástica",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente aprovechó la tecnología para llevar a sus estudiantes a recorridos virtuales por más de 80 museos del mundo desde la pantalla. Luego, los guió para recrear las obras de arte con pintura, cartón y materiales reciclables de su propia casa.",
        "estrategia": "Conectar la exploración estética digital con la creación plástica manual: mostrar imágenes o videos breves de obras famosas y proponer retos de creación con materiales reciclables que los alumnos tengan a la mano.",
        "prompt": "🤖 Prompt para Apreciación Artística y Creación con Reciclaje\\n\\\"Actúa como una profesora creativa de educación artística. Diseña una guía de trabajo de 30 minutos donde los estudiantes observen una obra de arte o escultura famosa y luego la recreen usando elementos reciclables del hogar (cajas, tapas, papel). Incluye 2 preguntas para reflexionar sobre lo que sintieron al crear.\\\""
    },
    {
        "doc_id": "DOC-19",
        "pista_num": "19",
        "titulo_full": "Pista 19: El Títere que Aprendió a Enseñar",
        "titulo": "Pista 19: El Títere que Aprendió a Enseñar",
        "titulo_corto": "El Títere que Aprendió a Enseñar",
        "area": "Inglés y Ciencias en Educación Infantil",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Para captar la atención de los más pequeños, la profe creó a 'Mr. Whiskers', un gatito títere que solo hablaba inglés. Además, animó con herramientas sencillas los dibujos de los niños, llenándolos de orgullo y ganas de participar.",
        "estrategia": "Usar personajes guiados y proyectos creativos animados: incorporar un títere o personaje simbólico para hacer preguntas curiosas e interactuar con los alumnos en idiomas o ciencias.",
        "prompt": "🤖 Prompt para Personajes Pedagógicos e Indagación Curiosa\\n\\\"Actúa como una educadora e investigadora en didáctica infantil. Diseña el guion breve de presentación (2 minutos) para un personaje de títere o mascota del aula que le enseñe a los niños curiosidades sobre los animales o la naturaleza en inglés. Incluye 2 preguntas interactivas para hacerle al grupo.\\\""
    }
]

def cargar_pistas():
    pistas_path = "pistas_data.json"
    if os.path.exists(pistas_path):
        try:
            with open(pistas_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data:
                    return data
        except Exception:
            pass
    return PISTAS_EMBEDDED

pistas = cargar_pistas()

# BUSCADOR BULLETPROOF DE AUDIOS EN TODO EL REPOSITORIO
def buscar_audio_robusto(doc_code, doc_num):
    num_int = str(int(doc_num)) if doc_num.isdigit() else doc_num
    exts = ('.mp3', '.ogg', '.wav', '.mp4', '.m4a', '.aac', '.flac', '.wma')
    
    encontrados = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.lower().endswith(exts):
                path = os.path.join(root, f)
                fn = f.lower()
                if doc_code.lower() in fn or doc_code.replace('-', '_').lower() in fn:
                    return path
                if f'pista_{doc_num}' in fn or f'pista {doc_num}' in fn or f'pista{doc_num}' in fn or f'pista_{num_int}' in fn or f'pista {num_int}' in fn:
                    return path
                if fn.startswith(f'{doc_num}.') or fn.startswith(f'{doc_num}_') or fn.startswith(f'{doc_num}-') or fn.startswith(f'{doc_num} '):
                    return path
                if fn.startswith(f'{num_int}.') or fn.startswith(f'{num_int}_') or fn.startswith(f'{num_int}-') or fn.startswith(f'{num_int} '):
                    return path
                encontrados.append((fn, path))
                
    for fn, path in encontrados:
        nums = re.findall(r'\\d+', fn)
        if doc_num in nums or num_int in nums:
            return path
            
    return None

st.markdown('<div class="title-neon">🎧 Sintonía Docente</div>', unsafe_allow_html=True)
st.markdown("""
<div class="subtitle-neon">
    SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA<br>
    <span style="font-size:0.9em; color:#E0E0E0; font-style:italic;">Ecosistema Multimodal de Resignificación Docente &bull; Universidad de Nariño</span>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='color:#39FF14; font-family:\"Freestyle Script\", \"Caveat\", cursive; font-size:2.2em; text-align:center; text-shadow:0 0 8px rgba(57, 255, 20, 0.5);'>🎙️ Sintonía Docente</h2>", unsafe_allow_html=True)
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

st.sidebar.markdown("<p style='color:#00F0FF; font-weight:bold; margin-top:15px;'>🎵 Selecciona la Pista Sonora:</p>", unsafe_allow_html=True)

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
            
        alb_name = pista_actual.get("album", "")
        p_title = pista_actual.get("titulo", "")
        p_area = pista_actual.get("area", "")
        st.markdown(f'<div class="{header_class}"><span style="background-color:{album_color}; color:#000000; font-weight:bold; padding:4px 12px; border-radius:12px; font-size:0.85em;">{alb_name}</span><h2 style="color:#FFFFFF; margin-top:10px; margin-bottom:5px; text-shadow:0 0 10px {album_color};">{p_title}</h2><p style="color:#E0E0E0; font-size:1.05em; margin:0;">📚 <b>Área Curricular:</b> {p_area}</p></div>', unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#39FF14; margin-bottom:8px;'>🎙️ Reproductor de Voz y Sonido:</h4>", unsafe_allow_html=True)
        
        doc_code = pista_actual.get("doc_id", "DOC-01")
        doc_num = pista_actual.get("pista_num", "01")
        
        audio_encontrado = buscar_audio_robusto(doc_code, doc_num)
        
        if audio_encontrado:
            st.audio(audio_encontrado)
        else:
            st.info(f"🎧 **Audio detectado:** Al colocar la carpeta `sintonia_docente` con tus archivos de audio (`{doc_code}.mp3`, `pista_{doc_num}.ogg`, etc.), el reproductor los cargará automáticamente.")

        st.markdown("<br>", unsafe_allow_html=True)

        col_v, col_e = st.columns(2, gap="medium")
        p_viv = pista_actual.get("vivencia", "")
        p_est = pista_actual.get("estrategia", "")
        with col_v:
            st.markdown(f'<div style="background-color: #121824; border-radius: 14px; padding: 20px; border: 2px solid #00F0FF; box-shadow: 0 0 12px rgba(0, 240, 255, 0.2); height: 100%;"><div style="color: #00F0FF; font-size: 1.15em; font-weight: 700; margin-bottom: 10px;">💬 Vivencia del Profe:</div><div style="color: #F0F4F8; font-size: 1.02em; line-height: 1.6;">{p_viv}</div></div>', unsafe_allow_html=True)

        with col_e:
            st.markdown(f'<div style="background-color: #121824; border-radius: 14px; padding: 20px; border: 2px solid #39FF14; box-shadow: 0 0 12px rgba(57, 255, 20, 0.2); height: 100%;"><div style="color: #39FF14; font-size: 1.15em; font-weight: 700; margin-bottom: 10px;">💡 Estrategia de Aula Replicable:</div><div style="color: #F0F4F8; font-size: 1.02em; line-height: 1.6;">{p_est}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div style="background-color: #181028; padding: 18px; border-radius: 12px; border: 2px solid #FF007F; box-shadow: 0 0 15px rgba(255, 0, 127, 0.25); margin-bottom: 10px;"><div style="color: #FF007F; font-size: 1.15em; font-weight: 700; margin-bottom: 8px;">🤖 Prompt de Inteligencia Artificial Sugerido (Listo para usar):</div></div>', unsafe_allow_html=True)

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
    st.markdown("<h3 style='color:#00F0FF;'>ℹ️ Sobre el Ecosistema Multimodal 'Sintonía Docente'</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Investigación:** Resignificación de la Experiencia Docente sobre la Enseñanza Mediada por Tecnología  
    **Título de la Tesis:** SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA  
    **Investigadora:** Catalina Díaz Chíquiza  
    **Asesora:** Mg. Lady Johana Gómez Bernal  
    **Institución:** Universidad de Nariño — Maestría en Educación Virtual (e-MEV)  

    ---

    ### 🎯 Objetivo del Ecosistema (Objetivo Específico 3):
    El producto comunicativo *Sintonía Docente* ha sido co-construido como una herramienta multimodal y de acceso libre para la comunidad educadora. Cada ficha integra la memoria viva de la pandemia con estrategias didácticas y *prompts* de Inteligencia Artificial diseñados para enriquecer la labor docente actual en entornos presenciales, híbridos y virtuales.

    **Nota Ética:** La totalidad de los relatos ha sido anonimizada bajo la codificación de **DOC-01 a DOC-19** para resguardar la identidad de los maestros participantes de las instituciones educativas privadas de Popayán.
    """)
'''

with open('/workspace/scratch/app_clean_bulletproof.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Wrote app_clean_bulletproof.py successfully.")
