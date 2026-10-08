import streamlit as st
import os
import json

st.set_page_config(
    page_title="Sintonía Docente - Ecosistema Transmedia",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Sedgwick+Ave+Display&family=Rock+Salt&family=Kalam:wght@700&display=swap');

    .stApp {
        background-color: #121212 !important;
        background-image: 
            radial-gradient(circle at 50% 20%, rgba(57, 255, 20, 0.08) 0%, transparent 60%),
            linear-gradient(335deg, rgba(0,0,0,0.85) 0%, rgba(20,20,20,0.6) 100%),
            repeating-linear-gradient(0deg, transparent, transparent 25px, rgba(0,0,0,0.4) 26px, rgba(0,0,0,0.4) 27px),
            repeating-linear-gradient(90deg, rgba(255,255,255,0.03), rgba(255,255,255,0.03) 50px, rgba(0,0,0,0.5) 51px, rgba(0,0,0,0.5) 52px) !important;
        color: #FFFFFF !important;
        font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #0A0D12 !important;
        border-right: 2px solid #2ECC71 !important;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 2px solid #2ECC71 !important;
    }
    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 1.05em !important;
    }
    ul[data-baseweb="menu"] {
        background-color: #FFFFFF !important;
    }
    ul[data-baseweb="menu"] li {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    .title-neon-urban {
        font-family: 'Permanent Marker', 'Sedgwick Ave Display', 'Rock Salt', cursive;
        color: #39FF14;
        font-size: 3.2em;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 5px;
        letter-spacing: 2px;
        text-shadow: 
            0 0 6px rgba(57, 255, 20, 0.6),
            0 2px 4px rgba(0, 0, 0, 0.9);
    }
    
    .subtitle-neon {
        color: #E0E0E0;
        font-size: 1.05em;
        text-align: center;
        font-weight: 600;
        margin-bottom: 25px;
        letter-spacing: 1px;
    }

    .stage-card {
        background: linear-gradient(135deg, rgba(20,25,35,0.95) 0%, rgba(10,12,18,0.95) 100%);
        padding: 20px 24px;
        border-radius: 16px;
        border: 2px solid #2ECC71;
        box-shadow: 0 0 15px rgba(46, 204, 113, 0.25);
        margin-bottom: 20px;
    }

    .box-vivencia {
        background-color: #1A2332;
        padding: 20px;
        border-radius: 14px;
        border-left: 5px solid #00F0FF;
        border-top: 1px solid rgba(0,240,255,0.2);
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        color: #F0F4F8;
        font-size: 1.02em;
        line-height: 1.6;
        min-height: 180px;
    }

    .box-estrategia {
        background-color: #1E293B;
        padding: 20px;
        border-radius: 14px;
        border-left: 5px solid #39FF14;
        border-top: 1px solid rgba(57,255,20,0.2);
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        color: #F0F4F8;
        font-size: 1.02em;
        line-height: 1.6;
        min-height: 180px;
    }

    .box-prompt {
        background-color: #1A1228;
        padding: 22px;
        border-radius: 14px;
        border: 2px solid #FF007F;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.25);
        color: #FFB3D9;
        font-size: 1.05em;
        line-height: 1.6;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #39FF14 !important;
    }
</style>
""", unsafe_allow_html=True)

PISTAS_DATA = [
  {
    "doc_id": "DOC-01",
    "pista_num": "01",
    "titulo_full": "Pista 01: Las Voces Anónimas del Corazón",
    "titulo_corto": "Las Voces Anónimas del Corazón",
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
    "titulo_full": "Pista 04: Ventanas Abiertas a la Cotidianidad",
    "titulo_corto": "Ventanas Abiertas a la Cotidianidad",
    "area": "Educación Inicial y Preescolar",
    "album": "Álbum 1: El Latido en el Silencio",
    "vivencia": "Con niños de preescolar, la profe transformó la rutina guiando las actividades paso a paso con imágenes sencillas y diapositivas coloridas. Descubrió que coordinarse con las familias y mantener la ternura en cada instrucción era la clave para que los más pequeños se sintieran seguros y motivados.",
    "estrategia": "Estructurar secuencias visuales claras y cortas: combinar adivinanzas, pausas musicales y guías visuales sencillas para la familia, asegurando que cada niño avance a su propio ritmo sin saturarse.",
    "prompt": "🤖 Prompt para Experiencias de Aprendizaje Visual e Infantil\n\"Actúa como una maestra experta en educación inicial. Ayúdame a diseñar una secuencia didáctica de 20 minutos basada en imágenes y cuentos breves para niños de preescolar. La actividad debe incluir una pausa activa de movimiento corporal y una recomendación práctica para coordinar fácilmente con los padres de familia.\""
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
    "prompt": "🤖 Prompt para Generar Historias y Casos Cotidianos en Sociales\n\"Actúa como un profesor apasionado de ciencias sociales. Dame 3 ejemplos de relatos breves o dilemas sencillos basados en la vida cotidiana para explicar a niños de primaria la importancia de la convivencia y los derechos en la comunidad. Incluye preguntas orientadoras para abrir una conversación agradable en el salón.\""
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
    "prompt": "🤖 Prompt para Pausas Activas y Circuitos Motrices Sencillos\n\"Actúa como un entrenador pedagógico y profesor de educación física. Diseña un circuito de 4 estaciones de movimiento y flexibilidad pensado para realizarse en espacios pequeños usando objetos cotidianos (sillas, botellas de agua). Describe cada ejercicio con instrucciones breves y divertidas para los estudiantes.\""
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
    "prompt": "🤖 Prompt para Indagación Guiada en Ciencias y Física\n\"Actúa como un docente de ciencias exactas que busca hacer la física fácil y entretenida. Diseña una actividad de indagación de 20 minutos usando una situación común del hogar o un simulador interactivo gratuito. Formula 3 preguntas cotidianas que lleven al estudiante a deducir el concepto principal sin usar jerga matemática compleja.\""
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
    "prompt": "🤖 Prompt para Cuentos Interactivos y Ludificación Infantil\n\"Actúa como una educadora infantil experta en juego y literatura. Crea una idea para adaptar un cuento corto tradicional en una experiencia interactiva donde los niños participen haciendo sonidos, gestos o dibujando en un papel. Incluye 2 pausas de movimiento para mantenerlos atentos.\""
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
    "prompt": "🤖 Prompt para Talleres de Lectura Crítica y Creación Análoga\n\"Actúa como un profesor de literatura enfocado en el aprendizaje manipulativo y humano. Diseña un taller de lectura y escritura de 30 minutos donde los estudiantes analicen un poema o cuento corto usando materiales físicos (papel, colores, tijeras) para construir un diario ilustrado. Explica el paso a paso de forma clara.\""
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
    "prompt": "🤖 Prompt para Experimentos Caseros e Indagación Científica\n\"Actúa como un biólogo y educador científico. Diseña una guía para un experimento casero completamente seguro que los estudiantes puedan realizar con elementos de la cocina (como sal, agua, aceite o plantas). Incluye la lista de materiales, 3 preguntas de hipótesis y una forma sencilla de presentar sus observaciones.\""
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
    "prompt": "🤖 Prompt para Juegos Matemáticos y Pensamiento Numérico\n\"Actúa como una maestra experta en didáctica de las matemáticas para primaria. Diseña una actividad gamificada de 15 minutos llamada 'El mercado del aula' para practicar sumas y restas básicas usando fichas o papelitos. Incluye las reglas del juego y 3 retos numéricos divertidos adaptados a niños.\""
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
    "prompt": "🤖 Prompt para Análisis de Casos y Debate Ciudadano\n\"Actúa como un docente de ciencias sociales enfocado en el pensamiento crítico. Diseña una actividad de debate breve (20 minutos) basada en una noticia sencilla sobre el cuidado del medio ambiente en la ciudad. Incluye 3 preguntas contrapuestas para guiarlos y pautas para que dialoguen con respeto.\""
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
    "prompt": "🤖 Prompt para Pensamiento Computacional Desenchufado (*Unplugged*)\n\"Actúa como un profesor de tecnología e informática. Diseña una dinámica de pensamiento computacional sin necesidad de computadores (*unplugged*) para explicar qué es un algoritmo usando la preparación de una receta o un juego de pasos en el salón. Describe la instrucción paso a paso de forma amena.\""
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
    "prompt": "🤖 Prompt para Decálogos de Convivencia y Acuerdos Pedagógicos\n\"Actúa como un directivo docente enfocado en el clima escolar positivo. Ayúdame a redactar un decálogo amigable de 5 acuerdos de convivencia digital y uso responsable del celular en el aula, redactado en un lenguaje positivo, claro y motivador para estudiantes y familias.\""
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
    "prompt": "🤖 Prompt para Evaluación Formativa de la Expresión Oral\n\"Actúa como docente de lenguaje y lectura. Diseña una pauta sencilla de retroalimentación oral en 3 pasos para evaluar cuando un estudiante cuenta un cuento o expone una idea frente al grupo. La pauta debe enfocarse en resaltar lo positivo, hacer una pregunta para profundizar y motivarlo a seguir hablando.\""
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
    "prompt": "🤖 Prompt para Muros de Opinión y Diálogo Ciudadano\n\"Actúa como un docente de ciencias sociales y ciudadanía. Genera 3 preguntas detonantes y reflexivas sobre la convivencia democrática en el colegio para que los estudiantes respondan en un foro o muro colaborativo. Asegúrate de que las preguntas motiven a los estudiantes más tímidos a dar su opinión.\""
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
    "prompt": "🤖 Prompt para Pausas de Humor Educativo y Acertijos Lógicos\n\"Actúa como un profesor lúdico de matemáticas. Diseña una lista de 3 acertijos lógicos y juegos de palabras matemáticos breves para usar como pausa activa o cierre relajante de clase (de 5 minutos). Cada acertijo debe incluir su solución explicada de forma sencilla y divertida.\""
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
    "prompt": "🤖 Prompt para Apreciación Artística y Creación con Reciclaje\n\"Actúa como una profesora creativa de educación artística. Diseña una guía de trabajo de 30 minutos donde los estudiantes observen una obra de arte o escultura famosa y luego la recreen usando elementos reciclables del hogar (cajas, tapas, papel). Incluye 2 preguntas para reflexionar sobre lo que sintieron al crear.\""
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
    "prompt": "🤖 Prompt para Personajes Pedagógicos e Indagación Curiosa\n\"Actúa como una educadora e investigadora en didáctica infantil. Diseña el guion breve de presentación (2 minutos) para un personaje de títere o mascota del aula que le enseñe a los niños curiosidades sobre los animales o la naturaleza en inglés. Incluye 2 preguntas interactivas para hacerle al grupo.\""
  }
]

st.markdown('<div class="title-neon-urban">🎙️ Sintonía Docente</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-neon">SINTONÍA DOCENTE: VOCES Y RESIGNIFICACIONES DE LA PRÁCTICA PEDAGÓGICA EN ENTORNOS TECNOLÓGICOS POSTPANDEMIA</div>', unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='color:#39FF14; font-family:\"Permanent Marker\", cursive;'>🎙️ Sintonía Docente</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#E0E0E0; font-size:0.9em; font-style:italic;'>Ecosistema Transmedia de Resignificación</p>", unsafe_allow_html=True)
st.sidebar.divider()

modo_vista = st.sidebar.radio(
    "📌 Selecciona la Colección:",
    ["Álbum 1: El Latido en el Silencio (DOC-01 a DOC-08)", 
     "Álbum 2: La Alquimia Pedagógica (DOC-09 a DOC-19)", 
     "Ver Todas las 19 Fichas Pedagógicas"]
)

if "Álbum 1" in modo_vista:
    pistas_filtradas = [p for p in PISTAS_DATA if p["album"] == "Álbum 1: El Latido en el Silencio"]
elif "Álbum 2" in modo_vista:
    pistas_filtradas = [p for p in PISTAS_DATA if p["album"] == "Álbum 2: La Alquimia Pedagógica"]
else:
    pistas_filtradas = PISTAS_DATA

opciones_titulos = [p["titulo_full"] for p in pistas_filtradas]

st.sidebar.markdown("<p style='color:#39FF14; font-weight:bold; margin-top:15px; font-size:1.1em;'>🎵 Selecciona la Pista Sonora:</p>", unsafe_allow_html=True)

pista_seleccionada_titulo = st.sidebar.selectbox(
    "Despliega para elegir la pista:",
    opciones_titulos,
    index=0
)

pista_actual = next((p for p in pistas_filtradas if p["titulo_full"] == pista_seleccionada_titulo), PISTAS_DATA[0])

tab_reproductor, tab_catalogo, tab_metodologia = st.tabs([
    "🎙️ Reproductor y Ficha Pedagógica", 
    "📚 Catálogo Completo (19 Fichas)", 
    "ℹ️ Acerca del Ecosistema"
])

with tab_reproductor:
    if pista_actual:
        doc_code = pista_actual["doc_id"]
        pista_num = pista_actual["pista_num"]
        
        st.markdown(f'''
        <div class="stage-card">
            <span style="background-color:#39FF14; color:#000000; font-weight:bold; padding:5px 14px; border-radius:12px; font-size:0.9em;">{pista_actual["album"]}</span>
            <h2 style="color:#39FF14; margin-top:12px; margin-bottom:6px; font-family:'Permanent Marker', cursive;">{pista_actual["titulo_full"]}</h2>
            <p style="color:#E0E0E0; font-size:1.1em; margin:0;">📚 <b>Área Curricular:</b> {pista_actual["area"]} | 🏷️ <b>Código Anónimo:</b> {doc_code}</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#39FF14; margin-bottom:10px;'>🎙️ Escuchar Relato Sonora:</h4>", unsafe_allow_html=True)
        
        posibles_rutas = [
            f"sintonia_docente/{doc_code}.mp3",
            f"sintonia_docente/pista_{pista_num}.ogg",
            f"sintonia_docente/pista_{pista_num}.mp4",
            f"sintonia_docente/pista_{pista_num}.mp3",
            f"sintonia_docente/{doc_code.lower()}.mp3",
            f"pista_{pista_num}.ogg",
            f"pista_{pista_num}.mp4",
            f"pista_{pista_num}.mp3",
            f"{doc_code}.mp3"
        ]
        
        audio_encontrado = None
        for ruta in posibles_rutas:
            if os.path.exists(ruta):
                audio_encontrado = ruta
                break
                
        if audio_encontrado:
            st.audio(audio_encontrado)
        else:
            st.info(f"🎧 **Audio listo para reproducir:** Al colocar el archivo de audio en la carpeta `sintonia_docente` (ej. `pista_{pista_num}.ogg` o `{doc_code}.mp3`), sonará aquí de inmediato.")

        st.divider()

        # DOS CAJITAS INDEPENDIENTES (LADO A LADO)
        col_vivencia, col_estrategia = st.columns(2)
        
        with col_vivencia:
            st.markdown("<h4 style='color:#00F0FF; margin-bottom:8px;'>💬 Vivencia del Profe:</h4>", unsafe_allow_html=True)
            st.markdown(f'''
            <div class="box-vivencia">
                {pista_actual["vivencia"]}
            </div>
            ''', unsafe_allow_html=True)
            
        with col_estrategia:
            st.markdown("<h4 style='color:#39FF14; margin-bottom:8px;'>💡 Estrategia de Aula:</h4>", unsafe_allow_html=True)
            st.markdown(f'''
            <div class="box-estrategia">
                {pista_actual["estrategia"]}
            </div>
            ''', unsafe_allow_html=True)

        # CAJITA ABAJO (ANCHO COMPLETO): PROMPT DE IA
        st.markdown("<h4 style='color:#FF007F; margin-top:20px; margin-bottom:8px;'>🤖 Prompt de Inteligencia Artificial Sugerido:</h4>", unsafe_allow_html=True)
        st.markdown(f'''
        <div class="box-prompt">
            {pista_actual["prompt"]}
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown("**📋 Haz clic para copiar el Prompt de IA listo para usar:**")
        st.code(pista_actual["prompt"], language="markdown")

with tab_catalogo:
    st.markdown("<h3 style='color:#39FF14;'>📚 Compendio de las 19 Fichas Pedagógicas de la Investigación</h3>", unsafe_allow_html=True)
    st.write("Explora las vivencias, estrategias y prompts de los docentes participantes de Popayán (DOC-01 a DOC-19).")
    
    search_term = st.text_input("🔍 Buscar por palabra clave (ej. inglés, matemáticas, inicial, títere, juego):", "")
    
    for p in PISTAS_DATA:
        if not search_term or search_term.lower() in p["titulo_full"].lower() or search_term.lower() in p["area"].lower() or search_term.lower() in p["vivencia"].lower():
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

    Este repositorio sonoro y pedagógico recopila las vivencias, padecimientos y resignificaciones de 19 docentes de instituciones privadas de Popayán durante y después de la pandemia por COVID-19.
    """)
