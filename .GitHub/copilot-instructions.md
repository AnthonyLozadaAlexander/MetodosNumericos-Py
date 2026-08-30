# Instrucciones para GitHub Copilot

## Idioma
Siempre responde y genera contenido en **español**.

---

## Mensajes de Commit

Al generar mensajes de commit, sigue estrictamente estas reglas:

### Formato obligatorio

```
<tipo>(<alcance>): <descripción corta en imperativo>

<cuerpo explicativo>

<notas adicionales o referencias (si aplica)>
```

### Tipos de commit permitidos
- `feat` → Nueva funcionalidad
- `fix` → Corrección de un error o bug
- `docs` → Cambios solo en documentación
- `style` → Cambios de formato (espacios, comas, punto y coma) sin afectar lógica
- `refactor` → Reestructuración del código sin cambiar comportamiento
- `test` → Añadir o corregir pruebas
- `chore` → Tareas de mantenimiento (dependencias, configuraciones, etc.)
- `perf` → Mejoras de rendimiento

### Reglas para la descripción corta
- Escrita en **español**, en modo **imperativo** (ej: "Agrega", "Corrige", "Elimina")
- Máximo **72 caracteres**
- No terminar con punto
- Debe ser **específica** y describir QUÉ cambia

### Reglas para el cuerpo
- Separado de la descripción por **una línea en blanco**
- Explica el **POR QUÉ** del cambio, no solo el qué
- Describe el **contexto** del problema que se resuelve
- Menciona el **impacto** del cambio si es relevante
- Si hay cambios en múltiples archivos, listarlos brevemente
- Máximo **80 caracteres por línea**

### Notas adicionales (opcional)
- Referencias a issues: `Cierra #123`, `Relacionado con #456`
- Cambios que rompen compatibilidad: `BREAKING CHANGE: <descripción>`

---

## Ejemplos de commits correctos

**Ejemplo 1 — Nueva funcionalidad:**
```
feat(ErroresNumericos): Agrega cálculo del error de truncamiento

Se implementa la función `calcularErrorTruncamiento` que estima
el error introducido al aproximar una serie infinita con un número
finito de términos. Esto es necesario para comparar la precisión
de los métodos numéricos implementados en el módulo.

Archivos modificados:
- src/ErroresNumericos/ErrorTruncamiento.py (nuevo)
```

**Ejemplo 2 — Corrección de bug:**
```
fix(Numpy): Corrige la transposición incorrecta de matrices

La operación de transposición usaba el índice equivocado al iterar
sobre las columnas, produciendo resultados erróneos en matrices
no cuadradas. Se ajusta el bucle para intercambiar correctamente
filas y columnas.

Cierra #12
```

**Ejemplo 3 — Refactorización:**
```
refactor(ErroresAproximacion): Extrae lógica común de cálculo de errores

Se mueve la validación de entradas y el cálculo base de error a una
función auxiliar `_validar_y_calcular`, compartida por los módulos
`Aproximacion.py`, `calculoError.py` y `sumaError.py`. Esto reduce
la duplicación de código y facilita el mantenimiento futuro.
```

---

- NUNCA OLVIDES ESTE ARCHIVO DIRIGO A GITHUB COPILOT-INSTRUCTIONS.MD, PARA QUE LOS COMMITS SIEMPRE SEAN EN ESPANIOL

## Qué NO hacer en commits
- ❌ No usar inglés en el mensaje de commit
- ❌ No escribir mensajes vagos como "cambios", "update", "fix stuff"
- ❌ No omitir el cuerpo cuando el cambio tiene cierta complejidad
- ❌ No mezclar múltiples cambios no relacionados en un solo commit
- ❌ No usar tiempo pasado ("Agregué", "Corregí"); usar imperativo ("Agrega", "Corrige")
