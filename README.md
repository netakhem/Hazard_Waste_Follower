This project focuses on the development of an autonomous robot capable of detecting and responding to four specific types of waste: disposable chopsticks, peach pits, cigarette butts, and toilet paper.
Each item is mapped to a directional command such as forward, backward, left, or right, allowing the robot not only to recognize the object but also to demonstrate a corresponding movement in real time.
To achieve this, a custom dataset was collected and annotated, and the MobileNetV2 architecture was selected for training. 
The trained model was then converted into TensorFlow Lite and deployed on a Raspberry Pi 4 Model 8. 
The model I used is MobileNetv2. 
Hyperparameters:
-	Image size: 224 x 224 
-	Epochs: 30 
-	Batch Size: 32
-	Optimizer: Adam (lr = 1e-4)
-	Augmentations: The following augmentation was applied to create 3 versions of each source image: 
	* 50% probability of horizontal flip
	* Equal probability of one of the following 90-degree rotations: none, clockwise, 		counter-clockwise, upside-down
	* Random brightness adjustment of between -15 and +15 percent
	* Random Gaussian blur of between 0 and 2.5 pixels
