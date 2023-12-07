The authors of the **RGB** part of a **RELLIS-3D: A Multi-modal Dataset for Off-Road Robotics** address the critical need for semantic scene understanding in off-road environments to ensure robust and safe autonomous navigation. Recognizing the scarcity of multimodal off-road data in existing autonomy datasets, they present RELLIS-3D—a multimodal dataset collected in an off-road setting, specifically on the Rellis Campus of Texas A&M University. This dataset includes annotations for 13,556 LiDAR scans and 6,235 images, introducing challenges related to class imbalance and environmental topography for existing algorithms. Furthermore, the authors conduct evaluations of state-of-the-art deep learning semantic segmentation models on RELLIS-3D, revealing the unique challenges it poses compared to datasets focused on urban environments. The dataset aims to provide researchers with the resources necessary to advance algorithms and explore new research directions for enhancing autonomous navigation in off-road scenarios.

<img src="https://github.com/dataset-ninja/rellis-3d-rgb/assets/78355358/674ed0ae-e522-49b0-8148-5d9956207d28" alt="image" width="400">

<span style="font-size: smaller; font-style: italic;">Warthog Platform Configuration. Illustration of the dimensions and mounting positions of the sensors with respect to the robot body. (Units: cm)</span>

The sensor setup and calibration involve various instruments:
* 1 × Ouster OS1 LiDAR: 64 Channels, 2048 horizontal resolution, 10 Hz, 45◦ vertical field of view.
* 1 × Velodyne Ultra Puck: 32 Channels, 10hz, 40◦ vertical field of view.
* 1 × Nerian Karmin2 + Nerian SceneScan: 3D Stereo Camera, 10 hz.
* 1 × RGB Camera: Basler acA1920-50gc camera with 16mm/F18 EDMUND Optics lens, image resolution 1920x1200, 10 hz.
* Inertial Navigation System (GPS/IMU): Vectornav VN-300 Dual Antenna GNSS/INS, 300 Hz GPS, 100 Hz IMU.

The platform, Warthog, features two computers—one for robotic control and another for data collection and sensor processing. The synchronization of sensors and computers is achieved using Precision Time Protocol (PTP). Camera calibration is performed using the ROS Camera Calibrator library for intrinsic camera calibration, and the extrinsic calibration between sensors is determined using established methods.

<img src="https://github.com/dataset-ninja/rellis-3d-rgb/assets/78355358/e45693be-1410-4ac9-9f41-88a825613c88" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Ground truth annotations examples provided in the RELLIS-3D dataset. Images are densely annotated with pixel-wise labels from 20 different visual classes. LiDAR scans are point-wise labeled with the same ontology.</span>

RELLIS-3D consists of five traversal sequences recorded on non-paved trails of the Ground Research facility, each presenting distinct environmental challenges. The dataset ontology includes object and terrain classes, derived from the [RUGD dataset](http://rugd.vision/), but expanded to encompass unique classes relevant to off-road scenarios. Annotations were provided by Appen through crowdsourcing, with trained annotators ensuring consistency. Both pixel-wise image annotations and point-wise annotations for 3D point clouds are included in the dataset. The authors highlight the statistics of the dataset, emphasizing the imbalanced class distribution, which is common in datasets used for semantic segmentation, but is more severe in off-road environments compared to urban settings. 

The authors present detailed statistics on class distribution for both image and point cloud annotations, shedding light on the challenges posed by the unique characteristics of off-road environments.

<img src="https://github.com/dataset-ninja/rellis-3d-rgb/assets/78355358/32af1a72-ecc2-4749-b578-745a08cd9c5a" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;"><i>Left</i> - Image Label distribution. The sky, grass, tree and bush constitute the major classes. <i>Right</i> - Point Cloud Label distribution. The grass, tree, and bush also dominate the population. </span>