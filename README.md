# radio-collar-tracker
This is the repository for the Radio Collar Tracker project focusing on RTK GPS integration.

# Project Overview
This project helps to further develop a new method for ecologists and biologists to find radio collar trackers on animals; it was initially started by Engineers for Exploration. We will make modifications to the Global Positioning Satellite (GPS) to increase its accuracy from meter-grade precision down to centimeter-grade. This gives biologists and ecologists better animal location measurements for research.

# Project Approach
In order to increase the GPS precision of the system, we will integrate a Real Time Kinetic (RTK) GPS module developed by Swift Navigation. RTK GPS requires an additional base station for functionality, but results in higher accuracy and consistency. Our team will integrate the RTK GPS hardware into the existing quadcopter, make software modifications to ensure compatibility, and then evaluate the performance improvements between the RTK GPS and the existing GPS. Our team members are Corbin Adelman, Ryan Kral, and Sam Hessenauer. For class papers, each team member will write separate sections initially, then we will review and edit the papers as a group. For the RTK GPS work, we will most commonly work together in-step on various milestones. However, each of us have different specialties and will be assigned to different tasks on the fly as we encounter problems.

# Project Milestones
1. Get up to speed with the Piksi RTK GPS hardware. -4/21/2015
2. Get the RTK GPS working in the field with laptops. -5/5/2015
3. Integrate hardware/software with the quadcopter. -5/19/2015
4. Evaluate performance between GPS and RTK GPS. -5/26/2015
5. Document results. -6/2/2015

# Constraints, Risks, and Feasibility
Integrating the RTK GPS module into the radio collar tracker project will provide instant improvements to the system overall. However, the following main risks must be managed: 
1. Access to hardware for both the RTK GPS module and the quadcopter depend on help from Engineers for Exploration and schedule compatibility
2. We plan to modify GPS code which already exists; there is a risk that this code is poorly written or challenging to comprehend
To avoid these issues, we plan to schedule meeting times far in advance, and will be flexible on both weekdays and weekends. We will also gain access to the hardware and software as soon as possible so that time may be spent overcoming challenging code or hardware issues.

# Project Updates
## 4/27/2015
See the file "Project Updates - Radio Collar Tracker.pdf" for details on our progress thus far. Up until this point we have completed our first milestone: get up to speed with the Piksi GPS hardware. This milestone is hard to quantify, but we included it to show that we did read documentation, watch YouTube videos, and get some hands on experience with the Piksi hardware. 

We are currently working to effectively run the RTK GPS with two laptops (one serving as a base station, and one serving as a rover). This process began by testing on two Raspberry Pis running Linux; however, this gave us difficulties as the operating systems were not compatible with the Piksi tools needed. We then changed our approach and were able to get RTK GPS working for a short time using a PC as the base station and a Mac as the rover. We will continue to work on getting Linux to work before the deadline of 5/5/2015.

# Thank You
