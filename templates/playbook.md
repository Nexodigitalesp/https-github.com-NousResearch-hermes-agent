# Playbook de Ejecución: {Nombre de la Campaña}

## Fase 1: Extracción y List Building
- [ ] Mapeo de TAM en modo lectura (APIs).
- [ ] Extracción de empresas desde 3 BBDD diferentes.
- [ ] Unificación y deduplicación en CSV.
- [ ] Filtrado de falsos positivos (LLM Prompt).

## Fase 2: Búsqueda de Decisores
- [ ] Identificación de 1-2 decisores por empresa.
- [ ] Scraping de emails (si aplica).
- [ ] Normalización de datos (Nombres/Empresas).

## Fase 3: Diseño de Copies
- **Estructura Dinámica:**
  - Canal:
  - Nº de mensajes:
  - Nº de señales:
- **Árbol de Mensajes:**
  - M1: {Variable/Señal} + {Fallback}
  - M2: {Variable/Señal} + {Fallback}
- [ ] Aprobación de Asier (Formato literal requerido).

## Fase 4: Enriquecimiento de Señales
- [ ] Scraping de señales de compra aprobadas (Datos recientes).
- [ ] Generación Bulk de mensajes (Prompt Maestro + API).

## Fase 5: Lanzamiento
- [ ] Merge final de CSV.
- [ ] Configuración en secuenciador {Instantly/Lemlist}.
- [ ] Lanzamiento.
