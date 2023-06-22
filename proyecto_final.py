import RPi.GPIO as GPIO
import time

LED_RED_PIN = 17
LED_GREEN_PIN = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)


print("-----Bienvenido al Sistema SynAmb-----")

flotilla = {"Amb1": ["TUM a cargo: Henry", "Escuadra: 4 técnicos", "Unidad 1", "Ubicación: Corregidora, Qro", "Disponible"],
"Amb2": ["TUM a cargo: Argelia", "Escuadra: 3 técnicos", "Unidad 2", "Ubicación: El Marqués, Qro", "No Disponible"],
"Amb3": ["TUM a cargo: Jennifer", "Escuadra: 4 técnicos", "Unidad 3", "Ubicación: Zibatá, Qro", "Disponible"]}

while True:
	try:
		GPIO.output(LED_GREEN_PIN, GPIO.LOW)
		GPIO.output(LED_RED_PIN, GPIO.LOW)
		print("Tiene 3 ambulancias dadas de alta en el sistema")
		print("ID´s: Amb1, Amb2, Amb3")
		print("Para conocer el status de la ambulancia")
		ambulance = input("Escriba el ID correspondiente: ")
		if ambulance in flotilla:
			for each_one in flotilla[ambulance]:
				print(each_one)
			if "Disponible" in flotilla[ambulance]:
				GPIO.output(LED_GREEN_PIN, GPIO.HIGH)
				GPIO.output(LED_RED_PIN, GPIO.LOW)
				time.sleep(7)
			else:
				GPIO.output(LED_GREEN_PIN, GPIO.LOW)
				GPIO.output(LED_RED_PIN, GPIO.HIGH)
				time.sleep(7)
		else:
			print("Esa ambulancia no se encuentra disponible")
			GPIO.output(LED_GREEN_PIN, GPIO.LOW)
			GPIO.output(LED_RED_PIN, GPIO.LOW)
	except KeyboardInterrupt:
		GPIO.cleanup()

	continue_program = input("Desea buscar otra ambulancia? (Si/No): ")
	if continue_program == "No":
		GPIO.cleanup()
		break
