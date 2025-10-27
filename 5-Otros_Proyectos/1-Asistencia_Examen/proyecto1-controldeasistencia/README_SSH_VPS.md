# 🔐 Gestión de Clave SSH Personalizada para VPS

Este documento explica cómo generar una nueva clave SSH sin borrar la anterior, y cómo configurarla para conectarte a tu servidor VPS de forma segura.

---

## 🛠️ Paso 1: Generar una nueva clave SSH

Ejecutar en tu terminal:

```bash
ssh-keygen -t ed25519 -C "charly_vps" -f ~/.ssh/id_ed25519_vps
```

- `-t ed25519`: crea una clave segura y moderna.
- `-C "charly_vps"`: comentario que identifica la clave.
- `-f ~/.ssh/id_ed25519_vps`: nombre del archivo (para no sobrescribir claves existentes).

Cuando se te pregunte por passphrase, podés dejarlo en blanco (Enter) o ingresar una clave si querés mayor seguridad.

---

## 📤 Paso 2: Subir la clave pública al servidor VPS

```bash
ssh-copy-id -i ~/.ssh/id_ed25519_vps.pub usuario@IP_o_HOST_DEL_SERVIDOR
```

> Reemplazá:
> - `usuario`: tu usuario en el VPS (ej: `root` o `charly`)
> - `IP_o_HOST_DEL_SERVIDOR`: IP o dominio de tu servidor VPS

Esto añadirá tu clave pública a `~/.ssh/authorized_keys` del servidor.

---

## ⚙️ Paso 3: Configurar el archivo SSH local (`~/.ssh/config`)

Editar (o crear) el archivo:

```bash
nano ~/.ssh/config
```

Agregar:

```sshconfig
Host mi-vps
    HostName IP_o_HOST_DEL_SERVIDOR
    User usuario
    IdentityFile ~/.ssh/id_ed25519_vps
```

> Podés cambiar `mi-vps` por cualquier alias que prefieras (ej: `vps-charly`).

---

## 🔗 Paso 4: Conectarse al VPS usando la nueva clave

Desde tu terminal:

```bash
ssh mi-vps
```

Este comando usará automáticamente la clave `~/.ssh/id_ed25519_vps`.

---

## 🔎 Paso 5: Verificar claves en el servidor (opcional)

Una vez conectado al VPS:

```bash
cat ~/.ssh/authorized_keys
```

Verificá que tu nueva clave (con comentario `charly_vps`) esté presente.

---

## 🧹 Extra: Eliminar claves viejas (si ya no las usás)

En tu PC:

```bash
rm ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.pub
```

En el VPS (desde `authorized_keys`):

```bash
nano ~/.ssh/authorized_keys
```

Y eliminá la línea correspondiente a la clave antigua.

---

## ✅ Resultado

✔️ Tenés múltiples claves SSH funcionando en paralelo, organizadas y seguras.

---

### ✍️ Autor

**Carlos César Portillo** (alias `charlyporty`)  
🚀 Proyecto de automatización y trabajo remoto con VPS y GitHub
