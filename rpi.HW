import RPi.GPIO as GPIO
import time

# Mengatur mode GPIO ke BCM
GPIO.setmode(GPIO.BCM)

# Pin yang digunakan untuk koneksi sensor ultrasonik
TRIGGER_PIN = 17
ECHO_PIN = 27

# Setup pin sebagai OUTPUT dan INPUT
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    # Mengirimkan sinyal ultrasonik
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    # Mendapatkan waktu awal dan akhir menerima sinyal balik
    pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Menghitung durasi sinyal balik
    pulse_duration = pulse_end - pulse_start

    # Menghitung jarak berdasarkan kecepatan suara
    sound_speed = 34300  # Kecepatan suara dalam cm/s
    distance = (pulse_duration * sound_speed) / 2

    return distance

try:
    while True:
        distance = get_distance()
        print(f"Jarak: {distance:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    # Mengatasi keyboard interrupt dengan membersihkan GPIO
    GPIO.cleanup()
