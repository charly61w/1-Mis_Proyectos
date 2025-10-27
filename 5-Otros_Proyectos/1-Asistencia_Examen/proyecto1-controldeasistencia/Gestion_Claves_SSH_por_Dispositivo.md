# Gestión de claves SSH por dispositivo

Esta guía tiene como objetivo ayudarte a manejar correctamente tus claves SSH cuando trabajás desde múltiples dispositivos (por ejemplo, notebook, PC de escritorio, VPS). Usar claves separadas por dispositivo mejora la seguridad y el control de acceso.

---

## 🔑 ¿Qué es una clave SSH?

Un par de claves SSH está compuesto por:

- **Clave privada (`id_ed25519` o `id_rsa`)**: solo debe estar en tu dispositivo.
- **Clave pública (`id_ed25519.pub` o `id_rsa.pub`)**: se comparte con los servidores o servicios (GitHub, VPS, etc.).

---

## ✅ Recomendación: una clave por dispositivo

Generá una clave diferente para cada computadora desde la que trabajes. Esto permite:
- Revocar el acceso de un solo dispositivo si lo perdés o dejás de usarlo.
- Llevar un control más claro de qué dispositivo accede a qué sistema.

---

## 🛠 Cómo generar una clave SSH en cada dispositivo

```bash
ssh-keygen -t ed25519 -C "charlyporty@notebook"
# o
ssh-keygen -t ed25519 -C "charlyporty@escritorio"
```

Presioná Enter en todas las opciones para usar la ruta por defecto (`~/.ssh/id_ed25519`).

---

## 📤 Subir clave pública al servidor (ej: VPS)

```bash
ssh-copy-id -p 4202 usuario@IP_DEL_VPS
```

Esto copia la clave pública al archivo `~/.ssh/authorized_keys` del servidor.

---

## 🌐 Subir clave pública a GitHub

1. Entrá a [https://github.com](https://github.com)
2. Ir a **Settings → SSH and GPG Keys**
3. Clic en **New SSH key**
4. Pegá el contenido de tu `~/.ssh/id_ed25519.pub`
5. Poné un nombre identificador (ej: "Notebook Debian", "Escritorio Casa")

---

## 🔍 Verificar conexión SSH con GitHub

```bash
ssh -T git@github.com
```

Si todo funciona, deberías ver algo como:
> Hi charlyporty! You've successfully authenticated.

---

## ❌ ¿Y si un dispositivo se pierde o ya no lo usás?

Simplemente entrás a GitHub, vas a la sección de claves SSH y eliminás esa clave. Lo mismo podés hacer en tu VPS, borrando la línea correspondiente en `~/.ssh/authorized_keys`.

---

## 🧠 Buenas prácticas

- No compartas claves privadas entre dispositivos.
- Usá frases identificadoras (`-C "nombre@dispositivo"`) para saber de dónde es cada clave.
- Hacé backups seguros de tus claves si es necesario.
- Revocá inmediatamente cualquier clave de un dispositivo perdido.

---

## 📁 Autor

**charlyporty**  
Guía: Gestión de claves SSH por dispositivo  
Proyecto 1 – Sistema de Control de Asistencia
