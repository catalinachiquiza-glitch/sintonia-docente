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
