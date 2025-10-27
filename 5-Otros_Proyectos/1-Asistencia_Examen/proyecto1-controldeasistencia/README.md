# Proyecto 1 – Sistema de Control de Asistencia

## Fase 0: Registro de dominio y configuración inicial del VPS

Este documento detalla los primeros pasos del proyecto, que incluyen desde el registro del dominio hasta la configuración básica del servidor en la nube.

---

## Registro del dominio .com.ar

1. Ingreso a [NIC Argentina](https://nic.ar)
2. Creación de cuenta y verificación de identidad
3. Registro del dominio y validación del nombre deseado
4. Configuración inicial en el panel de NIC

---

## Creación del VPS (Droplet en DigitalOcean)

1. Creación de cuenta en [DigitalOcean](https://digitalocean.com)
2. Generación del droplet con sistema operativo Debian 12 x64
3. Asignación de IP pública
4. Verificación de conexión por consola y actualización del sistema

---

## Configuración de acceso SSH

1. Generación de clave pública y privada en Debian local (`ssh-keygen`)
2. Subida de clave pública al VPS (`ssh-copy-id`)
3. Verificación de conexión sin contraseña (`ssh usuario@ip -p puerto`)
4. Edición del archivo `/etc/ssh/sshd_config`:
    - Cambio de puerto SSH (ej: `Port 4202`)
    - Deshabilitar autenticación por contraseña: `PasswordAuthentication no`
    - Deshabilitar acceso root: `PermitRootLogin no`
5. Reinicio del servicio SSH

---

## Configuración del firewall UFW

1. Instalación de UFW (`sudo apt install ufw`)
2. Permitir puerto SSH personalizado: `sudo ufw allow 4202/tcp`
3. (Opcional) Permitir HTTP/HTTPS: `sudo ufw allow 80/tcp` y `443/tcp`
4. Activación del firewall: `sudo ufw enable`
5. Verificación del estado: `sudo ufw status`

---

## Resultado de la Fase 0

Servidor VPS en funcionamiento, acceso SSH por clave con puerto personalizado y firewall activo. Listo para avanzar con la Fase 1 del desarrollo del sistema.

---

## 📁 Autor

**charlyporty**  
Proyecto 1 – Sistema de Control de Asistencia  
Versión documentada: Fase 0
# proyecto1-controldeasistencia
# proyecto1-controldeasistencia
