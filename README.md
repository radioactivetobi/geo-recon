# Geo-Recon (macOS Setup)

Un instrument de recunoaștere bazat pe Python, adaptat pentru macOS.

## Instalare

1. Clonează repository-ul:
   ```bash
   git clone https://github.com/gordasgdc/geo-recon.git
   cd geo-recon
   ```

2. Instalează binarul Nmap:
   ```bash
   brew install nmap
   ```

3. Creează și activează mediul virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instalează dependențele:
   ```bash
   pip install -r requirements.txt
   ```
