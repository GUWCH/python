height = input('height:');
height = int(height);
weight =input('weight');
weight = int(weight);
BMI = weight/height**2;
if BMI<18.5:
	print('过轻');
elif