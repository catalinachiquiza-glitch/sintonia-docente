import streamlit as st
import os
import json

# Configuración de la página
st.set_page_config(
    page_title="Sintonía Docente - Ecosistema",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS - Pared de ladrillos, Neón Verde en Freestyle Script, Menú con letra negra
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Permanent+Marker&family=Rock+Salt&display=swap');

    /* Fondo general estilo Pared de Ladrillos en Escenario Oscuro */
    .stApp {
        background-color: #0d0d11 !important;
        background-image: 
            linear-gradient(rgba(13, 13, 17, 0.88), rgba(13, 13, 17, 0.92)),
            radial-gradient(circle at 50% 20%, rgba(57, 255, 20, 0.08) 0%, transparent 60%),
            repeating-linear-gradient(0deg, transparent, transparent 24px, rgba(255, 255, 255, 0.03) 25px),
            repeating-linear-gradient(90deg, transparent, transparent 48px, rgba(255, 255, 255, 0.03) 50px) !important;
        color: #F0F4F8 !important;
        font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #121620 !important;
        border-right: 2px solid #39FF14 !important;
        box-shadow: 2px 0 15px rgba(57, 255, 20, 0.15);
    }
    [data-testid="stSidebar"] * {
        color: #F0F4F8 !important;
    }
    
    /* MENÚ DESPLEGABLE (SELECTBOX) - LETRA NEGRA SIEMPRE */
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

    /* TÍTULO PRINCIPAL - FREESTYLE SCRIPT / CURSIVA CALLEJERA NEÓN VERDE */
    .title-neon {
        font-family: 'Freestyle Script', 'Caveat', 'Permanent Marker', cursive !important;
        font-size: 3.4em !important;
        font-weight: 700;
        color: #39FF14 !important;
        text-shadow: 0 0 8px #39FF14, 0 0 18px rgba(57, 255, 20, 0.5);
        text-align: center;
        margin-bottom: 2px;
        line-height: 1.1;
    }
    .subtitle-neon {
        font-size: 1.05em;
        color: #00F0FF;
        text-shadow: 0 0 6px #00F0FF;
        text-align: center;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* ENCABEZADOS DE ÁLBUM */
    .album-header-1 {
        background: linear-gradient(135deg, #092235 0%, #113854 100%);
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 2px solid #00F0FF;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.25);
    }
    .album-header-2 {
        background: linear-gradient(135deg, #350922 0%, #541138 100%);
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 2px solid #FF007F;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.25);
    }

    /* CAJITAS INDEPENDIENTES (VIVENCIA Y ESTRATEGIA) */
    .box-vivencia {
        background-color: #121824;
        border-radius: 14px;
        padding: 20px;
        border: 2px solid #00F0FF;
        box-shadow: 0 0 12px rgba(0, 240, 255, 0.2);
        height: 100%;
    }
    .box-estrategia {
        background-color: #121d18;
        border-radius: 14px;
        padding: 20px;
        border: 2px solid #39FF14;
        box-shadow: 0 0 12px rgba(57, 255, 20, 0.2);
        height: 100%;
    }
    .box-title-vivencia {
        color: #00F0FF;
        font-size: 1.2em;
        font-weight: 800;
        margin-bottom: 12px;
        text-shadow: 0 0 6px rgba(0, 240, 255, 0.4);
    }
    .box-title-estrategia {
        color: #39FF14;
        font-size: 1.2em;
        font-weight: 800;
        margin-bottom: 12px;
        text-shadow: 0 0 6px rgba(57, 255, 20, 0.4);
    }
    .box-text {
        color: #F0F4F8;
        font-size: 1.02em;
        line-height: 1.6;
    }

    /* BADGES */
    .ficha-badge {
        background: linear-gradient(90deg, #39FF14 0%, #00F0FF 100%);
        color: #000000 !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 0.9em;
        display: inline-block;
        margin-bottom: 12px;
    }
    .area-badge {
        background-color: #1F293D;
        color: #00F0FF !important;
        border: 1px solid #00F0FF;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9em;
        display: inline-block;
        margin-left: 8px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# 19 FICHAS ANÓNIMAS EMBEBIDAS
PISTAS = [
    {
        "doc_id": "DOC-01",
        "pista_num": "01",
        "titulo_full": "Pista 01: El Corazón De Las Voces Anónimas",
        "titulo": "Pista 01: El Corazón De Las Voces Anónimas",
        "titulo_corto": "El Corazón De Las Voces Anónimas",
        "area": "Francés y Lenguas Extranjeras",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "En medio del aislamiento y la timidez inicial de hablar en pantalla, surgió un ejercicio de escritura en el que los estudiantes pudieron expresar de forma sincera sus temores y emociones sin temor al qué dirán. La profe descubrió que el lenguaje es, ante todo, un puente para conectarse con la vida de los muchachos.",
        "estrategia": "Proponer actividades reales y vivenciales en lengua extranjera: los alumnos describen su ropa favorita, objetos significativos de su habitación o lugares de su casa mediante dinámicas de participación cercana y respetuosa.",
        "prompt": "🤖 Prompt para Práctica de Idiomas y Expresión Cotidiana\n\"Actúa como un profesor cercano y entusiasta de lenguas extranjeras. Diseña un ejercicio práctico de 15 minutos para que mis estudiantes describan en el idioma que aprenden objetos cotidianos de su entorno o prendas de vestir. Incluye 3 preguntas sencillas de calentamiento y una rúbrica cualitativa enfocada en la confianza y el esfuerzo comunicativo más que en la perfección gramatical.\""
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
        "prompt": "🤖 Prompt para Dinámicas Lúdicas y Vocabulario con Objetos Reales\n\"Actúa como docente especialista en didáctica de inglés para primaria. Diseña una guía con 4 dinámicas breves de juego activo usando objetos comunes del aula o del hogar (ropa, útiles, juguetes) para repasar vocabulario básico. Cada dinámica debe durar menos de 10 minutos y promover la participación espontánea sin presionar al niño.\""
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
        "prompt": "🤖 Prompt para Círculos de Palabra y Acompañamiento Socioemocional\n\"Actúa como un orientador escolar y profesor de humanidades. Diseña una guía de 15 minutos para realizar un círculo de palabra afectivo al inicio de la jornada con estudiantes. Incluye 3 preguntas sencillas y cálidas para abrir el diálogo sobre cómo se sienten y un cierre reflexivo que fomente la empatía en el grupo.\""
    },
    {
        "doc_id": "DOC-04",
        "pista_num": "04",
        "titulo_full": "Pista 04: Tarjetas Pequeñas para Manos Grandes",
        "titulo": "Pista 04: Tarjetas Pequeñas para Manos Grandes",
        "titulo_corto": "Tarjetas Pequeñas para Manos Grandes",
        "area": "Educación Inicial y Preescolar",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "Con niños de preescolar, la profe transformó la rutina guiando las actividades paso a paso con imágenes sencillas y diapositivas coloridas. Descubrió que coordinarse con las familias y mantener la ternura en cada instrucción era la clave para que los más pequeños se sintieran seguros y motivados.",
        "estrategia": "Estructurar secuencias visuales claras y cortas: combinar adivinanzas, pausas musicales y guías visuales sencillas para la familia, asegurando que cada niño avance a su propio ritmo sin saturarse.",
        "prompt": "🤖 Prompt para Experiencias de Aprendizaje Visual e Infantil\n\"Actúa como una maestra experta en educación inicial. Ayúdame a diseñar una secuencia didáctica de 20 minutos basada en imágenes y cuentos breves para niños de preescolar. La actividad debe incluir una pausa activa de movimiento corporal y una recomendación práctica para coordinar fácilmente con los padres de familia.\""
    },
    {
        "doc_id": "DOC-05",
        "pista_num": "05",
        "titulo_full": "Pista 05: La Maestra del Tablero que Aprendió a Grabarse",
        "titulo": "Pista 05: La Maestra del Tablero que Aprendió a Grabarse",
        "titulo_corto": "La Maestra del Tablero que Aprendió a Grabarse",
        "area": "Ciencias Sociales y Desarrollo Humano (Primaria)",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La docente dio el salto de la clase magistral tradicional al uso de relatos y presentaciones participativas. Recordó con emoción cómo las familias escuchaban sus clases de fondo y cómo pequeños detalles espontáneos permitieron romper la frialdad y acercar la historia a la vida real de sus estudiantes.",
        "estrategia": "Transformar los contenidos teóricos en historias cercanas: utilizar casos cotidianos, imágenes icónicas y preguntas problematizadoras que inviten a los alumnos a dar su opinión y relacionar el tema con su entorno.",
        "prompt": "🤖 Prompt para Generar Historias y Casos Cotidianos en Sociales\n\"Actúa como un profesor apasionado de ciencias sociales. Dame 3 ejemplos de relatos breves o dilemas sencillos basados en la vida cotidiana para explicar a niños de primaria la importancia de la convivencia y los derechos en la comunidad. Incluye preguntas orientadoras para abrir una conversación agradable en el salón.\""
    },
    {
        "doc_id": "DOC-06",
        "pista_num": "06",
        "titulo_full": "Pista 06: Mover el Cuerpo Detrás de la Pantalla",
        "titulo": "Pista 06: Mover el Cuerpo Detrás de la Pantalla",
        "titulo_corto": "Mover el Cuerpo Detrás de la Pantalla",
        "area": "Educación Física, Recreación y Deporte",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "El profesor enfrentó el enorme reto de adaptar la actividad física a espacios reducidos. Con ingenio, utilizó implementos de aseo, elementos del hogar y música motivadora para mantener a los estudiantes activos y saludables, demostrando que el movimiento es bienestar mental.",
        "estrategia": "Diseñar circuitos motrices dinámicos con elementos caseros o del aula: organizar rutinas de ejercicios de bajo impacto, pausas activas y juegos de coordinación usando botellas plásticas, escobas o marcadores.",
        "prompt": "🤖 Prompt para Pausas Activas y Circuitos Motrices Sencillos\n\"Actúa como un entrenador pedagógico y profesor de educación física. Diseña un circuito de 4 estaciones de movimiento y flexibilidad pensado para realizarse en espacios pequeños usando objetos cotidianos (sillas, botellas de agua). Describe cada ejercicio con instrucciones breves y divertidas para los estudiantes.\""
    },
    {
        "doc_id": "DOC-07",
        "pista_num": "07",
        "titulo_full": "Pista 07: Clases para los Abuelos que Terminaron Aprendiendo Matemáticas",
        "titulo": "Pista 07: Clases para los Abuelos que Terminaron Aprendiendo Matemáticas",
        "titulo_corto": "Clases para los Abuelos que Terminaron Aprendiendo Matemáticas",
        "area": "Física y Ciencias Exactas",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "El docente descubrió que al explicar temas complejos como la física, ver a los abuelos y padres sentados al lado de los niños aprendiendo juntos enriquecía el proceso. Perdió el miedo a las herramientas digitales y comenzó a grabar explicaciones breves con pizarras visuales.",
        "estrategia": "Utilizar la indagación guiada con simuladores y experimentos simples: plantear preguntas problema cotidianas (como el movimiento de una bicicleta o el calor de una taza) para explorar los conceptos antes de la fórmula.",
        "prompt": "🤖 Prompt para Indagación Guiada en Ciencias y Física\n\"Actúa como un docente de ciencias exactas que busca hacer la física fácil y entretenida. Diseña una actividad de indagación de 20 minutos usando una situación común del hogar o un simulador interactivo gratuito. Formula 3 preguntas cotidianas que lleven al estudiante a deducir el concepto principal sin usar jerga matemática compleja.\""
    },
    {
        "doc_id": "DOC-08",
        "pista_num": "08",
        "titulo_full": "Pista 08: La Cámara que Se Quedó Encendida",
        "titulo": "Pista 08: La Cámara que Se Quedó Encendida",
        "titulo_corto": "La Cámara que Se Quedó Encendida",
        "area": "Educación Infantil y Dimensión Afectiva",
        "album": "Álbum 1: El Latido en el Silencio",
        "vivencia": "La maestra comprendió la importancia de la empatía y el buen humor en el aula. Usó historias vivas, fondos animados y cuentos interactivos para mantener la chispa del aprendizaje en los niños, aprendiendo que la tecnología debe sumar calidez y no distancia.",
        "estrategia": "Implementar dinámicas de ludificación y cuentos expresivos: intercalar momentos de lectura compartida con pausas de expresión gestual y artística que mantengan la alegría en el salón de clase.",
        "prompt": "🤖 Prompt para Cuentos Interactivos y Ludificación Infantil\n\"Actúa como una educadora infantil experta en juego y literatura. Crea una idea para adaptar un cuento corto tradicional en una experiencia interactiva donde los niños participen haciendo sonidos, gestos o dibujando en un papel. Incluye 2 pausas de movimiento para mantenerlos atentos.\""
    },
    {
        "doc_id": "DOC-09",
        "pista_num": "09",
        "titulo_full": "Pista 09: El Regreso a lo que se Puede Tocar",
        "titulo": "Pista 09: El Regreso a lo que se Puede Tocar",
        "titulo_corto": "El Regreso a lo que se Puede Tocar",
        "area": "Español y Lengua Castellana",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Tras el exceso de pantallas, la profesora decidió hacer una pausa consciente y regresar a lo análogo y manipulativo: recortar, armar, escribir a mano y tocar el papel. Redescubrió que la lectura crítica y la escritura creativa se disfrutan más cuando se sienten en las manos.",
        "estrategia": "Alternar el trabajo digital con talleres análogos y manipulativos: crear diarios de lectura en papel, murales físicos de palabras y álbumes ilustrados hechos a mano por los mismos alumnos.",
        "prompt": "🤖 Prompt para Talleres de Lectura Crítica y Creación Análoga\n\"Actúa como un profesor de literatura enfocado en el aprendizaje manipulativo y humano. Diseña un taller de lectura y escritura de 30 minutos donde los estudiantes analicen un poema o cuento corto usando materiales físicos (papel, colores, tijeras) para construir un diario ilustrado. Explica el paso a paso de forma clara.\""
    },
    {
        "doc_id": "DOC-10",
        "pista_num": "10",
        "titulo_full": "Pista 10: El Laboratorio que Cabía en una Cocina",
        "titulo": "Pista 10: El Laboratorio que Cabía en una Cocina",
        "titulo_corto": "El Laboratorio que Cabía en una Cocina",
        "area": "Ciencias Naturales y Biología",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profesor no dejó morir la curiosidad científica y creó la estrategia de 'El laboratorio en mi cocina'. Con ingredientes caseros como repollo morado, vinagre y bicarbonato, demostró que la ciencia está viva en cualquier rincón del hogar.",
        "estrategia": "Diseñar laboratorios caseros e indagar la naturaleza cercana: proponer pequeñas observaciones científicas con elementos cotidianos para que los estudiantes formulen hipótesis y experimenten sin peligro.",
        "prompt": "🤖 Prompt para Experimentos Caseros e Indagación Científica\n\"Actúa como un biólogo y educador científico. Diseña una guía para un experimento casero completamente seguro que los estudiantes puedan realizar con elementos de la cocina (como sal, agua, aceite o plantas). Incluye la lista de materiales, 3 preguntas de hipótesis y una forma sencilla de presentar sus observaciones.\""
    },
    {
        "doc_id": "DOC-11",
        "pista_num": "11",
        "titulo_full": "Pista 11: El Gato que se Robó el Saludo",
        "titulo": "Pista 11: El Gato que se Robó el Saludo",
        "titulo_corto": "El Gato que se Robó el Saludo",
        "area": "Matemáticas en Primaria (1° a 3°)",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente utilizó ruletas virtuales, juegos con semillas y desafíos de tienda escolar para que los niños de primaria perdieran el miedo a los números. Comprendió que cuando las matemáticas se juegan y se tocan, el aprendizaje perdura.",
        "estrategia": "Gamificar el pensamiento numérico con material concreto: organizar retos de cálculo mental rápido usando fichas, juegos de mercado escolar y tableros interactivos sencillos.",
        "prompt": "🤖 Prompt para Juegos Matemáticos y Pensamiento Numérico\n\"Actúa como una maestra experta en didáctica de las matemáticas para primaria. Diseña una actividad gamificada de 15 minutos llamada 'El mercado del aula' para practicar sumas y restas básicas usando fichas o papelitos. Incluye las reglas del juego y 3 retos numéricos divertidos adaptados a niños.\""
    },
    {
        "doc_id": "DOC-12",
        "pista_num": "12",
        "titulo_full": "Pista 12: Cumpleaños Compartidos a Través de la Pantalla",
        "titulo": "Pista 12: Cumpleaños Compartidos a Través de la Pantalla",
        "titulo_corto": "Cumpleaños Compartidos a Través de la Pantalla",
        "area": "Ciencias Sociales e Historia / Bilingüismo",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La profesora organizó momentos humanos memorables, como celebrar cumpleaños a través de las pantallas o debatir noticias actuales. Aprendió a sintetizar los contenidos en presentaciones breves para dar más tiempo a la conversación rica entre estudiantes.",
        "estrategia": "Implementar cuadros comparativos y análisis de casos reales: utilizar diapositivas breves para presentar ideas clave y abrir de inmediato espacio para el debate de opinión y la reflexión en grupos.",
        "prompt": "🤖 Prompt para Análisis de Casos y Debate Ciudadano\n\"Actúa como un docente de ciencias sociales enfocado en el pensamiento crítico. Diseña una actividad de debate breve (20 minutos) basada en una noticia sencilla sobre el cuidado del medio ambiente en la ciudad. Incluye 3 preguntas contrapuestas para guiarlos y pautas para que dialoguen con respeto.\""
    },
    {
        "doc_id": "DOC-13",
        "pista_num": "13",
        "titulo_full": "Pista 13: Cámaras Encendidas, Mentes Abiertas",
        "titulo": "Pista 13: Cámaras Encendidas, Mentes Abiertas",
        "titulo_corto": "Cámaras Encendidas, Mentes Abiertas",
        "area": "Tecnología e Informática",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profe tomó la decisión humanizada de priorizar la sustentación oral y la lógica de los alumnos por encima de exigir cámaras encendidas a quienes tenían mala conexión. Enseñó que la tecnología debe estar al servicio de las personas y no al revés.",
        "estrategia": "Desarrollar el pensamiento computacional sin pantallas (actividades *unplugged*): usar juegos de lógica con tarjetas, instrucciones paso a paso humanas y diálogos donde el alumno explique cómo solucionó un problema.",
        "prompt": "🤖 Prompt para Pensamiento Computacional Desenchufado (*Unplugged*)\n\"Actúa como un profesor de tecnología e informática. Diseña una dinámica de pensamiento computacional sin necesidad de computadores (*unplugged*) para explicar qué es un algoritmo usando la preparación de una receta o un juego de pasos en el salón. Describe la instrucción paso a paso de forma amena.\""
    },
    {
        "doc_id": "DOC-14",
        "pista_num": "14",
        "titulo_full": "Pista 14: La Impotencia de No Poder Ver Aprender",
        "titulo": "Pista 14: La Impotencia de No Poder Ver Aprender",
        "titulo_corto": "La Impotencia de No Poder Ver Aprender",
        "area": "Coordinación Académica y Pedagogía Infantil",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "La docente utilizó Paint como su tablero digital hecho a mano para explicar a su manera. Como directiva, construyó acuerdos de paciencia y confianza con los maestros y familias, recordando que la gestión educativa debe ser siempre cercana y comprensiva.",
        "estrategia": "Construir decálogos de convivencia y acuerdos claros de aula: establecer pautas amables para la escucha activa, la participación organizada y el uso con sentido de las herramientas digitales.",
        "prompt": "🤖 Prompt para Decálogos de Convivencia y Acuerdos Pedagógicos\n\"Actúa como un directivo docente enfocado en el clima escolar positivo. Ayúdame a redactar un decálogo amigable de 5 acuerdos de convivencia digital y uso responsable del celular en el aula, redactado en un lenguaje positivo, claro y motivador para estudiantes y familias.\""
    },
    {
        "doc_id": "DOC-15",
        "pista_num": "15",
        "titulo_full": "Pista 15: Cuadernos Frente a la Cámara",
        "titulo": "Pista 15: Cuadernos Frente a la Cámara",
        "titulo_corto": "Cuadernos Frente a la Cámara",
        "area": "Lengua Castellana y Proceso Lecto-Escritor",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "En los grados iniciales, la maestra estableció rutinas claras de escucha y normas sencillas para tomar la palabra. Descubrió que al combinar la lectura de cuentos con presentaciones sencillas, los niños fortalecieron enormemente su expresión verbal.",
        "estrategia": "Evaluar mediante sustentación oral y diálogo guiado: hacer preguntas cortas al final de las lecturas para que los alumnos cuenten con sus propias palabras lo que entendieron y compartan sus reflexiones.",
        "prompt": "🤖 Prompt para Evaluación Formativa de la Expresión Oral\n\"Actúa como docente de lenguaje y lectura. Diseña una pauta sencilla de retroalimentación oral en 3 pasos para evaluar cuando un estudiante cuenta un cuento o expone una idea frente al grupo. La pauta debe enfocarse en resaltar lo positivo, hacer una pregunta para profundizar y motivarlo a seguir hablando.\""
    },
    {
        "doc_id": "DOC-16",
        "pista_num": "16",
        "titulo_full": "Pista 16: El Silencio que Empezó a Escribir",
        "titulo": "Pista 16: El Silencio que Empezó a Escribir",
        "titulo_corto": "El Silencio que Empezó a Escribir",
        "area": "Ciencias Sociales y Ciencia Política",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "Un estudiante tímido que casi no hablaba en clase presencial comenzó a escribir largos mensajes en el chat para compartir reflexiones muy profundas. La profesora descubrió que la tecnología abrió puertas a nuevas formas de expresión para quienes antes callaban.",
        "estrategia": "Aprovechar espacios de participación escrita y foros de opinión: combinar el diálogo en clase con pequeños muros colaborativos digitales donde los estudiantes respondan preguntas breves a su ritmo.",
        "prompt": "🤖 Prompt para Muros de Opinión y Diálogo Ciudadano\n\"Actúa como un docente de ciencias sociales y ciudadanía. Genera 3 preguntas detonantes y reflexivas sobre la convivencia democrática en el colegio para que los estudiantes respondan en un foro o muro colaborativo. Asegúrate de que las preguntas motiven a los estudiantes más tímidos a dar su opinión.\""
    },
    {
        "doc_id": "DOC-17",
        "pista_num": "17",
        "titulo_full": "Pista 17: La Cámara que Tampoco Prendía",
        "titulo": "Pista 17: La Cámara que Tampoco Prendía",
        "titulo_corto": "La Cámara que Tampoco Prendía",
        "area": "Matemáticas y Física (Innovación y Humor)",
        "album": "Álbum 2: La Alquimia Pedagógica",
        "vivencia": "El profesor decidió institucionalizar los últimos 5 minutos de su clase como 'el receso de chistes'. Usó la risa y el buen humor como la mejor estrategia para liberar el estrés, conectar con los jóvenes y hacer amables las materias más exigentes.",
        "estrategia": "Incorporar pausas de humor y acertijos lógicos en clase: usar juegos de palabras, adivinanzas numéricas o pequeños chistes al final de temas complejos para mantener un ambiente de aula relajado y motivante.",
        "prompt": "🤖 Prompt para Pausas de Humor Educativo y Acertijos Lógicos\n\"Actúa como un profesor lúdico de matemáticas. Diseña una lista de 3 acertijos lógicos y juegos de palabras matemáticos breves para usar como pausa activa o cierre relajante de clase (de 5 minutos). Cada acertijo debe incluir su solución explicada de forma sencilla y divertida.\""
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
        "prompt": "🤖 Prompt para Apreciación Artística y Creación con Reciclaje\n\"Actúa como una profesora creativa de educación artística. Diseña una guía de trabajo de 30 minutos donde los estudiantes observen una obra de arte o escultura famosa y luego la recreen usando elementos reciclables del hogar (cajas, tapas, papel). Incluye 2 preguntas para reflexionar sobre lo que sintieron al crear.\""
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
        "prompt": "🤖 Prompt para Personajes Pedagógicos e Indagación Curiosa\n\"Actúa como una educadora e investigadora en didáctica infantil. Diseña el guion breve de presentación (2 minutos) para un personaje de títere o mascota del aula que le enseñe a los niños curiosidades sobre los animales o la naturaleza en inglés. Incluye 2 preguntas interactivas para hacerle al grupo.\""
    }
]

# FUNCIÓN ROBUSTA DE BÚSQUEDA DE AUDIOS
def buscar_audio_robusto(doc_code, doc_num):
    doc_num_clean = str(int(doc_num)) if doc_num.isdigit() else doc_num
    pista_code = f"Pista_{doc_num}"
    pista_space = f"Pista {doc_num}"
    
    posibles_rutas = [
        f"sintonia_docente/{doc_code}.mp3",
        f"sintonia_docente/{doc_code}.wav",
        f"sintonia_docente/{doc_code}.ogg",
        f"sintonia_docente/{doc_code}.mp4",
        f"sintonia_docente/{doc_code.lower()}.mp3",
        f"sintonia_docente/{doc_code.lower()}.ogg",
        f"sintonia_docente/{pista_code}.mp3",
        f"sintonia_docente/{pista_code}.ogg",
        f"sintonia_docente/{pista_space}.mp3",
        f"sintonia_docente/{pista_space}.ogg",
        f"sintonia_docente/{doc_num}.mp3",
        f"sintonia_docente/{doc_num}.ogg",
        f"audio/{doc_code}.mp3",
        f"audio/{doc_code}.ogg",
        f"{doc_code}.mp3",
        f"{doc_code}.ogg",
        f"pista_{doc_num}.ogg",
        f"pista_{doc_num}.mp3",
        f"pista_{doc_num}.mp4",
        f"pista_{doc_num_clean}.ogg",
        f"pista_{doc_num_clean}.mp3",
        f"pista_{doc_num_clean}.mp4"
    ]
    
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            return ruta
            
    # Búsqueda escaneando carpetas si no hubo coincidencia directa
    for folder in ["sintonia_docente", "audio", "."]:
        if os.path.exists(folder):
            for fname in sorted(os.listdir(folder)):
                fn_lower = fname.lower()
                if fn_lower.endswith((".mp3", ".wav", ".m4a", ".ogg", ".mp4")):
                    if (doc_code.lower() in fn_lower or 
                        doc_code.replace("-", "_").lower() in fn_lower or 
                        f"pista_{doc_num}" in fn_lower or 
                        f"pista {doc_num}" in fn_lower or 
                        f"pista{doc_num}" in fn_lower or 
                        fn_lower.startswith(f"{doc_num}.") or 
                        fn_lower.startswith(f"{doc_num}_") or
                        fn_lower.startswith(f"pista_{doc_num_clean}")):
                        return os.path.join(folder, fname) if folder != "." else fname
    return None

# ENCABEZADO
st.markdown('<div class="title-neon">🎙️ Sintonía Docente</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-neon">SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA</div>', unsafe_allow_html=True)

# BARRA LATERAL
st.sidebar.markdown("<h2 style='color:#39FF14; font-family: Freestyle Script, Caveat, cursive;'>🎙️ Sintonía Docente</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#E0E0E0; font-style:italic;'>Ecosistema de Resignificación Docente</p>", unsafe_allow_html=True)
st.sidebar.divider()

modo_vista = st.sidebar.radio(
    "📌 Selecciona la Colección:",
    ["Álbum 1: El Latido en el Silencio (DOC-01 a DOC-08)", 
     "Álbum 2: La Alquimia Pedagógica (DOC-09 a DOC-19)", 
     "Ver Todas las 19 Fichas Pedagógicas"]
)

if "Álbum 1" in modo_vista:
    pistas_filtradas = [p for p in PISTAS if p.get("album") == "Álbum 1: El Latido en el Silencio"]
elif "Álbum 2" in modo_vista:
    pistas_filtradas = [p for p in PISTAS if p.get("album") == "Álbum 2: La Alquimia Pedagógica"]
else:
    pistas_filtradas = PISTAS

opciones_titulos = [p["titulo"] for p in pistas_filtradas] if pistas_filtradas else ["Sin pistas disponibles"]

st.sidebar.markdown("<p style='color:#39FF14; font-weight:bold; margin-top:15px;'>🎵 Selecciona la Pista Sonora:</p>", unsafe_allow_html=True)

pista_seleccionada_titulo = st.sidebar.selectbox(
    "Despliega para elegir la pista:",
    opciones_titulos,
    index=0
)

pista_actual = next((p for p in pistas_filtradas if p["titulo"] == pista_seleccionada_titulo), PISTAS[0] if PISTAS else {})

# PESTAÑAS PRINCIPALES
tab_reproductor, tab_catalogo, tab_metodologia = st.tabs([
    "🎙️ Reproductor y Ficha Pedagógica", 
    "📚 Catálogo Completo (19 Fichas)", 
    "ℹ️ Acerca de la Investigación"
])

with tab_reproductor:
    if pista_actual:
        album_color = "#00F0FF" if pista_actual.get("album") == "Álbum 1: El Latido en el Silencio" else "#FF007F"
        header_class = "album-header-1" if pista_actual.get("album") == "Álbum 1: El Latido en el Silencio" else "album-header-2"
            
        album_name = pista_actual.get("album", "")
        track_title = pista_actual.get("titulo", "")
        area_name = pista_actual.get("area", "")
        
        st.markdown(
            f'<div class="{header_class}">'
            f'<span style="background-color:{album_color}; color:#000000; font-weight:bold; padding:4px 12px; border-radius:12px; font-size:0.85em;">{album_name}</span>'
            f'<h2 style="color:#FFFFFF; margin-top:10px; margin-bottom:5px; text-shadow:0 0 10px {album_color};">{track_title}</h2>'
            f'<p style="color:#E0E0E0; font-size:1.05em; margin:0;">📚 <b>Área Curricular:</b> {area_name}</p>'
            f'</div>',
            unsafe_allow_html=True
        )
        
        # REPRODUCCIÓN DE AUDIO
        st.markdown("<h4 style='color:#39FF14; margin-bottom:8px;'>🎙️ Reproductor de Voz y Sonido:</h4>", unsafe_allow_html=True)
        
        doc_code = pista_actual.get("doc_id", "DOC-01")
        doc_num = pista_actual.get("pista_num", "01")
        
        audio_encontrado = buscar_audio_robusto(doc_code, doc_num)
                
        if audio_encontrado:
            st.audio(audio_encontrado)
        else:
            st.info(f"🎧 **Audio detectado:** Al colocar la carpeta `sintonia_docente` con los archivos de audio (`{doc_code}.mp3` o `pista_{doc_num}.ogg`), este reproductor los cargará automáticamente.")

        st.markdown("<br>", unsafe_allow_html=True)
        
        # BADGES
        doc_id_val = pista_actual.get("doc_id", "")
        area_val = pista_actual.get("area", "")
        st.markdown(
            f'<div>'
            f'<span class="ficha-badge">CÓDIGO: {doc_id_val}</span>'
            f'<span class="area-badge">ÁREA: {area_val}</span>'
            f'</div>',
            unsafe_allow_html=True
        )
        
        # CAJITAS INDEPENDIENTES EN 2 COLUMNAS
        col1, col2 = st.columns(2)
        
        vivencia_txt = pista_actual.get("vivencia", "")
        estrategia_txt = pista_actual.get("estrategia", "")
        
        with col1:
            st.markdown(
                f'<div class="box-vivencia">'
                f'<div class="box-title-vivencia">💬 Vivencia del Profe:</div>'
                f'<div class="box-text">{vivencia_txt}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            
        with col2:
            st.markdown(
                f'<div class="box-estrategia">'
                f'<div class="box-title-estrategia">💡 Estrategia de Aula Replicable:</div>'
                f'<div class="box-text">{estrategia_txt}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        
        # PROMPT DE IA ÚNICO
        st.markdown("<h4 style='color:#FF007F; margin-bottom:6px;'>🤖 Prompt de Inteligencia Artificial Sugerido (Listo para usar):</h4>", unsafe_allow_html=True)
        st.code(pista_actual.get("prompt", ""), language="markdown")

with tab_catalogo:
    st.markdown("<h3 style='color:#39FF14;'>📚 Compendio de las 19 Fichas Pedagógicas de la Investigación</h3>", unsafe_allow_html=True)
    st.write("Explora de forma directa las vivencias, estrategias y prompts desarrollados a partir de las narrativas de los docentes (DOC-01 a DOC-19).")
    
    search_term = st.text_input("🔍 Buscar por palabra clave (ej. inglés, matemáticas, inicial, títere, juego):", "")
    
    for p in PISTAS:
        if not search_term or search_term.lower() in p["titulo"].lower() or search_term.lower() in p["area"].lower() or search_term.lower() in p["vivencia"].lower():
            with st.expander(f"🔹 {p['doc_id']} — {p['titulo_corto']} | 📚 {p['area']}"):
                st.markdown(f"**Área:** {p['area']}")
                st.markdown(f"**Vivencia del Profe:** {p['vivencia']}")
                st.markdown(f"**Estrategia de Aula:** {p['estrategia']}")
                st.markdown("**Prompt de IA Sugerido:**")
                st.code(p['prompt'], language="markdown")

with tab_metodologia:
    st.markdown("<h3 style='color:#39FF14;'>ℹ️ Acerca de la Investigación</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Investigación:** SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA  
    **Investigadora:** Catalina D. Chíquiza  
    **Asesora:** Mg. Lady Johana Gómez Bernal  
    **Institución:** Universidad de Nariño — Maestría en Educación Virtual (e-MEV)  

    ---

    ### 🎯 Objetivo del Ecosistema:
    El producto comunicativo *Sintonía Docente* ha sido co-construido como una herramienta multimodal y de acceso libre para la comunidad educadora. Cada ficha integra la memoria viva de la pandemia con estrategias didácticas y *prompts* de Inteligencia Artificial diseñados para enriquecer la labor docente actual en entornos presenciales, híbridos y virtuales.

    **Nota Ética:** La totalidad de los relatos ha sido anonimizada bajo la codificación de **DOC-01 a DOC-19** para resguardar la identidad de los maestros participantes de las instituciones educativas privadas de Popayán.
    """)
