print('01 - Type DC for DC parameter Calculation: ')
print('02 - Type AC1 for AC Single Phase Parameter Calculation: ')
print('03 - Type AC3 for Three-Phase Parameter Calculation: ')
input1 = input('Current Type: ')

root3 = 1.733

current_type = input1.upper()

'''DC Calculation '''

if current_type == 'DC':
	print('01 - Type C for Current Calculation')
	print('02 - Type V for Voltage Calculation')
	print('03 - Type P for Power Calculation')
	input1 = input('What you went to Calculate: ')
	type1 = input1.upper()
	
	if type1 == "C":
		voltage = float(input('Total Voltage: '))
		power = float(input('Total Power: '))
		current1 = power/voltage
		current = round(current1,2)
		print('Total Current = '+str(current) + ' Amp')
		
	if type1 == 'V':
		current = float(input('Total Current: '))
		power = float(input('Total Power: '))
		voltage1 = power/current
		voltage = round(voltage1,2)
		print('Total Voltage = ' + str(voltage) + ' Volt')
		
	if type1 == 'P':
		voltage = float(input('Total Voltage: '))
		current = float(input('Total Current: '))
		power1 = current*voltage
		power = round(power1,2)
		print('Total Power = ' + str(power) + ' Watt')

'''AC Single-Phase Calculation '''

if current_type == "AC1":
	print('01 - Type C for Current Calculation.')
	print('02 - Type V for Voltage Calculation.')
	print('03 - Type P for Power Calculation.')
	print('04 - Type PF for Power Factor Calculation.')
	input1 = input('What you went to Calculate: ')
	type1 = input1.upper()
	
	if type1 == "C":
		voltage = float(input('Total Voltage: '))
		power = float(input('Total Power: '))
		power_factor = float(input('Total Power Factor: '))
		if power_factor > 1:
			print('power factor is not more than 01')
		else:
		    current1 = power/(voltage*power_factor)
		    current = round(current1,2)
		    print('Total Current = '+str(current) + ' Amp')
		    
		    
	if type1 == 'V':
		current = float(input('Total Current: '))
		power = float(input('Total Power: '))
		power_factor = float(input('Total Power Factor: '))
		if power_factor > 1:
			print('power factor is not more than 01')
		else:
		    voltage1 = power/(current*power_factor)
		    voltage = round(voltage1,2)
		    print('Total Voltage = '+str(voltage) + ' Volt')
		    
		    
	if type1 == 'P':
		voltage = float(input('Total Voltage: '))
		current = float(input('Total Current: '))
		power_factor = float(input('Total Power Factor: '))
		if power_factor > 1:
			print('power factor is not more than 01')
		else:
		    power1 = voltage*current*power_factor
		    power = round(power1,2)
		    print('Total Power = '+str(power) + ' Watt')
		    
		    
	if type1 == 'PF':
		T_power = float(input('True Power: '))
		A_power = float(input('Apparent Power: '))
		
		if T_power>A_power:
			print('True power is always less than Apparent Power')
		else:
		    power_factor01 = T_power/A_power
		    power_factor = round(power_factor01,2)
		    print('Power Factor  = '+str(power_factor) + ' ϑ')

'''AC Three-Phase Calculation '''

if current_type == "AC3":
	print('01 - Type C for Current Calculation.')
	print('02 - Type V for Voltage Calculation.')
	print('03 - Type P for Power Calculation.')
	print('04 - Type PF for Power Factor Calculation.')
	input1 = input('What you went to Calculate: ')
	type1 = input1.upper()
	
	if type1 == "C":
		voltage = float(input('Total Voltage: '))
		power = float(input('Total Power: '))
		power_factor = float(input('Total Power Factor: '))
		if power_factor > 1:
			print('power factor is not more than 01')
		else:
		    current1 = power/(root3*voltage*power_factor)
		    current = round(current1,3)
		    print('Total Current = '+str(current) + ' Amp')
		    
		    
	if type1 == 'V':
		current = float(input('Total Current: '))
		power = float(input('Total Power: '))
		power_factor = float(input('Total Power Factor: '))
		if power_factor > 1:
			print('power factor is not more than 01')
		else:
		    voltage1 = power/(root3*current*power_factor)
		    voltage = round(voltage1,2)
		    print('Total Voltage = '+str(voltage) + ' Volt')
		    
		    
	if type1 == 'P':
		voltage = float(input('Total Voltage: '))
		current = float(input('Total Current: '))
		power_factor = float(input('Total Power Factor: '))
		if power_factor > 1:
			print('power factor is not more than 01')
		else:
		    power1 = voltage*current*power_factor*root3
		    power = round(power1,2)
		    print('Total Power = '+str(power) + ' Watt')
		    
		    
	if type1 == 'PF':
		T_power = float(input('True Power: '))
		A_power = float(input('Apparent Power: '))
		
		if T_power>A_power:
			print('True power is always less than Apparent Power')
		else:
		    power_factor01 = T_power/A_power
		    power_factor = round(power_factor01,2)
		    print('Power Factor  = '+str(power_factor) + ' ϑ')
	