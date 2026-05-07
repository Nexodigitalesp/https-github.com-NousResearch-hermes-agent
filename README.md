# NEXO Agent - Nexus Configuration

Este repositorio contiene la configuración especializada para el Agente NEXO (Hermes Nexus), diseñado para gestionar una agencia B2B de outbound y automatizar campañas de GTM.

## Estructura del Proyecto

- `SOUL.md`: Define la identidad, tono y valores del Agente NEXO.
- `AGENTS.md`: Instrucciones operativas detalladas y el workflow GTM de 17 pasos.
- `profiles/`: Directorio que contiene los perfiles aislados de NEXO y sus clientes.
  - `nexo/`: Perfil de la agencia.
  - `heyagencia/`: Perfil de cliente.
  - `naturebrain/`: Perfil de cliente.
  - Cada perfil incluye subcarpetas para `informes/entregables` e `informes/inteligencia`.
- `templates/`: Plantillas estándar para la estrategia de campaña y playbooks de ejecución.
- `scripts/`: Herramientas de automatización para el workflow.
  - `normalize_data.py`: Normalización de nombres y empresas.
  - `bulk_generator.py`: Generación masiva de mensajes personalizados.

## Cómo usar este Nexus

1. **Identidad:** Asegúrate de que Hermes cargue `SOUL.md` como su identidad principal.
2. **Perfiles:** Cuando trabajes para un cliente, navega al directorio del perfil correspondiente (`profiles/{cliente}`) para mantener el contexto aislado.
3. **Workflow GTM:** Sigue los 17 pasos definidos en `AGENTS.md`. Usa las plantillas en `templates/` para documentar cada fase.
4. **Automatización:**
   - Usa `scripts/normalize_data.py` para limpiar los datos de los leads (Paso 11).
   - Usa `scripts/bulk_generator.py` para procesar el "Prompt Maestro" y generar los mensajes finales en CSV (Paso 15).

## Reglas de Oro
- **Mínimo 3 BBDD:** Siempre cruza al menos 3 fuentes de datos por campaña.
- **Fallbacks:** Cada mensaje personalizado DEBE tener una variante genérica.
- **Aprobación Humana:** El agente propone, Asier aprueba. Nunca se escribe a leads sin validación externa.

---
*NEXO Bound - Transformando el Outbound con Inteligencia.*
