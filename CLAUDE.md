# Proyecto Autos (Alerce) — contexto inicial

Notas trasladadas desde una conversación previa (24 de agosto de 2026) para arrancar este proyecto sin perder contexto. Nace igual que [Radar Comercial](https://github.com/agenciaaimpacto-cyber/radar-comercial) y [Danny Mera Seguros](https://github.com/agenciaaimpacto-cyber/dannymeraseguros): un frente de negocio nuevo, separado intencionalmente en su propia carpeta.

**Estado: recién empieza.** Danny no tiene experiencia previa en venta de autos — la oportunidad se presentó el 24 de agosto de 2026 y quiere partir rápido (dijo textualmente "no sé nada, porque recién pasó hoy, pero quiero hacerlo y vender mucho").

**Ruta local:** `/Users/danny/negocio autos` (carpeta creada por Danny directamente fuera de `~/Documents` — ya sigue la regla aprendida en Radar Comercial de no ubicar proyectos con automatización dentro de Documentos/Escritorio/Descargas, ver nota técnica en el CLAUDE.md de Danny Mera Seguros si en algún momento se necesita algo corriendo en local vía `launchd`).

## El negocio: agente libre en consignación de autos

Danny se suma como agente libre (freelance) de una automotora en el sector de Alerce (Puerto Montt, Región de Los Lagos). No es dueño de la automotora ni tiene relación de dependencia — es un vendedor externo que capta autos y clientes, y la automotora pone el trato, la logística de venta y se queda con un porcentaje.

**Estructura de comisiones ofrecida por la automotora:**
- Venta de auto al contado: **$100.000** de comisión por auto vendido.
- Venta de auto con crédito: **$150.000** de comisión por auto vendido.
- **Consignación (el modelo con más potencial):** si Danny consigue que un dueño le entregue su auto en consignación (el dueño quiere vender con la automotora), Danny pacta un precio con ese dueño. Si el auto se termina vendiendo a un comprador por un precio mayor al pactado, la automotora se queda con el **2% del precio de venta final**, y **la diferencia entre el precio pactado con el dueño y el precio de venta final (menos ese 2%) es la ganancia de quien consiguió la consignación** — en este caso, Danny.

**Ejemplo trabajado (para tener la mecánica clara, no es un caso real de cliente):**
- Precio pactado con el dueño del auto: $5.000.000
- Precio de venta final a un comprador: $6.000.000
- Comisión de la automotora (2% de $6.000.000): $120.000
- Diferencia entre pactado y venta final: $1.000.000
- Ganancia de Danny: $1.000.000 − $120.000 = **$880.000**

**Por qué este modelo y no comprar-arreglar-vender (el modelo "Kia" que Danny ya probó una vez):**
- Consignación: $0 de capital invertido, $0 de riesgo financiero, el trabajo es 100% gestión digital (conseguir el auto + conseguir el comprador). Se pueden tener varios autos en proceso a la vez sin necesitar más capital.
- Comprar-arreglar-vender: inmoviliza capital (ej. ~$2.000.000 por auto) durante semanas, riesgo de que el arreglo salga más caro, depende de mecánico/repuestos/tiempo físico. No es el perfil de Danny (su patrón ya confirmado en otros negocios: todo lo que hace funciona desde el computador, sin capital en riesgo, escalable a otras ciudades sin depender de su presencia física).

## Plan de expansión
- **Alerce (Puerto Montt):** primer frente, con la automotora que hizo la oferta. Meta: operativo desde el jueves siguiente a esta conversación (27 de agosto de 2026).
- **Punta Arenas:** mismo modelo, replicado con el hermano de Danny. Es el paso lógico siguiente, pero **después** de que Alerce esté funcionando — no arrancar los dos frentes a la vez (más [Danny Mera Seguros](../DannyMeraSeguros) sigue activo en paralelo, con agosto 2026 recién cerrando). El orden importa: no sobrecargar el sistema.

## Número de WhatsApp
Decisión tomada en la conversación previa: usar el mismo número que ya usa para campañas (+56 9 5793 8503, el mismo que aparece en Danny Mera Seguros), pero separando las conversaciones con una etiqueta/carpeta específica en WhatsApp Business (ej. "Autos Alerce") para no mezclar leads de seguros con leads de autos en el mismo hilo. No se justifica un número nuevo hasta validar que el modelo funciona con el primer cierre real.

Razonamiento sobre por qué esto no genera bloqueo de Meta: los leads inician el contacto (por anuncio), Danny responde — es el flujo más seguro para WhatsApp Business. Lo que sí genera bloqueos es mensajería masiva no solicitada, algo que este flujo no hace.

## Sitio / landing (este proyecto)
Igual que con Seguros, la idea es que un sitio simple sea la capa de confianza para quien llega desde WhatsApp o desde un anuncio — no un catálogo de autos ni una tienda transaccional todavía, solo lo suficiente para que el lead confíe y siga la conversación.

**Decisiones tomadas para la primera versión (24 de agosto de 2026, sin más información disponible — ajustar cuando Danny tenga más detalles):**
- **Nombre/marca:** "Danny Mera Autos", por consistencia con "Danny Mera Seguros" (no confirmado explícitamente por Danny, es el default más razonable — cambiar si Danny prefiere otro nombre).
- **Automotora de Alerce:** se mantiene genérica en el sitio ("una automotora establecida en Alerce"), sin nombrarla — mismo criterio que en Seguros con los bancos/casas comerciales, para no dar detalles de un tercero sin su autorización explícita.
- **Público del sitio:** dos audiencias en una sola landing —
  1. Dueños de auto que quieren venderlo (consignación) — mensaje: gestión completa, sin costo para vender, sin las vueltas de venderlo por cuenta propia.
  2. Compradores de auto (contado o crédito).
- **No se exponen los números internos de comisión** (100k/150k/2%) en el sitio público — esa es información del negocio de Danny con la automotora, no algo que el cliente necesite ver.
- **Sin casos reales todavía** (recién parte) — la landing es de captación/validación, no de prueba social. Agregar casos reales cuando existan los primeros cierres.

## Cómo seguir
Al abrir una sesión de Claude Code en esta carpeta, este archivo da el contexto — se puede pedir directamente "seguimos con el proyecto de autos" y continuar desde acá. Si Danny confirma nombre de marca, si quiere nombrar la automotora, o si el número de WhatsApp cambia, actualizar este archivo.

Si más adelante se decide replicar el patrón técnico completo de Radar Comercial / Danny Mera Seguros (repo en GitHub, deploy automático en Netlify, posible automatización de contenido), seguir la misma guía documentada en el `CLAUDE.md` de Danny Mera Seguros, sección "Cómo se configuró Radar Comercial (guía técnica reutilizable)" — aplica igual acá.
