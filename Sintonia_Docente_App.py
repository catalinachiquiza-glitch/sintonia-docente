       import streamlit as st
import os
import json

# Configuración de página
st.set_page_config(
    page_title="Sintonía Docente - Ecosistema Transmedia",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Personalizados - Estética Escenario Stand-up / Pared de Ladrillos Oscuros + Neón Verde Urbano Moderado
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Sedgwick+Ave&family=Rock+Salt&family=Permanent+Marker&family=Inter:wght@400;600;700&display=swap');

    /* Fondo de Ladrillo Oscuro Estilo Escenario / Stand-up Comedy */
    .stApp {
        background-color: #0d0f12 !important;
        background-image: 
            radial-gradient(circle at 50% 20%, rgba(57, 255, 20, 0.08) 0%, transparent 60%),
            linear-gradient(rgba(13, 15, 18, 0.88), rgba(13, 15, 18, 0.95)),
            repeating-linear-gradient(0deg, transparent, transparent 19px, rgba(255, 255, 255, 0.03) 20px),
            repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(255, 255, 255, 0.03) 40px) !important;
        color: #F0F4F8 !important;
        font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Barra Lateral Escenario */
    [data-testid="stSidebar"] {
        background-color: #12161c !important;
        border-right: 2px solid #39FF14 !important;
        box-shadow: 2px 0 15px rgba(57, 255, 20, 0.15);
    }
    [data-testid="stSidebar"] * {
        color: #F0F4F8 !important;
    }

    /* MENÚ DESPLEGABLE (SELECTBOX) EN NEGRO SOBRE BLANCO */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 2px solid #39FF14 !important;
        box-shadow: 0 0 8px rgba(57, 255, 20, 0.3);
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

    /* TÍTULO EN NEÓN VERDE Y FUENTE CURSIVA URBANA / ESTILO CALLE MODERADO */
    .title-urban-neon {
        font-family: 'Sedgwick Ave', 'Caveat', 'Rock Salt', 'Permanent Marker', cursive !important;
        font-size: 3.2em;
        color: #39FF14;
        text-shadow: 0 0 4px #39FF14, 0 0 12px rgba(57, 255, 20, 0.5), 2px 2px 4px #000000;
        text-align: center;
        margin-bottom: 2px;
        letter-spacing: 1px;
    }
    .subtitle-thesis {
        font-size: 0.95em;
        color: #00F0FF;
        text-shadow: 0 0 6px rgba(0, 240, 255, 0.4);
        text-align: center;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
    }

    /* TARJETAS DE ÁLBUM */
    .album-header-1 {
        background: linear-gradient(135deg, #092026 0%, #103840 100%);
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        border: 1.5px solid #00F0FF;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.2);
    }
    .album-header-2 {
        background: linear-gradient(135deg, #26091c 0%, #401032 100%);
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        border: 1.5px solid #FF007F;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.2);
    }

    /* CAJITAS INDEPENDIENTES PARA CADA SECCIÓN */
    .box-vivencia {
        background-color: #121820;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #00F0FF;
        border-top: 1px solid rgba(0, 240, 255, 0.3);
        border-right: 1px solid rgba(0, 240, 255, 0.2);
        border-bottom: 1px solid rgba(0, 240, 255, 0.2);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        min-height: 180px;
    }
    .box-estrategia {
        background-color: #122018;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #39FF14;
        border-top: 1px solid rgba(57, 255, 20, 0.3);
        border-right: 1px solid rgba(57, 255, 20, 0.2);
        border-bottom: 1px solid rgba(57, 255, 20, 0.2);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        min-height: 180px;
    }
    .box-title-v {
        color: #00F0FF;
        font-size: 1.15em;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .box-title-e {
        color: #39FF14;
        font-size: 1.15em;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .box-text {
        color: #E2E8F0;
        font-size: 0.98em;
        line-height: 1.6;
    }
    
    .prompt-header {
        color: #FF007F;
        font-size: 1.2em;
        font-weight: 700;
        margin-top: 22px;
        margin-bottom: 8px;
        text-shadow: 0 0 6px rgba(255, 0, 127, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# DATOS DE LAS 19 PISTAS INCRUSTADOS DIRECTAMENTE
PISTAS_EMBEDDED = '[\n  {\n    "doc_id": "DOC-01",\n    "pista_num": "01",\n    "titulo_full": "Pista 01: Las Voces Anónimas del Corazón",\n    "titulo": "Pista 01: Las Voces Anónimas del Corazón",\n    "titulo_corto": "Las Voces Anónimas del Corazón",\n    "area": "Francés y Lenguas Extranjeras",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "En medio del aislamiento y la timidez inicial de hablar en pantalla, surgió un ejercicio de escritura en el que los estudiantes pudieron expresar de forma sincera sus temores y emociones sin temor al qué dirán. La profe descubrió que el lenguaje es, ante todo, un puente para conectarse con la vida de los muchachos.",\n    "estrategia": "Proponer actividades reales y vivenciales en lengua extranjera: los alumnos describen su ropa favorita, objetos significativos de su habitación o lugares de su casa mediante dinámicas de participación cercana y respetuosa.",\n    "prompt": "🤖 Prompt para Práctica de Idiomas y Expresión Cotidiana\\n\\"Actúa como un profesor cercano y entusiasta de lenguas extranjeras. Diseña un ejercicio práctico de 15 minutos para que mis estudiantes describan en el idioma que aprenden objetos cotidianos de su entorno o prendas de vestir. Incluye 3 preguntas sencillas de calentamiento y una rúbrica cualitativa enfocada en la confianza y el esfuerzo comunicativo más que en la perfección gramatical.\\""\n  },\n  {\n    "doc_id": "DOC-02",\n    "pista_num": "02",\n    "titulo_full": "Pista 02: Enseñar es Acompañar",\n    "titulo": "Pista 02: Enseñar es Acompañar",\n    "titulo_corto": "Enseñar es Acompañar",\n    "area": "Inglés (Educación Infantil y Primaria)",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "Al enseñar a niños pequeños durante el encierro, el profe utilizó Paint a pulso para simular los renglones del cuaderno y guiar los trazos con el mouse. Además, en fechas especiales organizó retos con objetos cotidianos de la casa, demostrando que el afecto y la creatividad mantienen vivo el entusiasmo de los niños.",\n    "estrategia": "Aprovechar la lúdica y los objetos de la vida diaria: organizar búsquedas del tesoro en casa o en el salón, juegos de asociación visual con dibujos sencillos y dinámicas corporales para afianzar el vocabulario básico.",\n    "prompt": "🤖 Prompt para Dinámicas Lúdicas y Vocabulario con Objetos Reales\\n\\"Actúa como docente especialista en didáctica de inglés para primaria. Diseña una guía con 4 dinámicas breves de juego activo usando objetos comunes del aula o del hogar (ropa, útiles, juguetes) para repasar vocabulario básico. Cada dinámica debe durar menos de 10 minutos y promover la participación espontánea sin presionar al niño.\\""\n  },\n  {\n    "doc_id": "DOC-03",\n    "pista_num": "03",\n    "titulo_full": "Pista 03: Tarjetas de Afecto en la Pantalla",\n    "titulo": "Pista 03: Tarjetas de Afecto en la Pantalla",\n    "titulo_corto": "Tarjetas de Afecto en la Pantalla",\n    "area": "Cátedra de Educación Emocional / Filosofía y Humanidades",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "La docente comprendió que en momentos de incertidumbre enseñar no es acumular contenidos, sino acompañar al ser humano. Recordó con cariño cómo los niños crearon tarjetas digitales dibujadas por ellos mismos para expresar su gratitud, demostrando que el vínculo afectivo es el verdadero motor del aprendizaje.",\n    "estrategia": "Iniciar las jornadas con un \'círculo de la palabra\' o pausa de conexión emocional: dedicar los primeros 10 minutos a escuchar cómo se sienten los estudiantes, usando preguntas socráticas sencillas y reflexivas.",\n    "prompt": "🤖 Prompt para Círculos de Palabra y Acompañamiento Socioemocional\\n\\"Actúa como un orientador escolar y profesor de humanidades. Diseña una guía de 15 minutos para realizar un círculo de palabra afectivo al inicio de la jornada con estudiantes. Incluye 3 preguntas sencillas y cálidas para abrir el diálogo sobre cómo se sienten y un cierre reflexivo que fomente la empatía en el grupo.\\""\n  },\n  {\n    "doc_id": "DOC-04",\n    "pista_num": "04",\n    "titulo_full": "Pista 04: Ventanas Abiertas a la Cotidianidad",\n    "titulo": "Pista 04: Ventanas Abiertas a la Cotidianidad",\n    "titulo_corto": "Ventanas Abiertas a la Cotidianidad",\n    "area": "Educación Inicial y Preescolar",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "Con niños de preescolar, la profe transformó la rutina guiando las actividades paso a paso con imágenes sencillas y diapositivas coloridas. Descubrió que coordinarse con las familias y mantener la ternura en cada instrucción era la clave para que los más pequeños se sintieran seguros y motivados.",\n    "estrategia": "Estructurar secuencias visuales claras y cortas: combinar adivinanzas, pausas musicales y guías visuales sencillas para la familia, asegurando que cada niño avance a su propio ritmo sin saturarse.",\n    "prompt": "🤖 Prompt para Experiencias de Aprendizaje Visual e Infantil\\n\\"Actúa como una maestra experta en educación inicial. Ayúdame a diseñar una secuencia didáctica de 20 minutos basada en imágenes y cuentos breves para niños de preescolar. La actividad debe incluir una pausa activa de movimiento corporal y una recomendación práctica para coordinar fácilmente con los padres de familia.\\""\n  },\n  {\n    "doc_id": "DOC-05",\n    "pista_num": "05",\n    "titulo_full": "Pista 05: El Visitante Inesperado",\n    "titulo": "Pista 05: El Visitante Inesperado",\n    "titulo_corto": "El Visitante Inesperado",\n    "area": "Ciencias Sociales y Desarrollo Humano (Primaria)",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "La docente dio el salto de la clase magistral tradicional al uso de relatos y presentaciones participativas. Recordó con emoción cómo las familias escuchaban sus clases de fondo y cómo pequeños detalles espontáneos permitieron romper la frialdad y acercar la historia a la vida real de sus estudiantes.",\n    "estrategia": "Transformar los contenidos teóricos en historias cercanas: utilizar casos cotidianos, imágenes icónicas y preguntas problematizadoras que inviten a los alumnos a dar su opinión y relacionar el tema con su entorno.",\n    "prompt": "🤖 Prompt para Generar Historias y Casos Cotidianos en Sociales\\n\\"Actúa como un profesor apasionado de ciencias sociales. Dame 3 ejemplos de relatos breves o dilemas sencillos basados en la vida cotidiana para explicar a niños de primaria la importancia de la convivencia y los derechos en la comunidad. Incluye preguntas orientadoras para abrir una conversación agradable en el salón.\\""\n  },\n  {\n    "doc_id": "DOC-06",\n    "pista_num": "06",\n    "titulo_full": "Pista 06: Cumpleaños en Comunidad",\n    "titulo": "Pista 06: Cumpleaños en Comunidad",\n    "titulo_corto": "Cumpleaños en Comunidad",\n    "area": "Educación Física, Recreación y Deporte",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "El profesor enfrentó el enorme reto de adaptar la actividad física a espacios reducidos. Con ingenio, utilizó implementos de aseo, elementos del hogar y música motivadora para mantener a los estudiantes activos y saludables, demostrando que el movimiento es bienestar mental.",\n    "estrategia": "Diseñar circuitos motrices dinámicos con elementos caseros o del aula: organizar rutinas de ejercicios de bajo impacto, pausas activas y juegos de coordinación usando botellas plásticas, escobas o marcadores.",\n    "prompt": "🤖 Prompt para Pausas Activas y Circuitos Motrices Sencillos\\n\\"Actúa como un entrenador pedagógico y profesor de educación física. Diseña un circuito de 4 estaciones de movimiento y flexibilidad pensado para realizarse en espacios pequeños usando objetos cotidianos (sillas, botellas de agua). Describe cada ejercicio con instrucciones breves y divertidas para los estudiantes.\\""\n  },\n  {\n    "doc_id": "DOC-07",\n    "pista_num": "07",\n    "titulo_full": "Pista 07: La Mirada Incompleta",\n    "titulo": "Pista 07: La Mirada Incompleta",\n    "titulo_corto": "La Mirada Incompleta",\n    "area": "Física y Ciencias Exactas",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "El docente descubrió que al explicar temas complejos como la física, ver a los abuelos y padres sentados al lado de los niños aprendiendo juntos enriquecía el proceso. Perdió el miedo a las herramientas digitales y comenzó a grabar explicaciones breves con pizarras visuales.",\n    "estrategia": "Utilizar la indagación guiada con simuladores y experimentos simples: plantear preguntas problema cotidianas (como el movimiento de una bicicleta o el calor de una taza) para explorar los conceptos antes de la fórmula.",\n    "prompt": "🤖 Prompt para Indagación Guiada en Ciencias y Física\\n\\"Actúa como un docente de ciencias exactas que busca hacer la física fácil y entretenida. Diseña una actividad de indagación de 20 minutos usando una situación común del hogar o un simulador interactivo gratuito. Formula 3 preguntas cotidianas que lleven al estudiante a deducir el concepto principal sin usar jerga matemática compleja.\\""\n  },\n  {\n    "doc_id": "DOC-08",\n    "pista_num": "08",\n    "titulo_full": "Pista 08: El Refugio del Chat",\n    "titulo": "Pista 08: El Refugio del Chat",\n    "titulo_corto": "El Refugio del Chat",\n    "area": "Educación Infantil y Dimensión Afectiva",\n    "album": "Álbum 1: El Latido en el Silencio",\n    "vivencia": "La maestra comprendió la importancia de la empatía y el buen humor en el aula. Usó historias vivas, fondos animados y cuentos interactivos para mantener la chispa del aprendizaje en los niños, aprendiendo que la tecnología debe sumar calidez y no distancia.",\n    "estrategia": "Implementar dinámicas de ludificación y cuentos expresivos: intercalar momentos de lectura compartida con pausas de expresión gestual y artística que mantengan la alegría en el salón de clase.",\n    "prompt": "🤖 Prompt para Cuentos Interactivos y Ludificación Infantil\\n\\"Actúa como una educadora infantil experta en juego y literatura. Crea una idea para adaptar un cuento corto tradicional en una experiencia interactiva donde los niños participen haciendo sonidos, gestos o dibujando en un papel. Incluye 2 pausas de movimiento para mantenerlos atentos.\\""\n  },\n  {\n    "doc_id": "DOC-09",\n    "pista_num": "09",\n    "titulo_full": "Pista 09: Dibujar el Alfabeto a Pulso",\n    "titulo": "Pista 09: Dibujar el Alfabeto a Pulso",\n    "titulo_corto": "Dibujar el Alfabeto a Pulso",\n    "area": "Español y Lengua Castellana",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "Tras el exceso de pantallas, la profesora decidió hacer una pausa consciente y regresar a lo análogo y manipulativo: recortar, armar, escribir a mano y tocar el papel. Redescubrió que la lectura crítica y la escritura creativa se disfrutan más cuando se sienten en las manos.",\n    "estrategia": "Alternar el trabajo digital con talleres análogos y manipulativos: crear diarios de lectura en papel, murales físicos de palabras y álbumes ilustrados hechos a mano por los mismos alumnos.",\n    "prompt": "🤖 Prompt para Talleres de Lectura Crítica y Creación Análoga\\n\\"Actúa como un profesor de literatura enfocado en el aprendizaje manipulativo y humano. Diseña un taller de lectura y escritura de 30 minutos donde los estudiantes analicen un poema o cuento corto usando materiales físicos (papel, colores, tijeras) para construir un diario ilustrado. Explica el paso a paso de forma clara.\\""\n  },\n  {\n    "doc_id": "DOC-10",\n    "pista_num": "10",\n    "titulo_full": "Pista 10: La Metamorfosis de la Voz",\n    "titulo": "Pista 10: La Metamorfosis de la Voz",\n    "titulo_corto": "La Metamorfosis de la Voz",\n    "area": "Ciencias Naturales y Biología",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "El profesor no dejó morir la curiosidad científica y creó la estrategia de \'El laboratorio en mi cocina\'. Con ingredientes caseros como repollo morado, vinagre y bicarbonato, demostró que la ciencia está viva en cualquier rincón del hogar.",\n    "estrategia": "Diseñar laboratorios caseros e indagar la naturaleza cercana: proponer pequeñas observaciones científicas con elementos cotidianos para que los estudiantes formulen hipótesis y experimenten sin peligro.",\n    "prompt": "🤖 Prompt para Experimentos Caseros e Indagación Científica\\n\\"Actúa como un biólogo y educador científico. Diseña una guía para un experimento casero completamente seguro que los estudiantes puedan realizar con elementos de la cocina (como sal, agua, aceite o plantas). Incluye la lista de materiales, 3 preguntas de hipótesis y una forma sencilla de presentar sus observaciones.\\""\n  },\n  {\n    "doc_id": "DOC-11",\n    "pista_num": "11",\n    "titulo_full": "Pista 11: El Gimnasio de los Objetos Olvidados",\n    "titulo": "Pista 11: El Gimnasio de los Objetos Olvidados",\n    "titulo_corto": "El Gimnasio de los Objetos Olvidados",\n    "area": "Matemáticas en Primaria (1° a 3°)",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "La docente utilizó ruletas virtuales, juegos con semillas y desafíos de tienda escolar para que los niños de primaria perdieran el miedo a los números. Comprendió que cuando las matemáticas se juegan y se tocan, el aprendizaje perdura.",\n    "estrategia": "Gamificar el pensamiento numérico con material concreto: organizar retos de cálculo mental rápido usando fichas, juegos de mercado escolar y tableros interactivos sencillos.",\n    "prompt": "🤖 Prompt para Juegos Matemáticos y Pensamiento Numérico\\n\\"Actúa como una maestra experta en didáctica de las matemáticas para primaria. Diseña una actividad gamificada de 15 minutos llamada \'El mercado del aula\' para practicar sumas y restas básicas usando fichas o papelitos. Incluye las reglas del juego y 3 retos numéricos divertidos adaptados a niños.\\""\n  },\n  {\n    "doc_id": "DOC-12",\n    "pista_num": "12",\n    "titulo_full": "Pista 12: El Aula de Tres Generaciones",\n    "titulo": "Pista 12: El Aula de Tres Generaciones",\n    "titulo_corto": "El Aula de Tres Generaciones",\n    "area": "Ciencias Sociales e Historia / Bilingüismo",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "La profesora organizó momentos humanos memorables, como celebrar cumpleaños a través de las pantallas o debatir noticias actuales. Aprendió a sintetizar los contenidos en presentaciones breves para dar más tiempo a la conversación rica entre estudiantes.",\n    "estrategia": "Implementar cuadros comparativos y análisis de casos reales: utilizar diapositivas breves para presentar ideas clave y abrir de inmediato espacio para el debate de opinión y la reflexión en grupos.",\n    "prompt": "🤖 Prompt para Análisis de Casos y Debate Ciudadano\\n\\"Actúa como un docente de ciencias sociales enfocado en el pensamiento crítico. Diseña una actividad de debate breve (20 minutos) basada en una noticia sencilla sobre el cuidado del medio ambiente en la ciudad. Incluye 3 preguntas contrapuestas para guiarlos y pautas para que dialoguen con respeto.\\""\n  },\n  {\n    "doc_id": "DOC-13",\n    "pista_num": "13",\n    "titulo_full": "Pista 13: La Pedagogía del Equilibrio",\n    "titulo": "Pista 13: La Pedagogía del Equilibrio",\n    "titulo_corto": "La Pedagogía del Equilibrio",\n    "area": "Tecnología e Informática",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "El profe tomó la decisión humanizada de priorizar la sustentación oral y la lógica de los alumnos por encima de exigir cámaras encendidas a quienes tenían mala conexión. Enseñó que la tecnología debe estar al servicio de las personas y no al revés.",\n    "estrategia": "Desarrollar el pensamiento computacional sin pantallas (actividades *unplugged*): usar juegos de lógica con tarjetas, instrucciones paso a paso humanas y diálogos donde el alumno explique cómo solucionó un problema.",\n    "prompt": "🤖 Prompt para Pensamiento Computacional Desenchufado (*Unplugged*)\\n\\"Actúa como un profesor de tecnología e informática. Diseña una dinámica de pensamiento computacional sin necesidad de computadores (*unplugged*) para explicar qué es un algoritmo usando la preparación de una receta o un juego de pasos en el salón. Describe la instrucción paso a paso de forma amena.\\""\n  },\n  {\n    "doc_id": "DOC-14",\n    "pista_num": "14",\n    "titulo_full": "Pista 14: El Laboratorio en la Cocina",\n    "titulo": "Pista 14: El Laboratorio en la Cocina",\n    "titulo_corto": "El Laboratorio en la Cocina",\n    "area": "Coordinación Académica y Pedagogía Infantil",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "La docente utilizó Paint como su tablero digital hecho a mano para explicar a su manera. Como directiva, construyó acuerdos de paciencia y confianza con los maestros y familias, recordando que la gestión educativa debe ser siempre cercana y comprensiva.",\n    "estrategia": "Construir decálogos de convivencia y acuerdos claros de aula: establecer pautas amables para la escucha activa, la participación organizada y el uso con sentido de las herramientas digitales.",\n    "prompt": "🤖 Prompt para Decálogos de Convivencia y Acuerdos Pedagógicos\\n\\"Actúa como un directivo docente enfocado en el clima escolar positivo. Ayúdame a redactar un decálogo amigable de 5 acuerdos de convivencia digital y uso responsable del celular en el aula, redactado en un lenguaje positivo, claro y motivador para estudiantes y familias.\\""\n  },\n  {\n    "doc_id": "DOC-15",\n    "pista_num": "15",\n    "titulo_full": "Pista 15: La Palabra sobre la Imagen",\n    "titulo": "Pista 15: La Palabra sobre la Imagen",\n    "titulo_corto": "La Palabra sobre la Imagen",\n    "area": "Lengua Castellana y Proceso Lecto-Escritor",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "En los grados iniciales, la maestra estableció rutinas claras de escucha y normas sencillas para tomar la palabra. Descubrió que al combinar la lectura de cuentos con presentaciones sencillas, los niños fortalecieron enormemente su expresión verbal.",\n    "estrategia": "Evaluar mediante sustentación oral y diálogo guiado: hacer preguntas cortas al final de las lecturas para que los alumnos cuenten con sus propias palabras lo que entendieron y compartan sus reflexiones.",\n    "prompt": "🤖 Prompt para Evaluación Formativa de la Expresión Oral\\n\\"Actúa como docente de lenguaje y lectura. Diseña una pauta sencilla de retroalimentación oral en 3 pasos para evaluar cuando un estudiante cuenta un cuento o expone una idea frente al grupo. La pauta debe enfocarse en resaltar lo positivo, hacer una pregunta para profundizar y motivarlo a seguir hablando.\\""\n  },\n  {\n    "doc_id": "DOC-16",\n    "pista_num": "16",\n    "titulo_full": "Pista 16: La Orquesta de los Micrófonos",\n    "titulo": "Pista 16: La Orquesta de los Micrófonos",\n    "titulo_corto": "La Orquesta de los Micrófonos",\n    "area": "Ciencias Sociales y Ciencia Política",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "Un estudiante tímido que casi no hablaba en clase presencial comenzó a escribir largos mensajes en el chat para compartir reflexiones muy profundas. La profesora descubrió que la tecnología abrió puertas a nuevas formas de expresión para quienes antes callaban.",\n    "estrategia": "Aprovechar espacios de participación escrita y foros de opinión: combinar el diálogo en clase con pequeños muros colaborativos digitales donde los estudiantes respondan preguntas breves a su ritmo.",\n    "prompt": "🤖 Prompt para Muros de Opinión y Diálogo Ciudadano\\n\\"Actúa como un docente de ciencias sociales y ciudadanía. Genera 3 preguntas detonantes y reflexivas sobre la convivencia democrática en el colegio para que los estudiantes respondan en un foro o muro colaborativo. Asegúrate de que las preguntas motiven a los estudiantes más tímidos a dar su opinión.\\""\n  },\n  {\n    "doc_id": "DOC-17",\n    "pista_num": "17",\n    "titulo_full": "Pista 17: El Receso de los Chistes",\n    "titulo": "Pista 17: El Receso de los Chistes",\n    "titulo_corto": "El Receso de los Chistes",\n    "area": "Matemáticas y Física (Innovación y Humor)",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "El profesor decidió institucionalizar los últimos 5 minutos de su clase como \'el receso de chistes\'. Usó la risa y el buen humor como la mejor estrategia para liberar el estrés, conectar con los jóvenes y hacer amables las materias más exigentes.",\n    "estrategia": "Incorporar pausas de humor y acertijos lógicos en clase: usar juegos de palabras, adivinanzas numéricas o pequeños chistes al final de temas complejos para mantener un ambiente de aula relajado y motivante.",\n    "prompt": "🤖 Prompt para Pausas de Humor Educativo y Acertijos Lógicos\\n\\"Actúa como un profesor lúdico de matemáticas. Diseña una lista de 3 acertijos lógicos y juegos de palabras matemáticos breves para usar como pausa activa o cierre relajante de clase (de 5 minutos). Cada acertijo debe incluir su solución explicada de forma sencilla y divertida.\\""\n  },\n  {\n    "doc_id": "DOC-18",\n    "pista_num": "18",\n    "titulo_full": "Pista 18: Museos sin Fronteras",\n    "titulo": "Pista 18: Museos sin Fronteras",\n    "titulo_corto": "Museos sin Fronteras",\n    "area": "Educación Artística y Plástica",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "La docente aprovechó la tecnología para llevar a sus estudiantes a recorridos virtuales por más de 80 museos del mundo desde la pantalla. Luego, los guió para recrear las obras de arte con pintura, cartón y materiales reciclables de su propia casa.",\n    "estrategia": "Conectar la exploración estética digital con la creación plástica manual: mostrar imágenes o videos breves de obras famosas y proponer retos de creación con materiales reciclables que los alumnos tengan a la mano.",\n    "prompt": "🤖 Prompt para Apreciación Artística y Creación con Reciclaje\\n\\"Actúa como una profesora creativa de educación artística. Diseña una guía de trabajo de 30 minutos donde los estudiantes observen una obra de arte o escultura famosa y luego la recreen usando elementos reciclables del hogar (cajas, tapas, papel). Incluye 2 preguntas para reflexionar sobre lo que sintieron al crear.\\""\n  },\n  {\n    "doc_id": "DOC-19",\n    "pista_num": "19",\n    "titulo_full": "Pista 19: El Títere que Aprendió a Enseñar",\n    "titulo": "Pista 19: El Títere que Aprendió a Enseñar",\n    "titulo_corto": "El Títere que Aprendió a Enseñar",\n    "area": "Inglés y Ciencias en Educación Infantil",\n    "album": "Álbum 2: La Alquimia Pedagógica",\n    "vivencia": "Para captar la atención de los más pequeños, la profe creó a \'Mr. Whiskers\', un gatito títere que solo hablaba inglés. Además, animó con herramientas sencillas los dibujos de los niños, llenándolos de orgullo y ganas de participar.",\n    "estrategia": "Usar personajes guiados y proyectos creativos animados: incorporar un títere o personaje simbólico para hacer preguntas curiosas e interactuar con los alumnos en idiomas o ciencias.",\n    "prompt": "🤖 Prompt para Personajes Pedagógicos e Indagación Curiosa\\n\\"Actúa como una educadora e investigadora en didáctica infantil. Diseña el guion breve de presentación (2 minutos) para un personaje de títere o mascota del aula que le enseñe a los niños curiosidades sobre los animales o la naturaleza en inglés. Incluye 2 preguntas interactivas para hacerle al grupo.\\""\n  }\n]'

def cargar_pistas():
    return json.loads(PISTAS_EMBEDDED)

pistas = cargar_pistas()

# ENCABEZADO
st.markdown('<div class="title-urban-neon">🎙️ Sintonía Docente</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-thesis">SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA</div>', unsafe_allow_html=True)

# BARRA LATERAL
st.sidebar.markdown("<h2 style='color:#39FF14; font-family:"Caveat", cursive;'>🎙️ Sintonía Docente</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#00F0FF; font-size:0.88em; font-weight:600;'>Ecosistema Transmedia de Resignificación</p>", unsafe_allow_html=True)
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
        album_txt = pista_actual.get("album", "")
        titulo_txt = pista_actual.get("titulo", "")
        area_txt = pista_actual.get("area", "")
        doc_id_txt = pista_actual.get("doc_id", "")
        
        if album_txt == "Álbum 1: El Latido en el Silencio":
            header_class = "album-header-1"
            album_color = "#00F0FF"
        else:
            header_class = "album-header-2"
            album_color = "#FF007F"
            
        st.markdown(f"""
        <div class="{header_class}">
            <span style="background-color:{album_color}; color:#000000; font-weight:bold; padding:4px 12px; border-radius:12px; font-size:0.85em;">{album_txt}</span>
            <h2 style="color:#FFFFFF; margin-top:8px; margin-bottom:5px; text-shadow:0 0 8px {album_color};">{titulo_txt}</h2>
            <p style="color:#E0E0E0; font-size:1.02em; margin:0;">📚 <b>Área Curricular:</b> {area_txt} &nbsp;|&nbsp; 🆔 <b>Código:</b> {doc_id_txt}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # BUSCADOR DE AUDIO FLEXIBLE
        doc_code = pista_actual.get("doc_id", "DOC-01")
        doc_num = pista_actual.get("pista_num", "01")
        doc_num_int = str(int(doc_num)) if doc_num.isdigit() else doc_num
        pista_code = f"pista_{doc_num}"
        
        posibles_rutas = [
            f"sintonia_docente/{doc_code}.mp3",
            f"sintonia_docente/{pista_code}.ogg",
            f"sintonia_docente/{pista_code}.mp4",
            f"sintonia_docente/{pista_code}.mp3",
            f"sintonia_docente/{doc_num}.mp3",
            f"sintonia_docente/{doc_num}.ogg",
            f"{pista_code}.ogg",
            f"{pista_code}.mp4",
            f"{pista_code}.mp3",
            f"{doc_code}.mp3"
        ]
        
        audio_encontrado = None
        for ruta in posibles_rutas:
            if os.path.exists(ruta):
                audio_encontrado = ruta
                break
                
        if not audio_encontrado:
            for folder in ["sintonia_docente", "audio", "."]:
                if os.path.exists(folder):
                    for fname in sorted(os.listdir(folder)):
                        fn_lower = fname.lower()
                        if fn_lower.endswith((".mp3", ".wav", ".m4a", ".ogg", ".mp4")):
                            if (doc_code.lower() in fn_lower or 
                                f"pista_{doc_num}" in fn_lower or 
                                f"pista_{doc_num_int}" in fn_lower or 
                                fn_lower.startswith(f"{doc_num}.") or 
                                fn_lower.startswith(f"{doc_num_int}.")):
                                audio_encontrado = os.path.join(folder, fname)
                                break
                    if audio_encontrado:
                        break

        st.markdown("<h4 style='color:#39FF14; margin-bottom:8px;'>🎙️ Reproductor del Relato Sonoro:</h4>", unsafe_allow_html=True)
        if audio_encontrado:
            st.audio(audio_encontrado)
        else:
            st.info(f"🎧 **Audio detectado:** Al colocar el archivo de audio (`{doc_code}.mp3` o `pista_{doc_num}.ogg`) en la carpeta `sintonia_docente`, este reproductor lo cargará automáticamente.")

        st.divider()

        # ESTRUCTURA EN DOS CAJITAS INDEPENDIENTES (LADO A LADO)
        col_v, col_e = st.columns(2, gap="medium")
        
        vivencia_txt = pista_actual.get("vivencia", "")
        estrategia_txt = pista_actual.get("estrategia", "")
        prompt_txt = pista_actual.get("prompt", "")
        
        with col_v:
            st.markdown(f"""
            <div class="box-vivencia">
                <div class="box-title-v">💬 Vivencia del Profe:</div>
                <div class="box-text">{vivencia_txt}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col_e:
            st.markdown(f"""
            <div class="box-estrategia">
                <div class="box-title-e">💡 Estrategia de Aula Replicable:</div>
                <div class="box-text">{estrategia_txt}</div>
            </div>
            """, unsafe_allow_html=True)

        # SECCIÓN DEL PROMPT - ÚNICA VEZ (CON BOTÓN COPIAR INTEGRADO)
        st.markdown('<div class="prompt-header">🤖 Prompt de Inteligencia Artificial Sugerido (Listo para usar):</div>', unsafe_allow_html=True)
        st.code(prompt_txt, language="markdown")

with tab_catalogo:
    st.markdown("<h3 style='color:#39FF14;'>📚 Compendio de las 19 Fichas Pedagógicas de la Investigación</h3>", unsafe_allow_html=True)
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
    st.markdown("<h3 style='color:#39FF14;'>ℹ️ Sobre el Ecosistema Transmedia 'Sintonía Docente'</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Investigación:** SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA  
    **Investigadora:** Catalina Díaz Chíquiza  
    **Asesora:** Mg. Lady Johana Gómez Bernal  
    **Institución:** Universidad de Nariño — Maestría en Educación Virtual (e-MEV)  

    ---

    ### 🎯 Propósito del Ecosistema Transmedia
    Este producto comunicativo de devolución pedagógica (Objetivo 3) recopila y sistematiza los sentidos y vivencias construidos por 19 docentes de instituciones educativas privadas de Popayán tras la transición forzada a la educación virtual y su retorno a las aulas presenciales e híbridas.

    Cada ficha integra:
    1. **The memoria sensible y el relato narrativo** del docente (Lado humano y emocional).
    2. **La estrategia pedagógica de aula** (Transferibilidad didáctica).
    3. **Un Prompt de Inteligencia Artificial Generativa** diseñado para apoyar el trabajo docente diario.
    """)
